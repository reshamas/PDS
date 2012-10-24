import sys

last = False
lastValue = 0

for line in sys.stdin:
    (key, value) = line.strip().split()
    value = int(value)
    if key != last:
        if last != False:
            print last + "\t" + str(lastValue)

        last = key
        lastValue = value


    else:
        lastValue = lastValue + value
if last!= False:
    print last + "\t" +str(lastValue)
