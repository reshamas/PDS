'''
import the module we are going to use
'''
# json/simplejson is the standard module to encode and decode .json files
try: import simplejson as json
except ImportError: import json
# The os module provides a portable way of using operating system dependent functionality.
import os
# The next module implements specialized container datatypes providing alternatives to 
# Python's general purpose built-in containers, dict, list, set, and tuple.
from collections import defaultdict


'''
Main Script
'''
# Data Processing
print('Data Processing')

# 1. Download the file user_tag_activity.json
print('1st Question')
#os.system('curl -O http://people.stern.nyu.edu/ja1517/data/user_tag_activity.json')

# How many unique users are there? How many unique objects and responses?
f = open('user_tag_activity.json', 'r') # open the file to read
users = set() # The sets module provides classes for constructing and manipulating unordered collections of unique elements.
objects = set()
responses = set() 
for line in f:
    data = json.loads(line)
    users.add(str(data['user']))
    objects.add(str(data['object']))
    responses.add(str(data['response']))
f.close()
print('Unique users: ' + str(len(users)))
print('Unique objects: ' + str(len(objects)))
print('Unique responses: ' + str(len(responses)))
print('')

# You can also use counters to answer this question



# 2. Real data is often dirty- filter any tuples with NULL fields. 
print('2nd Question')
os.system("grep -v 'NULL' user_tag_activity.json > user_tag_activity2.json")
print('We filtered the tuples with NULL fields..')
print('')


# 3. What are the 5 users with the highest rejection rate? What are the 5 users 
#    with the greatest number of rejections? 
print('3rd Question')
rejections = defaultdict(int)  #http://docs.python.org/library/collections.html#defaultdict-objects
submissions = defaultdict(int)
rejectionRates = defaultdict(lambda: 0) # alternative way to initialize our dictionary

f = open('user_tag_activity2.json', 'r')
for line in f:
    data = json.loads(line)
    submissions[str(data['user'])] += 1
    if (str(data['accepted']) == '0'):
        rejections[str(data['user'])] += 1
f.close()

for user in submissions.keys():
    rejectionRates[user] = float(rejections[user])/submissions[user]

# Again, you can also use counters to answer these questions

# Then, you can simply iterate directly over the dictionaries or  
# use a pythonic way:
top5UsersByRejectionRate = sorted(rejectionRates, key=rejectionRates.get, reverse=True)[:5]
top5UsersByRejections = sorted(rejections, key=rejections.get, reverse=True)[:5]

print('The 5 users with the highest rejection rate:')
for key in top5UsersByRejectionRate:
    print('Order: ' + str(top5UsersByRejectionRate.index(key)+1) + '\t User: ' + str(key) + '\t Rejection Rate: ' + str(rejectionRates[key]))
print('')

print('The 5 users with the greatest number of rejections:')
for key in top5UsersByRejections:
    print('Order: ' + str(top5UsersByRejections.index(key)+1) + '\t User: ' + str(key) + '\t Rejections: ' + str(rejections[key]))
print('')


# 4. What are the 5 responses with the highest rejection rate? If we were to try to 
#    automate the rejection process by rejecting the these responses, how many good 
#    (accepted) tags would erroneously be rejected?
print('4th Question')
rejections = defaultdict(int) 
submissions = defaultdict(int)
rejectionRates = defaultdict(int)

# Just for clarity, we load the same data set.
# In general, loading the same data set more than once is not a good practice. 
f = open('user_tag_activity2.json', 'r')
for line in f:
    data = json.loads(line)
    submissions[str(data['response'])] += 1
    if (str(data['accepted']) == '0'):
        rejections[str(data['response'])] += 1
f.close()

for response in submissions.keys():
    rejectionRates[response] = float(rejections[response])/submissions[response]

top5ResponsesByRejectionRate = sorted(rejectionRates, key=rejectionRates.get, reverse=True)[:5]

print('The 5 responses with the highest rejection rate:')
for key in top5ResponsesByRejectionRate:
    print('Order: ' + str(top5ResponsesByRejectionRate.index(key)+1) + '\t Response: ' + str(key) + '\t Rejection Rate: ' + str(rejectionRates[key]))
print('')


falseNegatives = 0
f = open('user_tag_activity2.json', 'r')
for line in f:
    data = json.loads(line)
    if (str(data['response']) in top5ResponsesByRejectionRate) and (str(data['accepted']) == '1'):
        falseNegatives += 1
f.close()

print('''If we were to try to automate the rejection process by rejecting these 
responses, we would reject ''' + str(falseNegatives) + ' tags!')   
print('')   


# 5. Similarly, some users may be more trustworthy than others. Find the 5 users with 
#    the greatest number of accepted responses. If one were to always accept responses 
#    from these users, how many "bad" tags would erroneously be accepted? 
print('5th Question')

acceptances = defaultdict(int) 
    
f = open('user_tag_activity2.json', 'r')
for line in f:
    data = json.loads(line)
    if (str(data['accepted']) == '1'):
        acceptances[str(data['user'])] += 1
f.close()

top5UsersByAcceptances = sorted(acceptances, key=acceptances.get, reverse=True)[:5]

print('The 5 users with the greatest number of acceptances:')
for key in top5UsersByAcceptances:
    print('Order: ' + str(top5UsersByAcceptances.index(key)+1) + '\t User: ' + str(key) + '\t Acceptances: ' + str(acceptances[key]))
print('')

falsePositives = 0
f = open('user_tag_activity2.json', 'r')
for line in f:
    data = json.loads(line)
    if (str(data['user']) in top5UsersByAcceptances) and (str(data['accepted']) == '0'):
        falsePositives += 1
f.close()

print('''If one were to always accept responses from the 5 users with the greatest 
number of acceptances, we would accept ''' + str(falsePositives) + ' "bad" tags!')   
