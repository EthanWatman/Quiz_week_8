#Imports Libraries
import matplotlib.pyplot as plt
import sqlite3
#Creates Required Lists
years = []
co2 = []
temp = []

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
ClimateDB = cursor.fetchall()
for Rows in ClimateDB:
    years.append(Rows[0])
    co2.append(Rows[1])
    temp.append(Rows[2])
conn.close()

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
plt.savefig("co2_temp_1.png") 
