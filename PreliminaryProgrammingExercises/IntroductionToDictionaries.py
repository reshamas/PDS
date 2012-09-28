'''
Objectives:
1. Create a dictionary
2. Print the dictionary you created in step #1, and its keys and values
3. Iterate through a dictionary
'''

# Create a dictionary
given = ['John', 'Eric', 'Terry', 'Michael'] # simple python list
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']

# How  to build a dictionary from two lists (or sequences): one list of keys, another list of values
# In this example keys:= given and corresponding values:= family
names = dict(zip(given, family))

# The next lines of code will help you understand even better the dictionary that we created
print('Dictionary: '), # Tip: You can also use 'print' to print on the same line
print(names) # print the entire dictionary
print('Dictionary keys: '), 
print(names.keys()) # just the dictionary keys
print('Dictionary values: '),
print(names.values()) # just the dictionary values
print('')

print('You can also write a simple loop..')
# iteritems(), iterkeys(), and itervalues() provide you with useful iterators over the dictionary’s (key, value) pairs, keys, and values, respectively.
for (given, family) in names.iteritems():
    print given, family # of course, we would get the result with print given, names[given]