from typing import Sequence
import pandas as pd

def explode_dict(df: pd.DataFrame, column: str) -> pd.DataFrame:
    result = df.copy()
    # Convert dictionary to iterable of values
    result[column] = df[column].apply(eval).apply(dict.values)
    # Explode on that iterable
    return result.explode(column)

def filter_unique_countries(df: pd.DataFrame) -> pd.DataFrame:
    # Return only movies that come from a single country
    return df.groupby('Wikipedia_Movie_ID')\
            .filter(lambda x: x.Movie_Countries.nunique() == 1)

def movies_and_countries(df: pd.DataFrame) -> pd.DataFrame:
    return df[['Wikipedia_Movie_ID', 'Movie_Countries']].drop_duplicates()

def keep_countries(df: pd.DataFrame, countries: Sequence[str]) -> pd.DataFrame:
    return  df[df.Movie_Countries.isin(countries)]

def add_countries_to_characters(characters: pd.DataFrame, movies: pd.DataFrame) -> pd.DataFrame:
    return movies[['Wikipedia_Movie_ID', 'Movie_Countries']].drop_duplicates()\
                .merge(characters, on='Wikipedia_Movie_ID')
