"""
Objectives: 
    Download a web page.
    Use of regular expressions to parse Strings
    
Please read first about regular expressions here:
    http://docs.python.org/library/re.html
Author mkokkodi@stern.nyu.edu 
   
"""



# The RE module provides regular expression matching operations
import re
# This module provides a high-level interface for fetching data across the World Wide Web
try: import urllib.request as urllib2 #python 3.X
except ImportError: import urllib2

# Get the web page 
def getPage(url):
    request = urllib2.urlopen(url) # open url
    response = str(request.read()) # read web page
    return response


# Extract rows with "<li>" in. 
def getBullets(response):
    bullets = []
    left = '''<li>'''
    right = '''</li>'''
    pattern = left + '''.*?''' + right # build pattern 
    rows = response.split("\n")
    for i in  range(0,len(rows)):
        match = re.search(pattern, rows[i], re.DOTALL) # r.e.
        if match:
            response = match.group()
            response = response.replace(left, '')
            response = response.replace(right, '')
            bullets.append(response)
            
    return bullets




url = "http://people.stern.nyu.edu/mk3539/pytutorial.html"
#page = getPage(url)
#bull = getBullets(page)
#for row in bull:
#    print row

    
#Other regular expressions examples:
#Extract emails from text:
lines = ['This guys email is somene@gmail.com','One more email somone2@stern.nyu.edu']
#you can read this pattern as follows:
# at least one alphanumeric character followd by '@' followed by at list one of (at least 
#one alphanumeric character and maybe a dot).  
pattern = '\w+@(\w+\.?)+'
for line in lines:
    match = re.search(pattern,line)
    print match.group(0)
