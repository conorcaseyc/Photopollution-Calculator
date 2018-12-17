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

#Rest of Graphs
max_lux = array([1, 23, 32, 44, 16, 44, 23, 55, 125, 34, 16, 16, 52, 32, 52, 32, 34, 23, 58, 16])
min_lux = array([0, 18, 23, 32, 11, 23, 16, 44, 98, 16, 7, 11, 32, 23, 44, 16, 23, 16, 44, 7])
firsttrip_pd = array([21.5, 1205.4, 1351.3, 1636.4, 748.5, 1254, 1064, 1892, 3300, 1230.3])
secondtrip_pd = array ([658, 821.6, 1286.6, 1387.5, 1591.2, 1292, 1423.6, 1206.6, 1796.3, 768.5])
firsttrip_pp = array([1, 21, 28, 38, 14, 34, 21, 50, 112, 25])
secondtrip_pp = array([12, 14, 42, 28, 48, 24, 29, 20, 51, 12])
kerry_pd = array([21.5, 658, 1206.6, 1796.3, 768.5])
kerry_pp = array([1, 12, 20, 51, 12])
tipp_pd = array([1205.4, 1351.3, 1636.4])
tipp_pp = array([21, 28, 38])
water_pd = array([748.5, 1254, 1064])
water_pp = array([14, 34, 21])
cork_pd = array([1892, 3300, 1230.3])
cork_pp = array([50, 112, 25])
clare_pd = array([821.6, 1286.6, 1387.5])
clare_pp = array([14, 42, 28])
lim_pd = array([1591.2, 1292, 1423.6])
lim_pp = array([48, 24, 29])

#p(n)
p2 = polyfit(population_density,max_lux,1)
p3 = polyfit(population_density,min_lux,1)
p4 = polyfit(firsttrip_pd,firsttrip_pp,1)
p5 = polyfit(secondtrip_pd,secondtrip_pp,1)
p6 = polyfit(kerry_pd,kerry_pp,1)
p7 = polyfit(tipp_pd,tipp_pp,1)
p8 = polyfit(water_pd,water_pp,1)
p9 = polyfit(cork_pd,cork_pp,1)
p10 = polyfit(clare_pd,clare_pp,1)
p11 = polyfit(lim_pd,lim_pp,1)

#Max LUX Graph
slope,intercept,r_value,p_value,std_err = linregress(population_density,max_lux)
correlation = (pow(r_value,2))
scatter(population_density,max_lux)
title("Max LUX Values (All Sites)")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(population_density), poly1d(p2)(unique(population_density)))
text(0,120, "r = " + str(round(correlation, 3)))
show()

#Min LUX Graph
slope,intercept,r_value,p_value,std_err = linregress(population_density,min_lux)
correlation = (pow(r_value,2))
scatter(population_density,min_lux)
title("Minimum LUX Values (All Sites)")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(population_density), poly1d(p3)(unique(population_density)))
text(0,95, "r = " + str(round(correlation, 3)))
show()

#Mean LUX Graph (First Trip)
slope,intercept,r_value,p_value,std_err = linregress(firsttrip_pd,firsttrip_pp)
correlation = (pow(r_value,2))
scatter(firsttrip_pd,firsttrip_pp)
title("Mean LUX Values (First Trip)")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(firsttrip_pd), poly1d(p4)(unique(firsttrip_pd)))
text(0,100, "r = " + str(round(correlation, 3)))
show()

#Mean LUX Graph (Second Trip)
slope,intercept,r_value,p_value,std_err = linregress(secondtrip_pd,secondtrip_pp)
correlation = (pow(r_value,2))
scatter(secondtrip_pd,secondtrip_pp)
title("Mean LUX Values (Second Trip)")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(secondtrip_pd), poly1d(p5)(unique(secondtrip_pd)))
text(620,50, "r = " + str(round(correlation, 3)))
show()

#Kerry Graph
slope,intercept,r_value,p_value,std_err = linregress(kerry_pd,kerry_pp)
correlation = (pow(r_value,2))
scatter(kerry_pd,kerry_pp)
title("Kerry Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(kerry_pd), poly1d(p6)(unique(kerry_pd)))
text(0,50, "r = " + str(round(correlation, 3)))
show()
#Tipperary Graph
slope,intercept,r_value,p_value,std_err = linregress(tipp_pd,tipp_pp)
correlation = (pow(r_value,2))
scatter(tipp_pd,tipp_pp)
title("Tipperary Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(tipp_pd), poly1d(p7)(unique(tipp_pd)))
text(1200,37.5, "r = " + str(round(correlation, 3)))
show()
#Waterford Graph
slope,intercept,r_value,p_value,std_err = linregress(water_pd,water_pp)
correlation = (pow(r_value,2))
scatter(water_pd,water_pp)
title("Waterford Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(water_pd), poly1d(p8)(unique(water_pd)))
text(725,34, "r = " + str(round(correlation, 3)))
show()
#Cork Graph
slope,intercept,r_value,p_value,std_err = linregress(cork_pd,cork_pp)
correlation = (pow(r_value,2))
scatter(cork_pd,cork_pp)
title("Cork Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(cork_pd), poly1d(p9)(unique(cork_pd)))
text(1200,100, "r = " + str(round(correlation, 3)))
show()
#Clare Graph
slope,intercept,r_value,p_value,std_err = linregress(clare_pd,clare_pp)
correlation = (pow(r_value,2))
scatter(clare_pd,clare_pp)
title("Clare Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(clare_pd), poly1d(p10)(unique(clare_pd)))
text(800,40, "r = " + str(round(correlation, 3)))
show()
#Limerick Graph
slope,intercept,r_value,p_value,std_err = linregress(lim_pd,lim_pp)
correlation = (pow(r_value,2))
scatter(lim_pd,lim_pp)
title("Limerick Mean LUX Values")
xlabel("Population Density (people per km^2)")
ylabel("LUX Values")
plot(unique(lim_pd), poly1d(p5)(unique(lim_pd)))
text(1300,45, "r = " + str(round(correlation, 3)))
show()