import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def movie_distribution_over_time(df: pd.DataFrame):
    """
    Plots the number of movies per countries over time.
    The first subplot displays the absolute counts, the second subplot displays
    the relative fraction of each country.
    """
    df = df[
        ["Wikipedia_Movie_ID", "Movie_Release_Date", "Movie_Countries"]
    ].drop_duplicates()

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle("Distribution of movies over time")

    g = sns.histplot(
        data=df,
        x="Movie_Release_Date",
        hue="Movie_Countries",
        multiple="stack",
        ax=axes[0],
    )
    g.get_legend().set_title("Country")
    g.set(xlabel="Movie release date", ylabel="Count")

    g = sns.histplot(
        data=df,
        x="Movie_Release_Date",
        hue="Movie_Countries",
        multiple="fill",
        ax=axes[1],
        legend=False,
    )
    g.set(xlabel="Movie release date", ylabel="Fraction of movies")

    plt.show()
