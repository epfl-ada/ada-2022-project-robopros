import pandas as pd

def nmovies(df: pd.DataFrame) -> int:
    return df.Wikipedia_Movie_ID.nunique()

def ncharacters(df: pd.DataFrame) -> int:
    return df.Freebase_Char_ID.nunique()

def nactors(df: pd.DataFrame) -> int:
    return df.Freebase_Actor_ID.nunique()

def ncountries(df: pd.DataFrame) -> int:
    return df.Movie_Countries.nunique()

def top_countries_nmovies(df: pd.DataFrame, n = 10) -> pd.Series:
    return df[['Wikipedia_Movie_ID', 'Movie_Countries']].groupby('Movie_Countries')\
                .nunique()\
                .sort_values('Wikipedia_Movie_ID', ascending=False)\
                .head(n)