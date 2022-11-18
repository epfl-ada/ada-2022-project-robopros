import pandas as pd


def nmovies(df: pd.DataFrame) -> int:
    """
    Returns the number of movies in the given movie metadata DataFrame.
    Note that the movie DataFrame can contain multiple rows for the same
    movie (one for each genre, language & country). We therefore have to
    count the number of unique Wikipedia_Movie_IDs.
    """
    if df.Wikipedia_Movie_ID.hasnans:
        print("WARNING: DataFrame contains movie IDs that are undefined")
    return df.Wikipedia_Movie_ID[df.Wikipedia_Movie_ID.notna()].nunique()


def ncharacters(df: pd.DataFrame) -> int:
    """
    Returns the number of characters in the given character metadata DataFrame.
    """
    return df.Freebase_Char_ID.nunique()


def nactors(df: pd.DataFrame) -> int:
    """
    Returns the number of actors in the given character metadata DataFrame.
    """
    if df.Freebase_Actor_ID.hasnans:
        print("WARNING: DataFrame contains actor IDs that are undefined")
    return df.Freebase_Actor_ID[df.Freebase_Actor_ID.notna()].nunique()


def ncountries(df: pd.DataFrame) -> int:
    """
    Returns the number of countries in the given DataFrame.
    """
    if df.Movie_Countries.hasnans:
        print("WARNING: DataFrame contains countries that are undefined")
    return df.Movie_Countries[df.Movie_Countries.notna()].nunique()


def top_countries_nmovies(df: pd.DataFrame, n=10) -> pd.Series:
    """
    Returns the n countries with most number of movies in the given
    DataFrame in descending order.
    """
    return (
        df[["Wikipedia_Movie_ID", "Movie_Countries"]]
        .groupby("Movie_Countries")
        .nunique()
        .sort_values("Wikipedia_Movie_ID", ascending=False)
        .head(n)
    )
