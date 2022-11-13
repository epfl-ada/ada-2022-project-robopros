from typing import Sequence
import pandas as pd

def explode_dict(df: pd.DataFrame, column: str) -> pd.DataFrame:
    result = df.copy()
    # Convert dictionary to iterable of values
    result[column] = df[column].apply(eval).apply(dict.values)
    # Explode on that iterable
    return result.explode(column)

def filter_unique_countries(df: pd.DataFrame) -> pd.DataFrame:
    pickle = './df_movies_unique.pickle'
    try:
        return pd.read_pickle(pickle)
    except:
        # Return only movies that come from a single country
        df = df.groupby('Wikipedia_Movie_ID')\
            .filter(lambda x: x.Movie_Countries.nunique() == 1)
        pd.to_pickle(df, pickle)
        return df

def movies_and_countries(df: pd.DataFrame) -> pd.DataFrame:
    return df[['Wikipedia_Movie_ID', 'Movie_Countries']].drop_duplicates()

def keep_countries(df: pd.DataFrame, countries: Sequence[str]) -> pd.DataFrame:
    return  df[df.Movie_Countries.isin(countries)]

def add_countries_to_characters(characters: pd.DataFrame, movies: pd.DataFrame) -> pd.DataFrame:
    return movies[['Wikipedia_Movie_ID', 'Movie_Countries']].drop_duplicates()\
                .merge(characters, on='Wikipedia_Movie_ID')

def parse_dates(df: pd.DataFrame):
    df['Movie_Release_Date'] = pd.to_datetime(df['Movie_Release_Date'])
    return df[~df.Movie_Release_Date.isna()].copy()


def date_differences(movies: pd.DataFrame, characters: pd.DataFrame) -> int:
    merged = pd.merge(movies[['Wikipedia_Movie_ID', 'Movie_Release_Date']], characters[['Wikipedia_Movie_ID', 'Movie_Release_Date']], on='Wikipedia_Movie_ID')
    return (merged.Movie_Release_Date_x != merged.Movie_Release_Date_y).sum()

def keep_dates(df: pd.DataFrame, min_year: int, max_year: int) -> pd.DataFrame:
    return df[(df.Movie_Release_Date.dt.year >= min_year) & (df.Movie_Release_Date.dt.year <= max_year)].copy()

def add_year_and_decade(df: pd.DataFrame):
    df['year'] = df.Movie_Release_Date.dt.year
    df['decade'] = df.year - (df.year % 10)
