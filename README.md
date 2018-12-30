# Photopollution Calculator for Munster

Welcome to the Photopollution Calculator for Munster. This program is based on the mathematical model developed in the BT Young Scientist project called "Is It Possible to Create a Mathematical Model to Predict Photopollution Based on Population Density in Munster".

***Frequently Asked Questions:***

> How do I run this program?

To run this program you will need:

* Python (Preferably Python 2.7)
* Pandas
* Scipy
* Numpy
* Mathplotlib

All the necessary tools needed to run this program are available through [Anaconda](https://www.anaconda.com/download/).
Choose the operating system you are using, download the Python 2.7 version, and follow the Installation instructions available on their website.

To install and run this program, open a command line and type the following:

``` bash
$ git clone https://www.github.com/conorcaseyc/Photopollution-Calculator 
$ cd Photopollution-Calculator
$ python2 Program.py
```
If you are using Python 3, use the following command instead of the final command previously mentioned.

```bash
$ python3 Program_3.py
```

If you have any problems, please [email me.](mailto:16ccasey@student.kenmarecs.com).
> Where did the population density for the towns come from?

They came from the Irish 2016 Census, and as a result are provided by the Central Statistics Office.

> Why does the program crash when I enter a town name into the program?

This is most likely due to the fact that you entered a town that is not included in the Central Statistics Office database for population density. There is also a probability you typed "license", "quit", or "help" into the section where you are asked to input a town name. These options can only be accessed when you are prompted "Is the name of the town being entered:".
  
> How do I open the files in the Map Data folder

All these files can be opened using a program called, QGIS (previously known as Quantum GIS). QGIS is a free and open-source cross-platform desktop geographic information system (GIS) program that supports viewing, editing, and analysis of geospatial data. This program can be downloaded at the link below.

https://qgis.org/en/site/forusers/download.html

> Questions, or any other problems?

Any other questions, want to report a bug, or just general feedback, please email me at 16ccasey@student.kenmarecs.com  
