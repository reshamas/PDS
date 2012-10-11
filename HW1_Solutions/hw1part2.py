'''
Created on Oct 6, 2012

@author: mkokkodi@stern.nyu.edu

Sample solution for income predictions.
'''
import csv
from collections import Counter

datapath = "/Users/mkokkodi/git/PDS/pds_data/"

#removing NA lines
def q3(): 
    data = open(datapath+"marketing.data",'r')

    f = open(datapath+"cleanMarketing.data",'w')
    for line in data:
        if not "NA" in line:
            s =  str(line)
            f.write(s)
        
    f.closed
    
#Most common education level.    
def q4(data):
    print("------------------------------------------") 
    print("        Question 4                       ")
    print("------------------------------------------") 
    
    cnt = Counter()
    for line in data:
        cnt[int(line[4])] +=1
    print "Most common education level:",cnt.most_common(1)
     
#distribution of income for 
#households with education level equals to 6.    
def q5(data):
    print("------------------------------------------") 
    print("        Question 5                        ")
    print("------------------------------------------") 
    print("Income | Frequency")
    cnt = Counter()
    for line in data:

        if(int(line[4]) == 6):
            cnt[int(line[0])]+=1
    for k,v in cnt.iteritems():
        print k,"     |     ",v
   
#predicting income based on education    
def q6(data,edu):
    print("------------------------------------------") 
    print("        Question 6                        ")
    print("------------------------------------------") 
    
       
    diff = 0
    totalInstances = 0
    for line in data:
        y = 4 + edu[int(line[4])]
        diff = diff + (abs(y - int(line[0]))) 
        totalInstances = totalInstances+1
    print("Total difference:"+str(diff))
    print("Avg difference Per Person:"+str(float(diff)/float(totalInstances)))


#predicting income based on education and occupations
def q7a(data,edu,occupation):
    print("------------------------------------------") 
    print("        Question 7                        ")
    print("------------------------------------------") 
    
    diff = 0
    totalInstances = 0
    overestimates = 0;
    underestimates = 0
    signedDiff = 0
    for line in data:
        y = 4 + edu[int(line[4])]+occupation[int(line[5])]
        curDiff = y - int(line[0])
        diff = diff + (abs(curDiff)) 
        totalInstances = totalInstances+1
        
        y = 4 + edu[int(line[4])]+occupation[int(line[5])]
        #One way to see whether the model overestimates 
        
        if(curDiff > 0):
            overestimates += 1
        else:
            underestimates+=1 
        #Another way is to take the signed differences instead of 
        #absolute differences  If signedDiff is greater than zero
        #-> it overestimates
        signedDiff += curDiff
    print("total difference:"+str(diff))
    print("Avg difference Per Person:"+str(float(diff)/float(totalInstances)))
    print("The model overestimates:"+str(overestimates)+" times.")
    print("The model underestimates:"+str(underestimates)+" times.")
    print("Signed Difference:"+str(signedDiff))
    print("Most likely our model overestimates.")

   
edu={}
edu[1]=-3
edu[2]=-1
edu[3] = 0
edu[4] = 1
edu[5] = 3
edu[6] = 4

occupation={}
occupation[1] = 2.5
occupation[2] = 0.6
occupation[3] = 0 
occupation[4] = 0.2
occupation[5] = -0.5
occupation[6] = -1.5
occupation[7] = 0.3
occupation[8] = 0.8
occupation[9] = -2.5

cleandata = csv.reader(open(datapath+"cleanMarketing.data"), delimiter=' ')
q4(cleandata)

cleandata = csv.reader(open(datapath+"cleanMarketing.data"), delimiter=' ')
q5(cleandata)
cleandata = csv.reader(open(datapath+"cleanMarketing.data"), delimiter=' ')
q6(cleandata,edu)
cleandata = csv.reader(open(datapath+"cleanMarketing.data"), delimiter=' ')
q7a(cleandata,edu,occupation)
