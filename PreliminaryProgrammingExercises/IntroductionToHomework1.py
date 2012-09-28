'''
Objectives:
1. Load file
2. Load file to dictionary
3. Convert each answer to a numeric value and load file to dictionary
4. Convert a dictionary to numpy array
'''

import csv
import numpy as np

pathfile = "/Set/your/path/here/" # The path where you stored the file


def answerToNumeric(answer, listWithAnswersInAscOrder):
    return listWithAnswersInAscOrder.index(answer)+1

def answersToNumeric(listWithAnswers, listsWithAnswersInAscOrder):
    listWithNumericAnswers = []
    for i in range(len(listWithAnswers)):
        listWithNumericAnswers.append( answerToNumeric(listWithAnswers[i].strip(), listsWithAnswersInAscOrder[i]) )
    return listWithNumericAnswers

question1 = ['I dont even understand the question', 
            'I have no experience working in a terminal', 
            'I have issued a few commands in a terminal based on given instructions',  
            'I have written simple terminal commands or done some system work on the terminal', 
            'I have written complex commands done or have done deep system work'
            ]

question2 = ['I have never directly accessed a database',  
            'I have issued simple queries to a relational database based on given instructions', 
            'I can write simple queries and issue them to a database',  
            'I can write very complex queries when needed',  
            'I am a database hacker'
            ]

question3 = ['I have never programmed before.', 
            'I have written simple programs, based on instructions or a tutorial', 
            'I can write simple programs to accomplish tasks I encounter',  
            'I can write complex programs, am familiar with programming design patterns, software testing, system design, and algorithms.', 
            'I am a hacker or have  senior-level programming experience'
            ]

# 1. Load file
tsv_file = csv.reader(open(pathfile+'survey_multiple_choice.tsv'), delimiter='\t')
for row in tsv_file:
    print row
    
# 2. Load file to dictionary
tsv_file = csv.reader(open(pathfile+'survey_multiple_choice.tsv'), delimiter='\t')
answers = {}
student = 1
for row in tsv_file:
    answers[student] = row 
    student += 1
print(answers)

# 3. Convert each answer to a numeric value and load file to dictionary
tsv_file = csv.reader(open(pathfile+'survey_multiple_choice.tsv'), delimiter='\t')
answers = {}
student = 1
for row in tsv_file:
    answers[student] = answersToNumeric(row, [question1, question2, question3])
    student += 1
print(answers)

# 4. Convert a dictionary to numpy array
myarray = np.empty((len(answers.keys()), 3), dtype=int)
for student in range(len(answers.keys())):
    for question in range(3):
        myarray[student, question] = answers[student+1][question] 
print(myarray)
