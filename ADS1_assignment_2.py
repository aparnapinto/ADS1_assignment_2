# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:20:14 2022

@author: manuv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read(file):
    df = pd.read_csv(file)
    df_transpose = df.transpose()
    return df, df_transpose


def bar_graph_1():
    
    """This function is for plotting the bar graph"""
   
    plt.figure()
    ax = plt.subplot(1, 1, 1)
    pop, pop_transpose = read('Population_total.csv')
    
    x = np.arange(len(pop.index))  
    w = 0.1
    
    plt.bar(x, pop['1995'].values, width=w, label='1995')
    plt.bar(x+w, pop['2000'].values, width=w, label='2000')
    plt.bar(x+w*2, pop['2005'].values, width=w, label='2005')
    plt.bar(x+w*3, pop['2010'].values, width=w, label='2010')
    plt.bar(x+w*4, pop['2015'].values, width=w, label='2015')
    ax.set_xlabel("Country Name")
    ax.set_ylabel("Population")
    ax.set_title("Total Population")
    ax.set_xticks(x)
    ax.set_xticklabels(pop["Country Name"])
    ax.legend(loc='upper left')
    ax.figure.savefig("population.png", bbox_inches = "tight")
    ax.figure.show()


def bar_graph_2():
    
    """This function is for plotting the bar graph"""

    plt.figure()
    ax = plt.subplot(1, 1, 1)
    co2, co2_transpose = read('CO2_emissions_from_solid_fuel_consumption_(kt).csv')
    
    x = np.arange(len(co2.index))  
    w = 0.1

    plt.bar(x, co2['1995'].values, width=w, label='1995')
    plt.bar(x+w, co2['2000'].values, width=w, label='2000')
    plt.bar(x+w*2, co2['2005'].values, width=w, label='2005')
    plt.bar(x+w*3, co2['2010'].values, width=w, label='2010')
    plt.bar(x+w*4, co2['2015'].values, width=w, label='2015')
    ax.set_xlabel("Country Name")
    ax.set_ylabel("CO2 emission")
    ax.set_title("CO2 Emissions from Solid Fuel Consumption(kt)")
    ax.set_xticks(x)
    ax.set_xticklabels(co2["Country Name"])
    ax.legend(loc='upper left')
    ax.figure.savefig("fuel_consumption.png", bbox_inches = "tight")
    ax.figure.show()

 
def line_graph_1():
   
    """This function is for plotting a line graph using iteration"""
   
    coal, coal_transpose = read("Electricity_production_from_coal_sources(% of total).csv")
   
    plt.figure()
    lab1 = ["1998","2002","2006","2010","2014"]
    for i in range(len(lab1)):
        plt.plot(coal['Country Name'], coal[lab1[i]],label = lab1[i])
    plt.xlabel("Country Name")
    plt.ylabel("Electricity production(in %)")
    plt.title("Electricity Production from Coal Sources (% of total)")
    plt.xticks(rotation = 90)
    plt.legend()
    plt.savefig("electricity_production.png", bbox_inches = "tight")
    plt.show()


def line_graph_2():
    
    """This function is for plotting a line graph using iteration"""

    power, power_transpose = read("Electric_power_consumption(kWh per capita).csv")
    
    plt.figure()
    lab2=["1998","2002","2006","2010","2014"]
    for i in range(len(lab2)):
        plt.plot(power['Country Name'],power[lab2[i]],label = lab2[i])
    plt.xlabel("Country Name")
    plt.ylabel("Electric power consumption")
    plt.title("Electric Power Consumption (kWh per capita)")
    plt.xticks(rotation = 90)
    plt.legend()
    plt.savefig("power_consumption.png", bbox_inches = "tight")
    plt.show()

#Reading the csv file to get a return of dataframes
pop, pop_transpose = read("Population_total.csv")
co2, co2_transpose = read("CO2_emissions_from_solid_fuel_consumption_(kt).csv")
coal, coal_transpose = read("Electricity_production_from_coal_sources(% of total).csv")
power, power_transpose = read("Electric_power_consumption(kWh per capita).csv")
   
#calling the functions
bar_graph_1()
bar_graph_2()
line_graph_1()
line_graph_2()