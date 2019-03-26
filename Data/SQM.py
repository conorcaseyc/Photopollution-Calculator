from numpy import *
from scipy.interpolate import *
from matplotlib.pyplot import *
from scipy.stats import *

#The Data
population_density = array([1901, 1292, 1423.6, 1069.2, 731.9, 2163.9, 1467.7, 327.6, 768.5, 2.4])
population = array ([94192, 1129, 6619, 2023, 2486, 23691, 14504, 172, 2376, 146])
sqm = array([16.15, 17.17, 16.88, 17.44, 19.11, 15.87, 16.89, 19.79, 18.57, 21.35])
print(population_density)
print(population)
print(sqm)

#Finds the formula to describe the correlation between population density and photopollution
p1 = polyfit(population_density,sqm,1)
print(p1)
#Finds the correlation coefficient in the case of population density
slope,intercept,r_value,p_value,std_err = linregress(population_density,sqm)
correlation = (pow(r_value,2))
print(correlation)
#Finds the formula to describe the correlation between population and photopollution (Normalization of Walker's Law.)
p2 = polyfit(population,sqm,1)
print(p2)
#Finds the correlation coefficient in the case of population
slope,intercept2,r_value2,p_value2,std_err2 = linregress(population,sqm)
correlation2 = (pow(r_value2,2))
print (correlation2)
#Calculate Standard Deviation
stddev = std(sqm)
print(stddev)