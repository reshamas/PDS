'''
Objectives:
1. Create a dictionary
2. Print the dictionary you created in step #1, and its keys and values
3. Iterate through a dictionary
'''

# Create a dictionary
given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']

# How  to build a dictionary from two lists (or sequences): one list of keys, another list of values
names = dict(zip(given, family))

print('Dictionary: '), # You can also print on the same line
print(names)
print('Dictionary keys: '), 
print(names.keys())
print('Dictionary values: '),
print(names.values())
print('')

print('You can also write a simple loop..')
for (given, family) in names.iteritems():
    print given, family