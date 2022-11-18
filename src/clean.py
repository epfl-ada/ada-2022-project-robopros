from typing import Sequence
import pandas as pd


def explode_dict(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Takes a column with dictionary values of form {freebase_id:value} and explodes
    them, i.e. creates one new row for each value of that dictionary.
    """
    result = df.copy()
    # Convert dictionary to iterable of values
    result[column] = df[column].apply(eval).apply(dict.values)
    # Explode on that iterable
    return result.explode(column)


def filter_unique_countries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops all movies that originate from multiple countries.
    It stores the result in a pickle for faster reuse, as this
    method can take a bit of time.
    """
    pickle = "./df_movies_unique.pickle"
    try:
        return pd.read_pickle(pickle)
    except:
        # Return only movies that come from a single country
        df = df.groupby("Wikipedia_Movie_ID").filter(
            lambda x: x.Movie_Countries.nunique() == 1
        )
        pd.to_pickle(df, pickle)
        return df


def movies_and_countries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame with each movie ID associated with its country of origin.
    """
    return df[["Wikipedia_Movie_ID", "Movie_Countries"]].drop_duplicates()


def keep_countries(df: pd.DataFrame, countries: Sequence[str]) -> pd.DataFrame:
    """
    Drops all movies that do not come from the given list of countries.
    """
    return df[df.Movie_Countries.isin(countries)]


def align_movie_countries(
    characters: pd.DataFrame, movies: pd.DataFrame
) -> pd.DataFrame:
    """
    Adds the Movie_Countries column from the movies DataFrame to the character
    DataFrame.
    """
    return (
        movies[["Wikipedia_Movie_ID", "Movie_Countries"]]
        .drop_duplicates()
        .merge(characters, on="Wikipedia_Movie_ID")
    )


def align_year_and_decade(
    summaries: pd.DataFrame, movies: pd.DataFrame
) -> pd.DataFrame:
    """
    Aligns the year and decade columns from the movies dataframe to the summaries
    dataframe.
    """
    return summaries.merge(
        movies[["Wikipedia_Movie_ID", "year", "decade"]],
        on="Wikipedia_Movie_ID",
        how="inner",
    )


def parse_dates(df: pd.DataFrame):
    """
    Parses movie release dates into datetime for the given DataFrame.
    Note that this drops every row that has no movie release date.
    """
    df["Movie_Release_Date"] = pd.to_datetime(df["Movie_Release_Date"])
    return df[~df.Movie_Release_Date.isna()].copy()


def date_differences(movies: pd.DataFrame, characters: pd.DataFrame) -> int:
    """
    Counts the number differences in movie release dates between the movies and characters
    DataFrame. This is used as a sanity check to see whether there are any inconsistencies.
    """
    merged = pd.merge(
        movies[["Wikipedia_Movie_ID", "Movie_Release_Date"]],
        characters[["Wikipedia_Movie_ID", "Movie_Release_Date"]],
        on="Wikipedia_Movie_ID",
    )
    return (merged.Movie_Release_Date_x != merged.Movie_Release_Date_y).sum()


def keep_dates(df: pd.DataFrame, min_year: int, max_year: int) -> pd.DataFrame:
    """
    Filters movie rows that are released in the given year interval.
    """
    return df[
        (df.Movie_Release_Date.dt.year >= min_year)
        & (df.Movie_Release_Date.dt.year <= max_year)
    ].copy()


def add_year_and_decade(df: pd.DataFrame):
    """
    Adds a year and decade column for the given movie release dates.
    """
    df["year"] = df.Movie_Release_Date.dt.year
    df["decade"] = df.year - (df.year % 10)


def drop_undefined_actors(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.Freebase_Actor_ID.notna()]
