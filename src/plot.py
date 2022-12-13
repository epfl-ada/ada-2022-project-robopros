import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
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


def distributions_countries(df: pd.DataFrame, feature, title, logy=False):
    """
    Creates 5 figures comparing the distribution for each country.
    """

    ax1 = plt.subplot2grid(shape=(2, 6), loc=(0, 0), colspan=2)
    ax2 = plt.subplot2grid((2, 6), (0, 2), colspan=2)
    ax3 = plt.subplot2grid((2, 6), (0, 4), colspan=2)
    ax4 = plt.subplot2grid((2, 6), (1, 1), colspan=2)
    ax5 = plt.subplot2grid((2, 6), (1, 3), colspan=2)

    df[df.Movie_Countries == 'France'][feature].plot(kind='hist', title='France', ax=ax1, logy=logy)
    df[df.Movie_Countries == 'India'][feature].plot(kind='hist', title='India', ax=ax2, logy=logy)
    df[df.Movie_Countries == 'Japan'][feature].plot(kind='hist', title='Japan', ax=ax3, logy=logy)
    df[df.Movie_Countries == 'United Kingdom'][feature].plot(kind='hist', title='United Kingdom', ax=ax4, logy=logy)
    df[df.Movie_Countries == 'United States of America'][feature].plot(kind='hist', title='United States', ax=ax5,
                                                                       logy=logy)

    plt.subplots_adjust(hspace=2, wspace=15)
    plt.suptitle(title)
    plt.show()


def reg_coeff(result, title, x_ticks, log=False):
    """
    Plot the coefficients and their 95% confidence interval of the predictors for linear regression
    """
    # get coefficients and 95% confidence interval
    coef = result.params[1:]
    t = result.conf_int()[1] - result.conf_int()[0]
    if log == True:
        coef = np.exp(result.params[1:])
        t = np.exp(result.conf_int()[1]) - np.exp(result.conf_int()[0])
        plt.vlines(1, 0, len(coef), linestyle='--')
    else:
        plt.vlines(0, 0, len(coef), linestyle='--')

    plt.errorbar(coef, x_ticks, xerr=t[1:], fmt="o", color="r")
    plt.yticks(range(len(coef)), x_ticks)
    plt.ylabel('Predictors')
    plt.xlabel('Coefficients')
    plt.title(title)


def countries_decades(countries: pd.Series, decades: pd.Series, name):
    """
    Two plots to compare development over decades and countries.
    """
    fig, ax = plt.subplots(1, 2)
    countries.plot(kind='bar', ax=ax[0])
    decades.plot(kind='bar', ax=ax[1])
    ax[0].set_ylabel(name)
    ax[1].set_ylabel(name)
    fig.suptitle(f'{name} over Countries and Decades')
    plt.tight_layout()


def diversity(div_fr: pd.DataFrame, div_in: pd.DataFrame, div_jp: pd.DataFrame,
              div_uk: pd.DataFrame, div_us: pd.DataFrame):
    """
    Plot the diversity development of the different countries.
    """
    data_max = pd.concat([div_fr, div_in, div_jp, div_uk, div_us], axis=0).max()

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

    ax1.axhline(5, color='r', linestyle='--')
    ax2.axhline(5, color='r', linestyle='--')
    ax3.axhline(5, color='r', linestyle='--')
    ax4.axhline(5, color='r', linestyle='--')
    ax5.axhline(5, color='r', linestyle='--')

    div_fr.plot(kind='bar', title='France', ax=ax1)
    div_in.plot(kind='bar', title='India', ax=ax2)
    div_jp.plot(kind='bar', title='Japan', ax=ax3)
    div_uk.plot(kind='bar', title='United Kingdom', ax=ax4)
    div_us.plot(kind='bar', title='United States', ax=ax5)

    plt.subplots_adjust(hspace=2, wspace=15)
    plt.suptitle("Diversity in the Big 5 Movie Industries")
    plt.show()
    

