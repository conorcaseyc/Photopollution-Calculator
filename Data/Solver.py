from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from scipy.stats import *

#The Data
x = array([21.5, 1205.4, 1351.3, 1636.4, 748.5, 1254, 1064, 1892, 3300, 1230.3, 658, 821.6, 1286.6, 1387.5, 1591.2, 1292, 1423.6, 1206.6, 1796.3, 768.5])
y = array([1, 21, 28, 38, 14, 34, 21, 50, 112, 25, 12, 14, 42, 28, 48, 24, 29, 20, 51, 12])
print x
print y

#Finding the formula to describe the correlation between population density and photopollution
p1 = polyfit(x,y,1)
print(p1)

#Find the correlation coefficient
slope,intercept,r_value,p_value,std_err = linregress(x,y)
correlation = (pow(r_value,2))
print correlation

#Calculate Standard Error
mean = 0
for i in y:
	mean += i
mean = mean / len(y)
deviation_array = []
for i in y:
	deviation = mean - i
	deviation_array.append(deviation)
sqaured_deviation = 0
for i in deviation_array:
	i = i ** 2
	sqaured_deviation += i
sqaured_deviation /= len(y) - 1
standard_deviation = sqaured_deviation ** 0.5
print standard_deviation		