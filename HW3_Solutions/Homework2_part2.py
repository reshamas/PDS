# The RE module provides regular expression matching operations
import re
# This module provides a high-level interface for fetching data across the World Wide Web
try: import urllib.request as urllib2 #python 3.X
except ImportError: import urllib2

'''
Functions
'''
# Get the web page 
def getPage(url):
    request = urllib2.urlopen(url) # open url
    response = str(request.read()) # read web page
    return response

    
# Extract all the emails from the webpage
def getIDs(response):
    IDs = []
    left = '''@stern.nyu.edu>'''
    right = '''</a>&nbsp;</TD>'''
    pattern = left + '''.*?''' + right # build pattern 
    rows = response.split("\n")
    for row in rows:
        match = re.search(pattern, row, re.DOTALL) # r.e.
        if match:
            response = match.group()
            response = response.replace(left, '')
            response = response.replace(right, '')
            IDs.append(response)       
    return IDs


# Extract all the students' names with four letters in their last names or less
def getNames(response):
    names = []
    left = '''PRACTICAL DATA SCIENCE'>'''
    right = ''','''
    pattern = left + '''[A-z]{1,4}''' + right
    rows = response.split("\n")
    for row in rows:
        match = re.search(pattern, row, re.DOTALL)
        if match:
            response = match.group()
            response = response.replace(left,'')
            response = response.replace(right,'')
            names.append(response)
    return names


'''
Main Script
'''
print('1st Question')
# 1. Within the document, there are several student IDs (the column actually 
# is titled E-mail). Extract these IDs from the html and print them to a file, 
# one per line.
url = 'http://people.stern.nyu.edu/ja1517/data/pds_2012_roster.html'
response = getPage(url) # read webpage
IDs = getIDs(response) # extract ids
f = open('studentsIds.txt', 'w') # open the file to write
for studentId in IDs:
    f.write(studentId+'\n') # write to file
f.close() # close file
print('We extracted the IDs from the html and print them to a file.\n')


print('2nd Question')
# 2. Constrain your search to print only those students with four letters in 
# their last names or less. 
url = 'http://people.stern.nyu.edu/ja1517/data/pds_2012_roster.html'
response = getPage(url) # read webpage
names = getNames(response) # extract matching names
for student in names:
    print(student)
print('We just printed only those students with four letters in their last names or less.\n')
    


print('3rd Question')
# 3. For every student in the class, in addition to extracting their student ID, 
# extract their name. Present the results by printing out, one student per line:
#                first (and middle) name [tab] last name [tab] student id

def parsePage(response):
    rows = []
    left = '''E-mail</B></FONT></TD>'''
    right = '''</TABLE></table>'''
    pattern = left + '''.*?''' + right # build pattern 
    match = re.search(pattern, response, re.DOTALL) # r.e.
    if match:
        response = match.group()
        response = response.replace(left, '')
        response = response.replace(right, '')
        rows = response.split('<TD align=center><c><img')
    return rows[1: len(rows)] 

# Extract email from row
def parseId(response):
    studentId = ''
    left = '''@stern.nyu.edu>'''
    right = '''</a>'''
    pattern = left + '''.*?''' + right # build pattern 
    match = re.search(pattern, response, re.DOTALL) # r.e.
    if match:
        response = match.group()
        response = response.replace(left, '')
        response = response.replace(right, '')
        studentId = response
    return studentId

# Extract name from row
def parseNames(response):
    firstname, lastname = '', ''
    left = '''PRACTICAL DATA SCIENCE'>'''
    right = '''</a>'''
    pattern = left + '''.*?''' + right # build pattern 
    # we could have answered this question using a different pattern  
    # e.g. pattern = left + '''([A-z\.]*[ ]?[A-z\.]*), ([A-z]*[ ]*[A-z\.\-]*)''' + right
    match = re.search(pattern, response, re.DOTALL) # r.e.
    if match:
        response = match.group()
        response = response.replace(left, '')
        response = response.replace(right, '')
        name = response.split(',')
        firstname = name[1]
        lastname = name[0]
    return firstname, lastname

url = 'http://people.stern.nyu.edu/ja1517/data/pds_2012_roster.html'
students = {} # The keys of this dictionary will be used in answering question 4. 
response = getPage(url)
table = parsePage(response)
for student in table:
    firstname, lastname = parseNames(student)
    studentId = parseId(student)
    students[studentId] = lastname + ', ' + firstname
    print(firstname + '\t' + lastname + '\t' + studentId)
print('We just finished part 3!\n')


print('4th Question')
# 4. The E-mail column seems misnamed. Create a new html document that replaces 
# all student ids in this field with student email addresses.
url = 'http://people.stern.nyu.edu/ja1517/data/pds_2012_roster.html'
response = getPage(url)
for studentId in students.keys():
    response = response.replace(studentId+'<', studentId+'@stern.nyu.edu<') # replace ids with emails
f = open('pds_2012_roster.html', 'w') # open the file to read
f.write(response) # write to file
f.close() # close file
print('We created a new html document that replaces all student ids in this field with student email addresses.')