# Importing modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining a function to read a datafile


def read(file):
    df = pd.read_csv(file)
    df_transpose = df.set_index("Country Name").transpose()
    return df, df_transpose


def bar_graph_1():
    """
    This function is for plotting the bar graph of population total.
    """

    plt.figure()
    ax = plt.subplot(1, 1, 1)
    pop, pop_transpose = read("Population_total.csv")

    x = np.arange(len(pop.index))
    w = 0.1

    plt.bar(x, pop["1995"].values, width=w, label='1995')
    plt.bar(x+w, pop['2000'].values, width=w, label='2000')
    plt.bar(x+w*2, pop['2005'].values, width=w, label='2005')
    plt.bar(x+w*3, pop['2010'].values, width=w, label='2010')
    plt.bar(x+w*4, pop['2015'].values, width=w, label='2015')
    ax.set_xlabel("Country Name")
    ax.set_ylabel("Population")
    ax.set_title("Total Population", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(pop["Country Name"])
    ax.legend(loc='upper left')
    ax.figure.savefig("population.png", bbox_inches="tight")
    ax.figure.show()


def bar_graph_2():
    """
    This function is for plotting the bar graph of CO2 emissions from solid 
    fuel consumption(kt)
    """

    plt.figure()
    ax = plt.subplot(1, 1, 1)
    co2, co2_transpose = read(
        "CO2_emissions_from_solid_fuel_consumption_(kt).csv")

    x = np.arange(len(co2.index))
    w = 0.1

    plt.bar(x, co2['1995'].values, width=w, label='1995')
    plt.bar(x+w, co2['2000'].values, width=w, label='2000')
    plt.bar(x+w*2, co2['2005'].values, width=w, label='2005')
    plt.bar(x+w*3, co2['2010'].values, width=w, label='2010')
    plt.bar(x+w*4, co2['2015'].values, width=w, label='2015')
    ax.set_xlabel("Country Name")
    ax.set_ylabel("CO2 emission")
    ax.set_title("CO2 Emissions from Solid Fuel Consumption(kt)", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(co2["Country Name"])
    ax.legend(loc='upper left')
    ax.figure.savefig("fuel_consumption.png", bbox_inches="tight")
    ax.figure.show()


def line_graph_1():
    """
    This function is for plotting a line graph of Electricity production
    from coal sources(%) of total using iteration.
    """

    coal, coal_transpose = read(
        "Electricity_production_from_coal_sources(% of total).csv")

    plt.figure()
    lab1 = ["Australia", "Belgium", "Canada",
            "Germany", "Israel", "Japan", "Mexico"]
    for i in range(len(lab1)):
        plt.plot(coal_transpose.index, coal_transpose[lab1[i]], label=lab1[i])
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Electricity production(in %)", fontsize=12)
    plt.title("Electricity Production from Coal Sources (% of total)",
              pad=60, fontsize=15)
    plt.xticks()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
               fancybox=True, shadow=True, ncol=4)

    plt.savefig("electricity_production.png", bbox_inches="tight")
    plt.show()


def line_graph_2():
    """
    This function is for plotting a line graph of Electric power 
    consumption(kWh per capita) using iteration
    """

    power, power_transpose = read(
        "Electric_power_consumption(kWh per capita).csv")

    plt.figure()
    lab2 = ["Australia", "Belgium", "Canada",
            "Germany", "Israel", "Japan", "Mexico"]
    for i in range(len(lab2)):
        plt.plot(power_transpose.index,
                 power_transpose[lab2[i]], label=lab2[i])
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Electric power consumption(kWh)", fontsize=12)
    plt.title("Electric Power Consumption (kWh per capita)",
              pad=60, fontsize=15)
    plt.xticks()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25),
               fancybox=True, shadow=True, ncol=4)
    plt.savefig("power_consumption.png", bbox_inches="tight")
    plt.show()


def CO2_data_mean():
    """
    This function is used to calculate the mean of CO2 emissions from solid 
    fuel consumption(kt) of the selected countries.
    """

    df1, df2 = read("CO2_emissions_from_solid_fuel_consumption_(kt).csv")
    df = df1.set_index("Country Name")
    transpose = df.transpose()
    cleaned_data = transpose.fillna(0)
    mean = cleaned_data[["Australia", "Belgium", "Canada", "Germany", "Israel",
                         "Japan", "Mexico"]].mean()
    return mean


# Reading the csv file to get a return of dataframes
pop, pop_transpose = read("Population_total.csv")
co2, co2_transpose = read("CO2_emissions_from_solid_fuel_consumption_(kt).csv")
coal, coal_transpose = read(
    "Electricity_production_from_coal_sources(% of total).csv")
power, power_transpose = read("Electric_power_consumption(kWh per capita).csv")

# Calling the functions
bar_graph_1()
bar_graph_2()
line_graph_1()
line_graph_2()

# Function to return the mean of CO2 emissions
mean = CO2_data_mean()
mean = mean.to_csv("mean_of_CO2.csv")
