'''
Created on Oct 6, 2012

@author: mkokkodi@stern.nyu.edu

Sample solution for HW1-part1.
'''

import csv
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np



possible_answers = """I dont even understand the question 
I have no experience working in a terminal
I have issued a few commands in a terminal based on given instructions 
I have written simple terminal commands or done some system work on the terminal 
I have written complex commands done or have done deep system work
I have never directly accessed a database
I have issued simple queries to a relational database based on given instructions 
I can write simple queries and issue them to a database
I can write very complex queries when needed
I am a database hacker
I have never programmed before. 
I have written simple programs, based on instructions or a tutorial 
I can write simple programs to accomplish tasks I encounter
I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms. 
I am a hacker or have  senior-level programming experience
"""


#Reading data

datapath = "/Users/mkokkodi/git/PDS/pds_data/"
surveyData = csv.reader(open(datapath+"survey_multiple_choice.tsv"), delimiter="\t")
nline = "--------------------------------------------------------"
print 'Survey results'
print nline
print "Answer | count"
print nline


possible_answers = possible_answers.splitlines()
i=0;
answer_values ={}
int2string ={}

#Here  I am assigning values of expertise to each answer.
#For example, the choice "I dont even understand the question"
# gets 0, while the choice "I have written complex commands done or have done deep system work"
#gets 4 .
for line in possible_answers:
    answer_values[line.strip()]=i%5
    int2string[i]=line.strip()
    i+=1
    
#Define a dictionary of counters. 
#Here I will aggregate the answers for each question (1,2,3) 
questions = defaultdict(Counter)

#Counting the answers to each question
for row in surveyData:
    if len(row) > 1:
        j=1;
        for answer in row:
            questions[j][answer.strip()] +=1
            #print  answer.strip(), questions[j][answer.strip()]
            j+=1
        
#This dictionary stores the count distribution for each question
#We will use it later for plotting.        
     
for k,v in questions.iteritems():
        #Sorting responses in increasing order.
        v =OrderedDict(sorted(v.items(), key=lambda t: t[0]))
        
        for k1,v1 in v.items():
            print k," | ",k1, "|", v1
        print nline

#Store data to use in later in plot.
data=defaultdict(list)
for j in range(0,15):
    data[j/5 + 1].append(questions[j/5 + 1][int2string[j]])
    




#I am computing the expertise for each question, by aggregating the products
#of the counts  with the values of each answer.
expertise_scores = Counter()    

for k,v in questions.iteritems():
        for k1,v1 in v.iteritems():
            expertise_scores[k] += answer_values[k1.strip()]*v1
            

print "Question | Aggregated Expertise"
for k,v in expertise_scores.iteritems():
    print k," | ",v
print nline    

fig = plt.figure()
ax = fig.add_subplot(111)
width=0.25
x=[1,2,3,4,5]
    
N = 5

ind = np.arange(N)  # the x locations for the groups
    
rects1 = ax.bar(ind,data[1], width, color='r')

rects2 = ax.bar(ind+width, data[2], width, color='g')

rects3 = ax.bar(ind+width+width, data[3], width, color='b')
# add some
ax.set_ylabel('Number of People')
ax.set_xlabel('Skill level')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1', '2', '3', '4', '5') )

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Unix', 'Database','Programming') )


plt.show();

