import pandas as pd
import aggregate
from typing import Tuple


def runtimes(movies: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the movie dataframe with columns of interests for runtime. Drops rows that have no runtime.
    Note that we drop duplicates to make sure we have one row per ID. (assumption from the preprocessing)
    """
    runtimes = movies[
        [
            "Wikipedia_Movie_ID",
            "Movie_Name",
            "Movie_Runtime",
            "Movie_Countries",
            "decade",
        ]
    ].drop_duplicates()

    nmovies = aggregate.nmovies(runtimes)
    runtimes = runtimes[runtimes.Movie_Runtime.notna()]
    nmovies_filtered = aggregate.nmovies(runtimes)
    dropped = nmovies - nmovies_filtered

    print(
        f"{dropped:,} ({dropped/nmovies:.1%}) movies without runtime. Keeping {nmovies_filtered:,} ({nmovies_filtered/nmovies:.1%}) movies."
    )

    return runtimes


def country_split(df: pd.DataFrame, feature) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame,
                                                      pd.DataFrame]:
    """
    Split the dataframe into 5 different dataframes, one for each country.
    """
    df_fr = df[df.Movie_Countries == 'France'][feature]
    df_jp = df[df.Movie_Countries == 'Japan'][feature]
    df_in = df[df.Movie_Countries == 'India'][feature]
    df_uk = df[df.Movie_Countries == 'United Kingdom'][feature]
    df_us = df[df.Movie_Countries == 'United States of America'][feature]

    return df_fr, df_jp, df_in, df_uk, df_us
