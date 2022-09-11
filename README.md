# Google Search Accuracy Check
Scrapes top ten sites from google based on a query and reviews search ranking accuracy with cosine similarity.

## Explanation
This project will use a webscraper to get content from the top ten results from a website based on a user inputted query and then will index this content for further analysis using the beautiful soup library. Then developed cosine similarity checker will cross reference each document and re rank them based on this, the rankings are then compared based on the original search rankings to the new. Synonyms, antonyms, filtered out stop words and lemmatization will be used to get these rankings.

### Tasks:
- Build web scraper
- Analyse search results
- Enhance queries
- Compare



### Using
- Beautiful soup 4 for scraping and comparison
- Using NLTK stem, corpus tokenizing
- Python
