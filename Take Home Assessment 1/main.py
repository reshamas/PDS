'''
import the module we are going to use
'''
# json/simplejson is the standard module to encode and decode .json files
try: import simplejson as json
except ImportError: import json

from collections import Counter, OrderedDict


'''
Main Script
'''
#number of customers
customers = 0 
f = open('assess1_data.json', 'r') # open the file to read
for line in f:
    data = json.loads(line) # load json entry
    customers += 1
f.close() # close the file
print('Number of customers: ' + str(customers))

# detect duplicates
names = [] # store names
duplicates = 0 
f = open('temp.json', 'r') # open the file to read
for line in f:
    data = json.loads(line) # load json entry
    if data["NAME"] in names:
        print('Duplicate: ' + str(data["NAME"]))
        duplicates += 1
    names.append(data["NAME"]) 
f.close() # close the file
print('Number of duplicates: ' + str(duplicates))


# How many rows have value -9999?
filtered = 0 
filtered_data = [] # store filtered rows
f = open('temp.json', 'r') # open the file to read
for line in f:
    if '-9999' in line:
        filtered += 1
    else: 
        filtered_data.append(line)    
f.close() # close the file
print('Number of filtered customers: ' + str(filtered))


# RFA_2F,  RFA_2A, and WEALTH_INDEX frequency
RFA_2F, RFA_2A, WEALTH_INDEX = Counter(), Counter(), Counter()  # we use counters
for line in filtered_data:
    data = json.loads(line) # load json entry
    RFA_2F[data['RFA_2F']] += 1
    RFA_2A[data['RFA_2A']] += 1
    WEALTH_INDEX[data['WEALTH_INDEX']] += 1
print('RFA_2F: '), 
print(RFA_2F) 


# What proportion of the targeted consumers responded?
TARGET_B = Counter()
for line in filtered_data:
    data = json.loads(line) # load json entry
    TARGET_B[data['TARGET_B']] += 1
print('Proportion of the targeted consumers that responded: '), 
print(100*float(TARGET_B['1'])/(TARGET_B['0']+TARGET_B['1'])),  
print('%')

#Is there a difference in the distribution of the WEALTH_INDEX for the responders from the non-responders?
WEALTH_INDEX_R, WEALTH_INDEX_NR = Counter(), Counter() # we use 2 counters
for line in filtered_data:
    data = json.loads(line) # load json entry
    if data['TARGET_B'] == '1':
        WEALTH_INDEX_R[data['WEALTH_INDEX']] += 1
    else: 
        WEALTH_INDEX_NR[data['WEALTH_INDEX']] += 1
print('Distribution of the WEALTH_INDEX for the responders: '), 
print(WEALTH_INDEX_R) 
print('Distribution of the WEALTH_INDEX for the non-responders: '), 
print(WEALTH_INDEX_NR)


# Plot the distributions of WEALTH_INDEX for the responders
print('We have done this many many times before! :)' )


#  Alphabetize the records by the NAME field
filtered_data_Dict = {}
for line in filtered_data:
    data = json.loads(line) # load json entry
    filtered_data_Dict[data['NAME']] = data

# sort and print results
print('1-10: ')
print([(key, filtered_data_Dict[key]) for key in sorted(filtered_data_Dict.keys())[0:10]])
print('20,000-20,010: ')
print([(key, filtered_data_Dict[key]) for key in sorted(filtered_data_Dict.keys())[19999:20010]])


# alphabetize by the individual's *last name*.
filtered_data_DictII = {}
for line in filtered_data:
    data = json.loads(line) # load json entry
    # extract last name
    last_name = data['NAME'].partition('.')[2].strip()
    if (last_name == ''):
        last_name = data['NAME'].partition(' ')[2].strip()
    last_name = last_name.partition(' ')[0]
    if (last_name in filtered_data_DictII.keys()): # xxx - fix this
        filtered_data_DictII[last_name + ' ' + data['NAME'].replace(last_name,'')] = data
    else:
        filtered_data_DictII[last_name] = data
# sort and print results
print('1-10: ')
print([(key, filtered_data_DictII[key]) for key in sorted(filtered_data_DictII.keys())[0:10]])
print('20,000-20,010: ')
print([(key, filtered_data_DictII[key]) for key in sorted(filtered_data_DictII.keys())[19999:20010]])


# Consider predicting response with the following quantity:
# -40 + 0.8*WEALTH_INDEX + 0.12*RFA_2F
predictions = {}
for name in filtered_data_Dict.keys():
    data = filtered_data_Dict[name]
    # predict value
    predictions[name] = -40 + 0.8*float(data['WEALTH_INDEX']) + 0.12*float(data['RFA_2F'])

# order dictionary in reverse order
orderedPredictions = OrderedDict(sorted(predictions.items(), key=lambda t: t[1], reverse=True))

# print results
print('1-10: ')
print([(key, orderedPredictions[key]) for key in orderedPredictions.keys()[0:10]])
    