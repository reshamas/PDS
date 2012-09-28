'''
Objectives:
1. Load file
2. Load file to dictionary
3. Convert each answer to a numeric value and load file to dictionary
4. Convert a dictionary to numpy array
'''

# The csv module implements classes to read and write tabular data in CSV format.
# Keep in mind that there is no “CSV standard”!
# Documentation: http://docs.python.org/library/csv.html
import csv
# NumPy is an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays
import numpy as np

pathfile = "/Set/your/path/here/" # The path where you stored the file


def answerToNumeric(answer, listWithAnswersInAscOrder):
    # list.index(x) returns the index in the list of the first item whose value is x. It is an error if there is no such item.
    return listWithAnswersInAscOrder.index(answer)+1 # returns a numeric value (1-5; pay attention to the fact that we increased the result of the index function by 1) that corresponds to the answer that the student provided

def answersToNumeric(listWithAnswers, listsWithAnswersInAscOrder):
    listWithNumericAnswers = [] # a list which stores the numeric values for just one student
    for i in range(len(listWithAnswers)): # convert one answer at a time using the 'answerToNumeric' function that we previously defined 
        listWithNumericAnswers.append( answerToNumeric(listWithAnswers[i].strip(), listsWithAnswersInAscOrder[i]) ) # calls the 'answerToNumeric' function and add the result to the list
    return listWithNumericAnswers # returns the list with the numeric values that correspond to the answers of the specific user

# Simple python lists that store the alternative answers to each question
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
# You can iterate over the lines of the file 
# as we mentioned, there is no "CSV standard" and hence it's always useful to check that you have properly loaded the file
for row in tsv_file:
    print row
    
# 2. Load file to dictionary
tsv_file = csv.reader(open(pathfile+'survey_multiple_choice.tsv'), delimiter='\t')
answers = {} # we initialize our dictionary
student = 1 # we are going to use variable "student" as the key of our dictionary
for row in tsv_file:
    answers[student] = row 
    student += 1
print(answers)

# 3. Convert each answer to a numeric value and load file to dictionary
tsv_file = csv.reader(open(pathfile+'survey_multiple_choice.tsv'), delimiter='\t')
answers = {}
student = 1
for row in tsv_file:
    answers[student] = answersToNumeric(row, [question1, question2, question3]) # we call the function that we previously defined (once for each student)
    student += 1
print(answers)

# 4. Convert a dictionary to numpy array
# If you want to use some mathematical functions on your data, it's usually quite convenient to store them in numpy ndarray
myarray = np.empty((len(answers.keys()), 3), dtype=int) # we create an empty numpy ndarray. The dimensions (shape) of the ndarray are (#of students, #of answers). The data-type argument is optional but it's really important that you don't choose a wrong data type 
for student in range(len(answers.keys())):
    for question in range(3):
        myarray[student, question] = answers[student+1][question] 
print(myarray)
