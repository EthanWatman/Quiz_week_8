#Imports Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Loads CSV
data = pd.read_csv('climate.csv')

#Creates Required Lists and Fills the Lists from Column Names
years = data['Year']
co2 = data['CO2']
temp = data['Temperature']

#Code Supplied
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")
plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")
