# Globywood: the story of movie industries across time.

**Project structure (reference for grading)**

Final (milestone 3) notebook: [notebooks/milestone3.ipynb](notebooks/milestone3.ipynb)

Website: https://louisgevers.github.io/ada-robopros-website/

To keep the notebook clean we make use of python functions in our [src](src) folder. For exact implementation details refer to:
- [aggregate.py](src/aggregate.py) = functions for aggregate statistics on our dataframes (e.g. number of movies)
- [clean.py](src/clean.py) = functions for cleaning our data
- [load.py](src/load.py) = functions for loading the data in the appropriate dataframes
- [plot.py](src/plot.py) = plotting function
- [features.py](src/features.py) = extracting features of interest from out processed dataframes
- [nlp_modules.py](src/nlp_modules.py) = helper functions for NLP processing

## Abstract

Cinema made its debut in the late 19th century [1] and has become a multibillion-dollar industry, distributed over many different countries, and therefore made subject to distinct cultures and trends.
Using the CMU Movie Summary Corpus, a collection of 42.306 movie plot summaries extracted from Wikipedia, aligned with movie and character metadata, we take a trip through time to take a look at these trends and how they have (or have not) differed across the world.
We will analyze movies from some of the largest film industries - namely the United States, India, United Kingdom, Japan, and France [2] - from the 1950s to the 2010s.
More specifically, we will look from two different perspectives, the movies themselves and the actors that portray them.
This will give us an insight into whether the industry is converging due to globalization, or if each industry can keep its identity.

## Research questions

Our main research question is the following:

*"What are the differences between the largest movie industries and how have they changed over time?"*

This question can be split into three perspectives, each having its subquestions:

1. Differences in movies
   - What are the differences in typical movie attributes (main genres, typical durations) between industries?
   - What are the differences in movie plots between industries? E.g., are action movies semantically similar across the world?
   - Have these differences remained the same over time?
2. Differences in actors
   - Is the distribution of physical attributes (age, gender, height) the same across countries?
   - Are there differences in diversity representations across countries?
   - For these representations, is the effect of time or country stronger?
3. Differences in plot summaries
   - How does the lexic used to write the summaries look like?
   - Whate are the specification of plot summaries across different attributes (decades, industries, country)
 

## Methods

### Datasets

We make use of the following raw datasets:
- `movie.metadata.tsv`: movie metadata
- `character.metadata.tsv`: character and actor metadata
- `plot_summaries.txt`: movie plots

And split it into the following datasets:
- Dataset D1: Dataset containing metadata about movies (movie duration, genres, country, ...). This dataset will also be used to group our data by country and by date.
- Dataset D2: Dataset containing the movie plots, aligned with country and date.
- Dataset D3: Dataset containing information about movie characters and the corresponding actors, aligned with country and date.
  - D3.1: Subset with available actors' ages
  - D3.2: Subset with available actors' gender
  - D3.3: Subset with available actors' ethnicities
  - D3.4: Subset with available actors' heights

### Trends In Movie Industries Analysis

We want to see how different features of movies in different countries have evolved over time. 

- Runtimes: We want to see whether movie runtimes of different countries are significantly different. We also want to see the trend of the movie runtimes over time of the selected countries. Before analysis, we conducted some filtering. For the movies with short runtimes, we checked for potential errors and verified that those runtimes were indeed valid. On the other hand, for “super long” movies, we could not verify the length of the longest movie in the dataset. Additionally, we noticed movies above 300 mins were experimental movies and thus outliers. Therefore, we decided to exclude these long movies and the movies with missing runtime data from our analysis. We will subsequently use statistical tests to find potential differences.

- Revenue: The majority of the revenue of the movies is missing (83.3%).
Moreover, there are many potential outside cofounders like inflation over time in across countries. Finally, the revenue of movies does not tell us much about the types of movies made. Therefore, we decided not to do any further analysis on revenue. 

- Genres: We would like to see the distribution of different genres in different countries. This could be on one hand the most frequently produced genres, but we will also align the genres with the average ratings from IMDB to compare the most popular genres. We can then visualize whether the distribution of genres converged or diverged for the selected countries.

### Diversity Analysis

Since the data contains more information from Hollywood movies than any other movie industry, the analysis has to be
adjusted by looking at the big 5 movie industries separately and by comparing their relative numbers. The data is
enriched with information about the decade so that the development over the years can be analyzed. The preprocessing
steps include sanity checks and :
- Removal of errors, meaning, setting age and height into meaningful ranges
- complement age data by converting data about movie release date and actors' date of birth into date format and
calculating the age
- Movies which contain flashbacks to older movies have to be filtered out as the actors are no longer active during
the time the film was produced (they confound the data)
- Matching of Freebase IDs to the actual term of the ethnic group; for that
SPARQL was used to get the corresponding terms from Wikidata in form of a JSON file which could be used to map the IDs;
Not all IDs can be matched, but were left in the dataset as the number of ethnicities can be useful for analysis
- Gender was only divided into male and female; Creation of indicator variables for male and female
- Visualization of the data to find inconsistencies and get first insights

For continuous data like age and height the distributions and their statistics can be analyzed (e.g. mean, median).
Categorical data like ethnicity and gender are compared with ratios.

In general the data is prepared to find possible correlations later on with other gained insights e.g. success metrics
of the movies. The different chosen measures for diversity can be combined by using a weighted average depending on how
much data was available or by using regression as a descriptive data analysis tool.  

### Movie plots

To compare movie plots across countries over time we will make use of NLP techniques.

First, we study the frequent words used across the plots for different decades, industries and countries.


In addition we embed the plots using the sentence transformer model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model enables us to identify the semantic differences in paragraphs while being light to encode, and requiring little computation. 

We use later on TSNE on the embeddings to be able to visualize and understand the relationships between embeddings in a continous vector space. This allow us to determine if there is a difference between decades, countries, genres and how they are affected across different attributes.

Overall, this approach has the potential to give you a deeper understanding of the similarities and differences between movie plots across different time periods, industries, and countries.

In this work, we provide as well a method to extract keypoint from plots. This can be used in 2 different areas, namely to either extract a key point from a plot or from a set of plots. Our approach guarantee that we dont get repetitive kp and to have them general the more we input different sentences as we are computing 1:1 cosine similarity between each sentence embeddings and filter to get the candidates to be as distinct as possible from other kp candidates. 

It operates as following
1. Break the summary into sentences.
2. Calculate the cosine similarity between each sentence's embeddings and perform page_rank to leave the sentences with the highest similarity score.
3. Given the sentences chosen through page_rank, we perform filtering to get the N (set by user) sentences that are more distinguished from one another and don't cover the same topic for them to be general.
4. This gives us the main X keypoint in order.

## Proposed timeline

| Date | Goal |
|-|-|
| 25/11/2022 | Complete collection and cleaning of IMDB ratings and align them with datasets |
| 30/11/2022 | (Continuing analyses and focus on Homework 2) |
| 02/12/2022 | **Homework 2 deadline** |
| 05/12/2022 | Complete all analyses |
| 09/12/2022 | Draft the final datastory outline |
| 16/12/2022 | Create all visualizations for datastory and complete final text |
| 20/12/2022 | Complete GitHub pages datastory |
| 23/12/2022 | **Milestone 3 deadline** |


## Team contributions

| Team member | Responsibilities |
|-|-|
| Radia | Analyis of differences between movies, datastory |
| Tim | Diversity analysis of actors (age, height, gender, ethnicity, combined) |
| Ray | Analysis of movie summaries using NLP |
| Louis | Data wrangling and pipeline setup, create website, datastory |

## Sources

[1] S. Pruitt, “The Lumière Brothers, Pioneers of Cinema,” HISTORY. https://www.history.com/news/the-lumiere-brothers-pioneers-of-cinema (accessed Nov. 17, 2022).

[2] “Global Box Office Down 72%, Digital Leads Home Entertainment in 2020,” Boxoffice, Mar. 26, 2021. https://www.boxofficepro.com/global-box-office-down-72-digital-leads-home-entertainment-in-2020/ (accessed Nov. 16, 2022).


---

## Setting up the project 
### Dataset
To start with please download the CMU Movie Summary Corpus [Datasets](https://www.cs.cmu.edu/~ark/personas/) and locate them in the `data` folder. 
### Project Dependencies 
After activating your virtualenv in the root directory of the project install the necessary Dependencies by running
```bat
pip install requirements.txt
```
The requirement list will be updated and added along the project to make a reproducible code 

