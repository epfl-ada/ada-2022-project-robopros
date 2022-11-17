# From Hollywood to Bollywood, an analysis of film industries across time.

**Project structure (reference for grading)**

Milestone 2 notebook: [notebooks/milestone2.ipynb](notebooks/milestone2.ipynb)

To keep the notebook clean we make use of python functions in our [src](src) folder. For exact implementation details refer to:
- [aggregate.py](src/aggregate.py) = functions for aggregate statistics on our dataframes (e.g. number of movies)
- [clean.py](src/clean.py) = functions for cleaning our data
- [load.py](src/load.py) = functions for loading the data in the appropriate dataframes
- [plot.py](src/plot.py) = plotting function

## Abstract

Cinema made its debut in the late 19th century [1] and has become a multibillion-dollar industry, distributed over many different countries, and therefore made subject to distinct cultures and trends.
Using the CMU Movie Summary Corpus, a collection of 42.306 movie plot summaries extracted from Wikipedia, aligned with movie and character metadata, we take a trip through time to take a look at these trends and how they have (or have not) differed across the world.
We will analyze movies from some of the largest film industries - namely the United States, India, United Kingdom, Japan, and France [2] - from the 1950s to the 2010s.
More specifically, we will look from two different perspectives, the movies themselves and the actors that portray them.
This will give us an insight into whether the industry is converging due to globalization, or if each industry can keep its identity.

## Research questions

Our main research question is the following:

*"What are the differences between the largest movie industries and how have they changed over time?"*

This question can be split into two perspectives, each having its subquestions:

1. Differences in movies
   - todo
2. Differences in actors
   - todo

## Additional datasets (if any)

To quantify a movie's success across industries, we collect the IMDB rating of the movies we are interested in per industry and decade through the IMDB python library which seems to be more precise and gives fewer nones than the beautifulsoup alternative. It is possible at a later point to collect other information such as production company and more detailed information on the revenue or characters.  

## Methods
### NLP 
For the NLP task, we take the plot summaries of movies and we first embed them using the sentence transformer model [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model has of advantage, in that it allows the detection of semantic differences in paragraphs and is light to encode, and doesn't require a lot of computation. Following, we visualize through TSNE how the summary embeddings of 2 different genres differ and if there is an overlap to break it slowly into subgroups that might be distinct (decade, country of movies, rating). The current results show that there is some overlap between romance and action and will be studied more in P3, where we will be performing grouping and clustering. 
In addition, we made a keypoint extraction pipeline that aims to extract the most relevant event in a movie. It works as follows: 
1. Break the summary into sentences
2. Calculate the cosine similarity between each sentence's embeddings and perform page_rank to leave the sentences with the highest similarity score.
3. Given the sentences chosen through page_rank, we perform filtering to get the N (set by user) sentences that are more distinguished from one another and don't cover the same topic for them to be general.
4. Congrats. that is the main event.
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
The requirement list will be updated and added along the project to make a reproducible code 

