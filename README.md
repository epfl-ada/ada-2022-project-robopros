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

IMDB ratings (@Ray if you can complement with exact source, perhaps format)

## Methods

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

