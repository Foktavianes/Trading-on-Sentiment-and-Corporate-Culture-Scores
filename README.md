# Trading-on-Sentiment-and-Corporate-Culture-Scores
There are 3 steps required before the creation of trading strategy based on market sentiment, news sentiment and corporate culture scores. 
1. Generation of market index using PCA, PLS and Autoencoder
- We use five proxy variables which obtained from Jeffrey Wurgler’s personal website and S&P 500 monthly returns. The proxies are pdnd, ripo, nipo, s, cefd. Then, we apply PCA, PLS and Autoencoder to generate comprehensive market sentiment index.
- The data on proxy variables is obtained from Jeffrey Wurgler’s personal website while data on S&P 500 monthly returns is obtained from Bloomberg.
2. Scoring on news headlines to determine the news sentiment scores
- We used VADER package for sentiment analysis of news headlines to obtain sentiment score on each news headline. 
- The news headlines data is obtained from Seeking Alpha website.
3. Creation of culture dictionary to analyse and scores on each company corporate culture based on their conference call transcripts. 
- We used Question and Answers (Q&A) sections of 123,158 conference call transcripts between 2015 to 2019 for 8140 companies to generate a culture dictionary.
- There are several steps for the creation of culture dictionary. The first step is parsing the data using Stanford CoreNLP package. This allows for segmentation and tokenisation, lemmatisation and Named Entity Recognition (NER). Then, we use gensim library to perform dependency parsing to learn grammatical relationships in a sentence and helps to identify multi-word expression and compounds. Lastly, we use word2vec to convert the word to numerical vector which can be understood by machine, then we use a gensim library to predict each word's neighbouring words to create list of words with similar meaning.
- Example of our culture dictionary:
![image](https://user-images.githubusercontent.com/112449862/212245798-d19769c4-cbca-4ed9-93ff-07f5894d5345.png)
- After the creation of culture dictionary, we can score each transcript by taking equal weighted count of the number of words associated with each value divided by the total numebr of words in Q&A. 
- The data on conference call transcripts is obtained from Thomson Reuters StreetEvents
Building a trading strategy based on market sentiment scores, news sentiment scores and corporate culture scores

After the completion of all 3 steps above, we then can formulate our trading strategy. We needs to determine the parameter for the signal creation for our trading strategy:
- We only going to take positive market sentiment scores which created by PLS because PLS have better predictive power compared to PCA and Autoencoder.
- News sentiment scores with positive value and higher than 0.7. This is because we are able to observe greater impact with higher sentiment and we only consider long position. 
- We going to rank S&P 500 companies based on their culture scores and we identify top and bottom 30 for our trading tickers. We will do rebalancing of trading tickers every year, i.e the top 30 tickers in terms of culture scores in 2015 will be our trading tickers in 2016 while the top 30 tickers in terms of culture scores in 2016 will be our trading tickers in 2017 while 
-Our trading period is 4 years from 2016 to 2019 and we will trade on top and bottom 30 of S&P 500 companies in terms of culture scores. 
- The data on closing prices of S&P 500 companies are pulled from Yahoo Finance. 

Final result on cumulative return and sharpe ratio from sentiment based trading strategy
![image](https://user-images.githubusercontent.com/112449862/212240362-2419220d-327b-4093-83ca-8aafcde402af.png)
