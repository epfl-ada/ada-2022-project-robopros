# From Hollywood to Bollywood, an analysis of film industries across time.

**Project structure (reference for grading)**

Milestone 2 notebook: [notebooks/milestone2.ipynb](notebooks/milestone2.ipynb)

To keep the notebook clean we make use of python functions in our [src](src) folder. For exact implementation details refer to:
- [aggregate.py](src/aggregate.py) = functions for aggregate statistics on our dataframes (e.g. number of movies)
- [clean.py](src/clean.py) = functions for cleaning our data
- [load.py](src/load.py) = functions for loading the data in the appropriate dataframes
- [plot.py](src/plot.py) = plotting function

## Abstract

Cinema has made its debute in the late 19th century [1] and has become a multibillion dollar industry, distributed over many different countries, and therefore made subject to distinct cultures and trends.
Using the CMU Movie Summary Corpus, a collection of 42.306 movie plot summaries extracted from Wikipedia, aligned with movie and character metadata, we take a trip through time to take a look at these trends and how they have (or have not) differed across the world.
We will analyze movies from some of the largest film industries - namely United States, India, United Kingdom, Japan, and France [2] - from the 1950s to 2010s.
More specifically, we will look from two different perspectives, the movies themselves and the actors that portray in them.
This will give us an insight on whether the industry is converging due to globalization, or if each industry is able to keep their identity.

## Research questions

Our main research question is the following:

*"What are the differences between the largest movie industries and how have they changed over time?"*

This question can be split into two perspectives, each having their own subquestions:

1. Differences in movies
   - todo
2. Differences in actors
   - todo

## Additional datasets (if any)

To quantify a movie's success across industries, we collect the IMDB rating of the movies we are interested in per industry and decade through IMDB python library that seem to be more precise and give less nones than the beautifulsoup alternative. It is possible at a later point to collect other information such as production compagny and a more detailed information on the revenue or characters.  

## Methods
### NLP 
For the NLP task, we take the plot summaries of movies and we first embedd them using the sentence transformer model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model has of advantage that it allows to detect the semantic difference in paragraphs and is light to encode and doesn't require a lot of computation. Following, we visualize through TSNE how the summary embeddings of 2 different genres differs and if there is an overlap in order to break it slowly into subgroups that might be distincts (decade, country of movies, rating). The current results shows that there is some overlap between romance and action and will be studied more in P3, where we will be performing grouping and clustering on them. 
We as well made a keypoint extraction pipline that has of a goal to extract the most relevant event in a summary. It works as follow: 
1. Break the summary into sentences
2. Calculate the cosine similarity between each sentence's embeddings and perform page_rank to leave the sentences with the highest similarity score.
3. Given the sentences chosen through page_rank, we perform a filtering to get the N (set by user) sentences that are more distinguished between one another and dont cover the same topic for it to be general.
4. Congrats. that is the main event
## Proposed timeline

## Organization within the team

## Questions for TA (if any)

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
The requirement list will be updated and added along the project to make a reproducable code 

