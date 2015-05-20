This set of code is designed to give a prediction of the probability of a delivery of pizza on the reddit.com subreddit /r/Random_Acts_Of_Pizza. 

Files:
RAOP_Data_Cleaning.py
- This is to read in the test and training files, clean them, organize them, and print them out to reusable .csv files for testing.
- Yes. I did the first read in the hard way. Thought I would give it a try before going the much simpler (and easier) route. Both turn out just fine...but one is two lines vs. 30-40.

RAOP_Data_Inspect.py
- This (currently) runs sklearn's random forest classifier algorithm to determine the probability that a request for pizza will yield a pizza given all of the data. 
- It could definitely be further optimized by taking into account the types of words used by the requester. We could probably figure out a way to determine the tone which should give a better prediction. I am confident that it has a lot to do with how someone asks and their circumstances.

Prediction_Attempts Folder:
- This has all the current prediction attempts for the Kaggle competition this is related to. 
- Syntax: Test_Predict_(date)_(attempt no.)

RAOP_Cleaned_Data.csv
- The cleaned data for the training set.

RAOP_Cleaned_Test_File.csv
- The cleaned data for the test set.

test.json
- The json file for the test data.

train.csv
- The csv file with all the training data.