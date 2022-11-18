import pandas as pd
from typing import Tuple, List


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


def stats_age_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get statistics of actors' ages grouped by countries.
    """
    return df.groupby('Movie_Countries')['Actor_Age_at_Movie_Release'].describe()


def not_assigned_fb_ids(df: pd.DataFrame) -> List[str]:
    """
    Returns the not assigned Freebase IDs.
    """
    not_found_ethn = []
    for ethn in df.Actor_Ethnicity.unique():
        if '/' in ethn:
            not_found_ethn.append(ethn)

    return not_found_ethn


def ethnicities_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the number of different ethnicities grouped by countries.
    """
    return df.groupby(['Movie_Countries', 'decade']).Actor_Ethnicity.nunique()


def max_min(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns the minimum and maximum values grouped by country and decade.
    """
    min_v = df.groupby(['Movie_Countries', 'decade']).min(numeric_only=True)
    max_v = df.groupby(['Movie_Countries', 'decade']).max(numeric_only=True)
    return min_v, max_v
