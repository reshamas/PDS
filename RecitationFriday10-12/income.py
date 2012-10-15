###  This is the result of the PDS recitation on Friday 10/12/2012.

# In this recitation, as a class we wrote this code to compute the top
#  median income towns The point of this recitation was not that you
#  necessarily would have done this task in Python.  Maybe your Excel
#  skills would allow you to do it more efficiently.  However, we
#  talked about reasons why even *if* you could do it in Excel, you
#  might want to do it in Python.  For example, if you have to revisit
#  the analysis later, it is codified and you know *exactly* what was
#  done.  If you have to rerun later on data from a different time
#  period, you can make minimal changes to the script, and then just
#  push the button.

# Also, we saw two things when we went from zipcode to town name.
# First, pulling in the town names took almost no time, because we
# essentially already had the code for it.  Second, the only thing
# that kept it from being trivial was that there were some unexpected
# things in the data.  We see the power of having the analytics coded
# up, because we can just add an "if" statement or a regular
# expression, and deal with almost anything (and dealing with data,
# lots of "anythings" come up).

import re
import operator  # need this one for sorting
import sys 

income_filename = 'median_income.txt'

#we are going to read in the zips and the incomes; we discussed how if
#you wanted to store multiple things keyed by zip, you could have the
#value be the list of things.  Then you'd get the particular info
#items something like this: zip_info[zip][3] for the fourth piece of
#info.  We also discussed that in cases where the info was
#complicated, you might want to build a class and have the dictionary
#store class objects, like we did in the prior recitations.

zip_info = dict() # keyed by zip, value is income

# We settled on this form of reading as being the way we wanted to do it
with open(income_filename, 'r') as f:
    next(f) # these skip the first two header rows of the datafile
    next(f)
    for line in f:
        line = line.strip() # get rid of the newline
        #print line
        record=line.split('|') # turn the line into a list of fields

        #NOW ... we ran into some noise problems, which
        #turned out to be from the header rows, but before we put in
        #the nexts above, we used a regular expression to get rid of
        #"incomes" that were not all digits, after deciding to store
        #the income as an integer rather than a string.
        if (not re.search("\D",record[4])) and not record[4]=='':
            #Finally, the crucial part: save the income for each zip
            zip_info[record[1]] = int(record[4])  
        #print record[1], zip_info[record[1]]


#-------------------
# This is out of order in terms of the recitation, but in the right place in the script.

# After finding the highest income zips, we decided we wanted to know
# where they were.  Fortunately, I had a data file with zips and place
# names.  What a nice coincidence.
            
place_filename = 'zipcode.csv'

#Coding up the zip->placename lookup, it was extremely efficient we
#just copied the code from above and changed the names.  Note that
#here we wanted to take two fields (town and state) and turn them into
#the place name: Town, State.

place_info = dict() # keyed by zip, value is income
with open(place_filename, 'r') as f:
    next(f)
    for line in f:
        line = line.strip() # get rid of the newline
        line = re.sub("\"","",line) # this file had pesky "'s, and we
                                    # decided to use regex to get rid
                                    # of them
        #print line
        record=line.split(',')  # this file is comma separated
        #print record
        #        if (not re.search("\D",record[4])) and not record[4]=='':
        if record[0]:
            place_info[record[0]] = record[1]+", "+record[2]

#Now, we would like to have the zips sorted by income.  That means
# that we need to sort by the *values* of the dictionary.  Hey -- we
# did that before (see the starred question to the prior lab
# exercise).

# Here we just searched the web and found the following line in about 1 minute
# (note that this is a different way than in the sample script for the lab exercise)

#  note "key" here is the *sort key*, i.e., what the sort will be based on.
#   zip_info.get gets the values from the dictionary, and that's what we want to sort on.

sorted_zip_info = sorted(zip_info, key=zip_info.get, reverse=True)

#print sorted_zip_info[0]

#print "---------------------"

# Now, print out the places, sorted by median income, highest to lowest
#  We first just listed the top 10 or top 20, and sanity checked them
#  Then we printed them all out -- and redirected them to a file at the unix command line
#  In the resultant file, we can look up by town name or zip just using a text editor.
#  What are the highest income towns?  Where does your town stand?  

#for i in range(20):
for i in range(len(sorted_zip_info)):
    zip = sorted_zip_info[i]
    if place_info.has_key(zip):
        print i+1, zip, zip_info[zip], place_info[zip]
    else: # Ah ha!  We don't have names for some zips
        print i, zip, zip_info[zip], 'Nowhere, USA'

# Want to go further?  
# What are the "1%" in terms of median income?
# Try now to find the average median income by state.
# Plot a histogram of median incomes by location.
# Think up your own questions and answer them...
