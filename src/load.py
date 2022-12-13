import numpy as np
import pandas as pd
import clean
from typing import Tuple

# Data directories
DATA_DIR = "../data"
MOVIES_DIR = f"{DATA_DIR}/MovieSummaries"
NLP_DIR = f"{DATA_DIR}/corenlp_plot_summaries"

# Files
CHARACTER_META_FILE = f"{MOVIES_DIR}/character.metadata.tsv"
MOVIE_META_FILE = f"{MOVIES_DIR}/movie.metadata.tsv"
NAME_CLUSTERS = f"{MOVIES_DIR}/name.clusters.txt"
PLOT_SUM = f"{MOVIES_DIR}/plot_summaries.txt"
TVTROPES_CLUSTERS = f"{MOVIES_DIR}/tvtropes.clusters.txt"

# Columns
CHARACTER_META_COLS = [
    "Wikipedia_Movie_ID",
    "Freebase_Movie_ID",
    "Movie_Release_Date",
    "Character_Name",
    "Actor_DOB",
    "Actor_Gender",
    "Actor_Height",
    "Actor_Ethnicity",
    "Actor_Name",
    "Actor_Age_at_Movie_Release",
    "Freebase_Char_Actor_Map_ID",
    "Freebase_Char_ID",
    "Freebase_Actor_ID",
]
MOVIE_META_COLS = [
    "Wikipedia_Movie_ID",
    "Freebase_Movie_ID",
    "Movie_Name",
    "Movie_Release_Date",
    "Revenue",
    "Movie_Runtime",
    "Movie_Languages",
    "Movie_Countries",
    "Movie_Genres",
]
NAME_CLUSTERS_COLS = ["Character_Name", "Freebase_Char_Actor_Map_ID"]
PLOT_SUM_COLS = ["Wikipedia_Movie_ID", "Summary"]
TVTROPES_COLS = ["Character_Type", "Character_Description"]


def character_metadata() -> pd.DataFrame:
    """
    Loads the character metadata file into a DataFrame.
    It stores it into a pickle for faster subsequent loading.
    """
    pickle = "./df_character_raw.pickle"
    try:
        return pd.read_pickle(pickle)
    except:
        df = pd.read_csv(CHARACTER_META_FILE, sep="\t", names=CHARACTER_META_COLS)
        pd.to_pickle(df, pickle)
        return df


def movie_metadata() -> pd.DataFrame:
    """
    Loads the movie metadata file into a DataFrame.
    It explodes the movie languages, countries, and genres into multiple
    rows, such that each column contains a single value rather than a dictionary
    of values.
    It stores it into a pickle for faster subsequent loading.
    """
    pickle = "./df_movies_raw.pickle"
    try:
        return pd.read_pickle(pickle)
    except:
        df = pd.read_csv(MOVIE_META_FILE, sep="\t", names=MOVIE_META_COLS)
        # Explode dictionaries into separate rows
        df = clean.explode_dict(df, "Movie_Languages")
        df = clean.explode_dict(df, "Movie_Countries")
        df = clean.explode_dict(df, "Movie_Genres")
        pd.to_pickle(df, pickle)
        return df


def name_clusters() -> pd.DataFrame:
    """
    Loads the name cluster file into a DataFrame.
    We will not use this DataFrame in our analysis.
    """
    return pd.read_csv(NAME_CLUSTERS, sep="\t", names=NAME_CLUSTERS_COLS)


def plot_summaries() -> pd.DataFrame:
    """
    Loads the plot summaries into a DataFrame.
    """
    return pd.read_csv(PLOT_SUM, sep="\t", names=PLOT_SUM_COLS)


def character_types() -> pd.DataFrame:
    """
    Loads the character types file into a DataFrame.
    We will not use this DataFrame in our analysis.
    """
    return pd.read_csv(TVTROPES_CLUSTERS, sep="\t", names=TVTROPES_COLS)


def release_birth_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get data with missing information about the actors' ages but with information about the actors' date of
    birth and the movie release date.
    """
    return df[df.Actor_Age_at_Movie_Release.isnull()].dropna(subset=['Actor_DOB', 'Movie_Release_Date'])


def gender_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate gender ratio (female / male) and save results in new dataframe.
    """
    grouped_gender = df.groupby(['decade', 'Movie_Countries'])
    gr = grouped_gender['Actor_Gender_F'].sum().div(grouped_gender['Actor_Gender_M'].sum())
    return pd.DataFrame(gr, columns=['Ratio F/M'])


def indicator_mf(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data with created indicator variables of male / female.
    """
    indicator = pd.get_dummies(df, columns=['Actor_Gender'])
    female_age = indicator[indicator.Actor_Gender_F == 1]
    male_age = indicator[indicator.Actor_Gender_M == 1]
    return female_age, male_age


def ethnicity_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the ratio of number of unique ethnicities / number of actors (with data about their ethnicity).
    """
    return df.groupby(['Movie_Countries', 'decade']).Actor_Ethnicity.nunique().div(
        df.groupby(['Movie_Countries', 'decade']).Actor_Ethnicity.count())


def top_n_ethnic(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """
    Returns the top n ethnic groups.
    """
    top_ethn = df.groupby('Movie_Countries').Actor_Ethnicity.value_counts()
    top_ethn = top_ethn.groupby('Movie_Countries').nlargest(n).to_frame().droplevel(0)
    return top_ethn.rename(columns={'Actor_Ethnicity': 'Count'})


def std_full(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a proper dataframe to apply linear regression.
    """
    age_diversity = pd.DataFrame(df.values, columns=['std'])
    decades = [1950, 1960, 1970, 1980, 1990, 2000, 2010,
               1950, 1960, 1970, 1980, 1990, 2000, 2010,
               1950, 1960, 1970, 1980, 1990, 2000, 2010,
               1950, 1960, 1970, 1980, 1990, 2000, 2010,
               1950, 1960, 1970, 1980, 1990, 2000, 2010]
    countries = ['France', 'France', 'France', 'France', 'France', 'France', 'France',
                 'India', 'India', 'India', 'India', 'India', 'India', 'India',
                 'Japan', 'Japan', 'Japan', 'Japan', 'Japan', 'Japan', 'Japan',
                 'UK', 'UK', 'UK', 'UK', 'UK', 'UK', 'UK',
                 'US', 'US', 'US', 'US', 'US', 'US', 'US']
    age_diversity['decade'] = decades
    age_diversity['countries'] = countries
    return age_diversity


def contingency_table(df: pd.DataFrame):
    """
    Creates contingency table for chi-squared test.
    """
    observed_m = df.groupby('Movie_Countries').Actor_Gender_M.sum().to_numpy().reshape(1, -1)
    observed_f = df.groupby('Movie_Countries').Actor_Gender_F.sum().to_numpy().reshape(1, -1)
    observed = np.concatenate((observed_m, observed_f), axis=0)
    return observed


def diversity_full(div_fr: pd.DataFrame, div_in: pd.DataFrame, div_jp: pd.DataFrame,
                   div_uk: pd.DataFrame, div_us: pd.DataFrame) -> pd.DataFrame:
    countries = ['France', 'France', 'France', 'France', 'France', 'France', 'France',
                 'India', 'India', 'India', 'India', 'India', 'India', 'India',
                 'Japan', 'Japan', 'Japan', 'Japan', 'Japan', 'Japan', 'Japan',
                 'UK', 'UK', 'UK', 'UK', 'UK', 'UK', 'UK',
                 'US', 'US', 'US', 'US', 'US', 'US', 'US']
    combined = pd.concat((div_fr, div_in, div_jp, div_uk, div_us))
    total_div = pd.DataFrame(combined, columns=['diversity']).reset_index()
    total_div['countries'] = countries
    return total_div