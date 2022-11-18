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


def runtime_distribution(runtimes: pd.DataFrame, log: bool):
    """
    Plots the runtime distribution.
    """
    fig = sns.histplot(data=runtimes, x="Movie_Runtime", log_scale=log)
    fig.set(
        title="Distribution of movie runtimes",
        xlabel="Movie runtime (minutes)",
        ylabel="Number of movies",
    )
    plt.show()


def runtime_comparison(runtimes: pd.DataFrame):
    """
    Creates two figures comparing runtimes across countries.
    One is a boxplot and compares all runtimes, the second one is
    a lineplot and compares them across time.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle("Comparison of movie durations")
    g = sns.boxplot(data=runtimes, x="Movie_Countries", y="Movie_Runtime", ax=axes[0])
    g.set(xlabel="Country", ylabel="Runtime (minutes)")
    g.set_xticklabels(["US", "UK", "Japan", "India", "France"])
    g = sns.lineplot(
        data=runtimes,
        x="decade",
        y="Movie_Runtime",
        hue="Movie_Countries",
        ax=axes[1],
    )
    g.set(xlabel="Decade", ylabel="Runtime (minutes)")
    g.get_legend().set_title("Country")
    plt.show()
