
import pandas as pd
import numpy as np
import scipy.stats as scistat

data = pd.read_json('train.json')

feature_cols = [col for col in data.columns if col in\
 ['request_id','requester_account_age_in_days_at_request',\
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

sep_data = data[feature_cols]
pizza = data[['request_id','requester_received_pizza']]

unstruc_data = data[['request_id','request_text','request_title']]

temp = pizza[pizza['requester_received_pizza'] == True]
yes_pizza = pd.merge(temp,sep_data, how = 'inner')
yes_unstruc_pizza = pd.merge(temp,unstruc_data, how = 'inner')

temp = pizza[pizza['requester_received_pizza'] == False]
no_pizza = pd.merge(temp,sep_data, how = 'inner')
no_unstruc_pizza = pd.merge(temp,unstruc_data, how = 'inner')

yes_text = yes_unstruc_pizza['request_text'].apply(lambda x: pd.value_counts(x.lower().split(" "))).sum(axis = 0)
no_text = no_unstruc_pizza['request_text'].apply(lambda x: pd.value_counts(x.lower().split(" "))).sum(axis = 0)

p_str = ['pizza','pizzas','pizza,','pizza.','pizza?','pizza!']
pl_str = ['please','please,','please.']
t_str = ['thank','thanks','thanks.','thanks!']

print
print "We would like to know if there is a way to increase our chances of getting pizza when posting to /r/random_acts_of_pizza."
print
print "How about trying to maximize the post score?"
print "The average post score for the redditors that recieved pizza is %d +/- %d."\
 % (np.mean(yes_pizza['requester_upvotes_minus_downvotes_at_request']), \
 scistat.sem(yes_pizza['requester_upvotes_minus_downvotes_at_request'])*1.96)
print "The average post score for the redditors that recieved no pizza is %d +/- %d."\
 % (np.mean(no_pizza['requester_upvotes_minus_downvotes_at_request']), \
 scistat.sem(no_pizza['requester_upvotes_minus_downvotes_at_request'])*1.96)
print "This gives us a t-value of %f and a p-value of %f." % (scistat.ttest_ind(\
yes_pizza['requester_upvotes_minus_downvotes_at_request'],\
no_pizza['requester_upvotes_minus_downvotes_at_request'],equal_var = False))
print "Which indicates that this is not a statistically significant difference."
print
print "What if we make sure to comment in our request posting a lot?"
print "The average number of comments in a 'yes' pizza post is %f +/- %f."\
 % (np.mean(yes_pizza['requester_number_of_comments_in_raop_at_request']), \
 scistat.sem(yes_pizza['requester_number_of_comments_in_raop_at_request'])*1.96)
print "The average number of comments in a 'no' pizza post is %f +/- %f."\
 % (np.mean(no_pizza['requester_number_of_comments_in_raop_at_request']), \
 scistat.sem(no_pizza['requester_number_of_comments_in_raop_at_request'])*1.96)
print "This gives us a t-value of %f and a p-value of %f." % (scistat.ttest_ind(\
yes_pizza['requester_number_of_comments_in_raop_at_request'],\
no_pizza['requester_number_of_comments_in_raop_at_request'],equal_var = False))
print "Which indicates that this is a statistically significant difference."
print
print "But what about looking at the actual text of the pizza request?"
print "The average amount of times 'pizza' was used in the 'yes' group was %f." % (float(sum(yes_text.loc[p_str]))/len(yes_pizza))
print "The average amount of times 'pizza' was used in the 'no' group was %f." % (float(sum(no_text.loc[p_str]))/len(no_pizza))
print
print "The average amount of times 'please' was used in the 'yes' group was %f." % (float(sum(yes_text.loc[pl_str]))/len(yes_pizza))
print "The average amount of times 'please' was used in the 'no' group was %f." % (float(sum(no_text.loc[pl_str]))/len(no_pizza))
print
print "The average amount of times 'thank' was used in the 'yes' group was %f." % (float(sum(yes_text.loc[t_str]))/len(yes_pizza))
print "The average amount of times 'thank' was used in the 'no' group was %f." % (float(sum(no_text.loc[t_str]))/len(no_pizza))
print
print "This tells us that we can increase our chances of getting a free pizza\
 if we comment in our own post but not necessarily if we somehow increase the post ranking."
print "Looking at the text tells us that saying 'please' has no measurable \
effect, but it might help to actually ask for pizza or thank people before you get pizza."