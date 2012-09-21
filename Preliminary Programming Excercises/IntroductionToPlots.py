'''
Objectives:
1. Load data set into numpy ndarray
2. Plot histograms and scatter plots
3. Compute basic statistics
'''

import numpy as np
import matplotlib.pyplot as plt
import os

'''
Functions
'''
def plotHistogram(data, title='', xlabel='', ylabel=''):
    plt.hist(data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
    
def plotHistogramII(data1, data2, label1='', label2='', title='', xlabel='', ylabel=''):
    plt.hist(data1, label=label1)
    plt.hist(data2, color='r', alpha=0.5, label=label2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

def scatterPlot(data1, data2, title='', xlabel='', ylabel=''):
    plt.scatter(data1, data2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


'''
Script
'''
print('Please download the data set we are going to use in this hw: http://www.liaad.up.pt/~ltorgo/Regression/cal_housing.html')

# The path you stored the file
pathfile = "/Set/your/path/here/" 

# Load the data set
data = np.loadtxt(pathfile+'cal_housing.data', dtype=float, delimiter=',')

# Just to check that the file was loaded correctly 
print('This data set includes ' + str(data.shape[0]) + ' rows and ' + str(data.shape[1]) + ' columns!')
print('')

print('Now, let\'s plot a histogram!')
plotHistogram(data[:,7], title='Histogram of median income', xlabel='Value', ylabel='Frequency')
print('')

print('We can also plot two sets of values on the same axis with a histogram..')
plotHistogramII(data[:,2], data[:,7], label1='Median Age', label2='Media Income', title='Histogram of median income', xlabel='Value', ylabel='Frequency')
print('Documentation: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist')
print('')

print('Now, a scatter plot using just part of our data..')
scatterPlot(data[0:1000,7], data[0:1000,2], title='Scatter plot', xlabel='Median Income', ylabel='Median Age')
print('Documentation: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter')
print('')

print('For more examples, please visit http://matplotlib.org/gallery.html')
print('\n')

print('Finally, let\'s compute the mean value and the standard deviation of the median income.')
print('Mean: ' + str(np.mean(data[:,7])))
print('Std: ' + str(np.std(data[:,7])))
print('')

