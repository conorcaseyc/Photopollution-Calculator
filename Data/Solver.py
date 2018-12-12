from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from scipy.stats import *

#The Data
population_density = array([21.5, 1205.4, 1351.3, 1636.4, 748.5, 1254, 1064, 1892, 3300, 1230.3, 658, 821.6, 1286.6, 1387.5, 1591.2, 1292, 1423.6, 1206.6, 1796.3, 768.5])
population = array ([557, 4979, 3593, 17140, 138, 1374, 946, 1346, 119320, 3765, 540, 3287, 25276, 9729, 94192, 1129, 6619, 23691, 14504, 2175])
lux = array([1, 21, 28, 38, 14, 34, 21, 50, 112, 25, 12, 14, 42, 28, 48, 24, 29, 20, 51, 12])
print population_density
print population
print lux

#Finds the formula to describe the correlation between population density and photopollution
p1 = polyfit(population_density,lux,1)
print(p1)

#Finds the correlation coefficient in the case of population density
slope,intercept,r_value,p_value,std_err = linregress(population_density,lux)
correlation = (pow(r_value,2))
print correlation
#Finds the correlation coefficient in the case of population
slope,intercept2,r_value2,p_value2,std_err2 = linregress(population,lux)
correlation2 = (pow(r_value2,2))
print correlation2

#Calculate Standard Deviation
mean = 0
for i in lux:
	mean += i
mean = mean / len(lux)
deviation_array = []
for i in lux:
	deviation = mean - i
	deviation_array.append(deviation)
sqaured_deviation = 0
for i in deviation_array:
	i = i ** 2
	sqaured_deviation += i
sqaured_deviation /= len(lux) - 1
standard_deviation = sqaured_deviation ** 0.5
print standard_deviation

#Plotting Graphs
#Mean LUX Values Scattering Plot
scatter(population_density,lux)
title("Mean LUX Values (All Sites)")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(population_density), poly1d(p1)(unique(population_density)))
text(0,100, "r = " + str(round(correlation, 3)))
show()
