#Question 1 import Numpy and print the version number
import numpy as np
print(np.__version__)


#Question 2  Create a 1D array of numbers from 0 to 9
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)
print(arr.ndim)  #to show only 1D

#Question 3 Import dataset with numbers and texts keeping the text intact in python numpy
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter= ',', dtype= None, encoding= 'utf-8')
print(data.shape)
print(data[:5])  #first 5 rows

#question 4 Find the position of the first occurrence of a value greater than 1.0 in petal width 4th column of iris database
data = np.genfromtxt(url, delimiter=',', usecols=(0,1,2,3))    #filters only rows with petal width > 1.0 and returns the index from the result
petal_width = data[:, 3]
position = np.where(petal_width > 1.0)[0][0]
print('The position of the first occurrence where petal width > 1.0 is:', position)

#Question 5 from array a replace all values greater than 30 to 30 and less than 10 to 10
np.random.seed(100)
a = np.random.uniform(1,50,20)

a[a > 30] = 30
a[a < 10] = 10

print(a)

