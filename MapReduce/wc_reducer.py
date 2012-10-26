import sys

last = False #where we store the last key seen. False is a flag when the reducer hasnt seen any data yet
lastValue = 0 #where we store the accumulated value

#The reducer consumes input one line at a time
for line in sys.stdin:
    #The key value input to the reducer are just separated by a tab, split them up
    (key, value) = line.strip().split()
    #value is an int, a count
    value = int(value)
    #if the current key is different than the last key...
    if key != last:
        #if the last key isnt False (eg, this isnt the first line we've observed)
        if last != False:
            #print the count
            print last + "\t" + str(lastValue)
            last = False
        #then set the "accumulating key" to the new key, and reset the accumulating value
        last = key
        lastValue = value


    else:
        #we've seen this key before, just add to the value
        lastValue = lastValue + value
if last!= False:
    #print the last line
    print last + "\t" +str(lastValue)
