
#Import modules
#import csv
import pandas as pd
from sklearn import ensemble

#Open up the train csv
#temp2 = open('RAOP_Cleaned_Data.csv','rb')
#data = csv.reader(temp2)

data = pd.read_csv('RAOP_Cleaned_Data.csv')
test = pd.read_csv('RAOP_Cleaned_Test_File.csv')


feature_cols = [col for col in data.columns if col in\
 ['requester_account_age_in_days_at_request',\
 'requester_days_since_first_post_on_raop_at_request',\
 'requester_number_of_comments_at_request',\
 'requester_number_of_comments_in_raop_at_request',\
 'requester_number_of_posts_at_request',\
 'requester_number_of_posts_on_raop_at_request',\
 'requester_number_of_subreddits_at_request',\
 'requester_upvotes_minus_downvotes_at_request',\
 'requester_upvotes_plus_downvotes_at_request',\
 'unix_timestamp_of_request',\
 'unix_timestamp_of_request_utc']]
 
X_train = data[feature_cols]
X_test = test[feature_cols]
test_ids = test['request_id']
y = data['requester_received_pizza']

clf = ensemble.RandomForestClassifier(n_estimators = 500)
clf.fit(X_train, y)




with open("Test_Predict.csv", "wb") as ofile:
    ofile.write("request_id,requester_received_pizza\n")
    for e, val in enumerate(list(clf.predict_proba(X_test))):
        ofile.write("%s,%s\n"%(test_ids[e],val[1]))
