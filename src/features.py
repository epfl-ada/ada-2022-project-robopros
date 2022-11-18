import pandas as pd
import aggregate


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
