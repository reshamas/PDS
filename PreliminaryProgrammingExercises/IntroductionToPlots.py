'''
Objectives:
1. Load data set into numpy ndarray
2. Plot histograms and scatter plots
3. Compute basic statistics
'''

# NumPy is an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays
import numpy as np
# matplotlib is a plotting library for the Python programming language 
import matplotlib.pyplot as plt


'''
Functions
'''
# We create a method to plot a histogram
def plotHistogram(data, title='', xlabel='', ylabel=''): # title, xlabel, and ylabel are optional parameters with default values set to ''
    plt.hist(data) # plot a histogram
    plt.xlabel(xlabel) # set the x axis label 
    plt.ylabel(ylabel) # set the y axis label 
    plt.title(title) # set the title of the plot
    plt.grid(True) # turn the axes grids on or off
    plt.show() # display a figure

# We create a method to plot two sets of values on a histogram     
def plotHistogramII(data1, data2, label1='', label2='', title='', xlabel='', ylabel=''): # title, xlabel, and ylabel are optional parameters with default values set to ''
    plt.hist(data1, label=label1) # plot a histogram
    plt.hist(data2, color='r', alpha=0.5, label=label2) # plot another histogram 
    plt.xlabel(xlabel) # set the x axis label 
    plt.ylabel(ylabel) # set the y axis label 
    plt.title(title) # set the title of the plot
    plt.grid(True) # turn the axes grids on or off
    plt.legend() # place a legend on the current axes
    plt.show() # display a figure

# We create a method to make a scatter plot
def scatterPlot(data1, data2, title='', xlabel='', ylabel=''): # title, xlabel, and ylabel are optional parameters with default values set to ''
    plt.scatter(data1, data2) # make a scatter plot
    plt.xlabel(xlabel) # set the x axis label 
    plt.ylabel(ylabel) # set the y axis label 
    plt.title(title) # set the title of the plot
    plt.show() # display a figure


'''
Script
'''
print('Please download the data set we are going to use in this hw: http://www.liaad.up.pt/~ltorgo/Regression/cal_housing.html')

# The path you stored the file
pathfile = "/Set/your/path/here/" 

# Load the data set to a numpy array
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
data = np.loadtxt(pathfile+'cal_housing.data', dtype=float, delimiter=',')

# Just to check that the file was loaded correctly 
# ndarray.shape returns a tuple of array dimensions
print('This data set includes ' + str(data.shape[0]) + ' rows and ' + str(data.shape[1]) + ' columns!')
print('')

print('Now, let\'s plot a histogram!')
# We can refer to the 8th column of the ndarray that we previously created using numpy basic slicing: data[:,7]
# Also, we can set the desired values for the title, xlabel, and ylabel parameters for the specific plot   
plotHistogram(data[:,7], title='Histogram of median income', xlabel='Value', ylabel='Frequency')
print('')

print('We can also plot two sets of values on the same axis with a histogram..')
plotHistogramII(data[:,2], data[:,7], label1='Median Age', label2='Media Income', title='Histogram of median income', xlabel='Value', ylabel='Frequency')
print('Documentation: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist')
print('')

print('Now, a scatter plot using just part of our data..')
# Respectively, We can refer to the first 1000 rows of the 8th column of the ndarray: data[0:1000,7]  
scatterPlot(data[0:1000,7], data[0:1000,2], title='Scatter plot', xlabel='Median Income', ylabel='Median Age')
print('Documentation: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter')
print('')

print('For more examples, please visit http://matplotlib.org/gallery.html')
print('\n')
print('For a summary of the matplotlib commands, please visit http://matplotlib.org/api/pyplot_summary.html')
print('\n')


print('Finally, let\'s compute the mean value and the standard deviation of the median income.')
# http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-methods
print('Mean: ' + str(np.mean(data[:,7]))) # Returns the average of the array elements; here the average of the 8th column
print('Std: ' + str(np.std(data[:,7]))) # Returns the standard deviation; here the standard deviation of the 8th column
print('')

