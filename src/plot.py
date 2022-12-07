import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple


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


def ethnic_ratio_countries(df: pd.DataFrame):
    """
    Creates 5 figures comparing the distribution of the top 5 ethnic groups for each country.
    The distributions are visualized as barplots.
    """
    data_max = df.max().Fraction

    ax1 = plt.subplot2grid(shape=(2, 6), loc=(0, 0), colspan=2)
    ax2 = plt.subplot2grid((2, 6), (0, 2), colspan=2)
    ax3 = plt.subplot2grid((2, 6), (0, 4), colspan=2)
    ax4 = plt.subplot2grid((2, 6), (1, 1), colspan=2)
    ax5 = plt.subplot2grid((2, 6), (1, 3), colspan=2)

    ax1.set_ylim([0 - data_max / 10, data_max + data_max / 10])
    ax2.set_ylim([0 - data_max / 10, data_max + data_max / 10])
    ax3.set_ylim([0 - data_max / 10, data_max + data_max / 10])
    ax4.set_ylim([0 - data_max / 10, data_max + data_max / 10])
    ax5.set_ylim([0 - data_max / 10, data_max + data_max / 10])

    df.loc['France'].plot(kind='bar', title='France', ax=ax1)
    df.loc['India'].plot(kind='bar', title='India', ax=ax2)
    df.loc['Japan'].plot(kind='bar', title='Japan', ax=ax3)
    df.loc['United Kingdom'].plot(kind='bar', title='United Kingdom', ax=ax4)
    df.loc['United States of America'].plot(kind='bar', title='United States', ax=ax5)

    ax1.legend().remove()
    ax2.legend().remove()
    ax3.legend().remove()
    ax4.legend().remove()
    ax5.legend().remove()

    plt.subplots_adjust(hspace=2, wspace=15)
    plt.suptitle("Distribution of Top 5 Ethnic Groups in the Big 5 Movie Industries")
    plt.show()


def height_decades(dfs: Tuple[pd.DataFrame, pd.DataFrame], gender: str):
    """
    Creates two plots showing the height distributions over decades for the different movie industries.
    """
    fig, ax = plt.subplots(2, figsize=(10, 10))
    plt.tight_layout(pad=3)
    sns.set(style="ticks")
    ax[0].set_title(f'Shortest {gender} Actor')
    ax[1].set_title(f'Tallest {gender} Actor')
    sns.lineplot(data=dfs[0], x="decade", y="Actor_Height", hue="Movie_Countries", ax=ax[0])
    sns.lineplot(data=dfs[1], x="decade", y="Actor_Height", hue="Movie_Countries", ax=ax[1])
    plt.show()
