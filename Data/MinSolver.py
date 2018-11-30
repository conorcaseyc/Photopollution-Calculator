from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from scipy.stats import *

#The Data
x = array([21.7, 1205.4, 1351.3, 1636.4, 748.5, 1254, 1064, 1892, 3300, 1230.3, 658, 821.6, 1286.6, 1387.5, 1591.2, 1292, 1423.6, 1206.6, 1796.3, 768.5])
y = array([0, 18, 23, 32, 11, 23, 16, 44, 98, 16, 7, 11, 32, 23, 44, 16, 23, 16, 44, 7])
print x
print y

#Finding the formula to describe the correlation between population density and photopollution
p1 = polyfit(x,y,1)
print(p1)

#Plot the graph
plot(x,y,'o'), 16, 44, 7

#Find the correlation coefficient
slope,intercept,r_value,p_value,std_err = linregress(x,y)
correlation = (pow(r_value,2))
print correlation
show()