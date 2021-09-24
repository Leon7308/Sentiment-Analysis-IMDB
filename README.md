Research Group Project

Description 
This project is a simple implementation of Sentiment Analysis using a ‘bag of words’ approach. The database used was a simple IMBD review dataset and the model classifies these reviews into ‘Positive’ and ‘Negative’ reviews.  The project was created on the Google Colab platform and is also uploaded on Github. 

Dataset Used 
The ‘IMDB Movie Review Dataset transform into CSV files’ dataset was used for this project which contains two columns – Review of the movie and the sentiment label (0 for negative and 1 for positive). All the movie reviews are long sentences (most of them more than 200 words). 

Technique Used
I used a ‘bag of words’ approach in this project which means we represent a sentence as a bag of words vector which stores how many times a word occurs in a sentence. We then use TF-IDF to reflect how important a word is in a sentence. TF represents how many times a word occurs in a sentence divided by total words in a sentence and IDF is the log of total sentences by number of sentences containing a word. TF and IDF are then multiplied to determine how relevant a word is. This data is then given to a Neural Network to form the final model. So overall,
1.	Import dataset - I have used Google colab’s drive feature. So, to run the code, you need to have the dataset in the mentioned directory (/content/drive/My Drive/sentiment_analysis/) in google drive. 
2.	Read dataset using pandas - I have used the first 2000 values of the train data and the first 200 values of test and validate data. 
3.	Process the data – For pre-processing the text, I have converted the text to lowercase, removed punctuations and removed stop words like I, in, at, etc. 
4.	Apply TF-IDF – Apply the TF-IDF vectorizer to transform the data into a bag of words vector.
5.	Define and fit model – Define the Neural Network model and train the model using the processed train vector. We plot two simple graphs to check Training and Validation Loss (The lower the better) and Training and Validation accuracy (The Higher the better though very high training accuracy could indicate overfitting)
6.	Test model – Test the model against the Test Data Vector





Assumptions 
1.	Since we are using a bag of words approach, we assume that the order of words in a sentence does not matter. 
2.	We assume every review can be classified as ‘positive’ or ‘negative’ instead of having mixed reviews. 
3.	The bag of words assumes all words have different meanings. It does not club words with the same meanings together 

Links

•	Project on Google Colab - https://colab.research.google.com/github/Leon7308/Sentiment-Analysis-IMDB/blob/master/Archit_Sengupta_Sentiment_Analysis.ipynb

•	Database - https://www.kaggle.com/columbine/imdb-dataset-sentiment-analysis-in-csv-format
