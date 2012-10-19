# The next module implements specialized container datatypes providing alternatives to 
# Python's general purpose built-in containers, dict, list, set, and tuple.
from collections import defaultdict
# A Counter is a dict subclass for counting hashable objects
from collections import Counter
# The csv module implements classes to read and write tabular data in CSV format.
# Keep in mind that there is no "CSV standard"!
# Documentation: http://docs.python.org/library/csv.html
import csv
# The os module provides a portable way of using operating system dependent functionality.
import os
# The RE module provides regular expression matching operations
import re
# matplotlib is a plotting library for the Python programming language 
import matplotlib.pyplot as plt


'''
Main Script
'''
# Download the file student_skills_with_majors.tsv
#os.system('curl -O http://people.stern.nyu.edu/ja1517/data/student_skills_with_majors.tsv')


print('1st Question')
'''
The school / major column (field one) requested freeform text as a response. However, 
because there are only a finite number of majors, 
answers should probably have been categorical, a multiple choice response. 
Your job is to "canonicalize" the values in this column- map them to a smaller set 
of true values. For instance, "Stern MBA" and "MBA" should probably be the 
treated the same way. What are the resulting canonical majors? How many students in 
the class belong to each major?
'''
# "canonicalize" the values
def matchMajors(major):
    for word in re.split(r'[,/ ]', major.lower()): # convert major to lowercase and split it using 3 delimiters
        if word in ['mba', 'stern', 'langome']:
            return 'MBA'
        elif word in ['msis', 'information', 'systems', 'courant']:
            return 'MSIS'
    return 'Other' # else case
  

majors = Counter({'MBA': 0, 'MSIS': 0, 'Other':0}) # create a counter
tsv_file = csv.reader(open('student_skills_with_majors.tsv'), delimiter='\t')
for row in tsv_file:
    #print row
    majors[matchMajors(row[0])] += 1
print(majors)


print('\n2nd Question')
'''
Which major, in your estimation, has the lowest and highest skill levels?
'''
print('\tJust for the 6th question (i.e. programming experience).')

possibleAnswers = ['I have never programmed before.', 
            'I have written simple programs  based on instructions or a tutorial', 
            'I can write simple programs to accomplish tasks I encounter',  
            'I can write complex programs  am familiar with programming design patterns  software testing  system design  and algorithms.', 
            'I am a hacker or have  senior-level programming experience'
            ]

def answerToNumeric(answer, listWithAnswersInAscOrder):
    # list.index(x) returns the index in the list of the first item whose value is x. It is an error if there is no such item.
    return listWithAnswersInAscOrder.index(answer)+1 # returns a numeric value (1-5; pay attention to the fact that we increased the result of the index function by 1) that corresponds to the answer that the student provided

programmingSkills = defaultdict(list)
tsv_file = csv.reader(open('student_skills_with_majors.tsv'), delimiter='\t')
for row in tsv_file:
    major = matchMajors(row[0])
    answer = answerToNumeric(row[5], possibleAnswers)
    programmingSkills[major].append(answer)
    
# compute average skill
averageSkill = {}
for major in programmingSkills.keys():
    averageSkill[major] = sum(programmingSkills[major])/float(len(programmingSkills[major]))
print(averageSkill)


print('\n3rd Question')
'''
How do the computer skills of the different majors differ? For any major with at least 
three students enrolled in the class, use matplotlib to make a plot of the distribution 
of skill levels, starting from the lowest and going to the highest for each of the three 
disciplines. You may wish to substitute the strings describing the skill level with a 
numeric value.
'''

# We create a method to plot two sets of values on a histogram     
def plot(data, label='', title='', xlabel='', ylabel=''): # title, xlabel, and ylabel are optional parameters with default values set to ''
    plt.bar([1, 2, 3, 4, 5], data, 0.9, label=label) # plot a histogram
    plt.xlabel(xlabel) # set the x axis label 
    plt.ylabel(ylabel) # set the y axis label 
    plt.title(title) # set the title of the plot
    plt.xticks( [1.45, 2.45, 3.45, 4.45, 5.45], ('1', '2', '3', '4', '5') )
    plt.grid(True) # turn the axes grids on or off
    plt.legend() # place a legend on the current axes
    plt.show() # display a figure
    

print('\tAgain, just for the 6th question (i.e. programming experience).')
for major in programmingSkills.keys():
    c = Counter()
    for answer in programmingSkills[major]:
        c[answer] += 1
    data = [c[1], c[2], c[3], c[4], c[5]]
    plot(data, label=major, title='Distribution of skill levels', xlabel='Level', ylabel='Frequency')