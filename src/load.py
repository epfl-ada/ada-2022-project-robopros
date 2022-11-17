import pandas as pd
import clean

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
