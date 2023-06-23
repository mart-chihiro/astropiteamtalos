import pandas as pd
import matplotlib.pyplot as plt

#read the data from the file
data = pd.read_csv('dataISS&Earth.csv')

#correlation between ISS temp & Earth temp
r_temp = data['iss_temp'].corr(data['earth_temp'])
print("correlation between ISS temp & Earth temp",r_temp)

temp_iss_mean = data['iss_temp'].mean()
print("mean iss temp", temp_iss_mean)

temp_earth_mean = data['earth_temp'].mean()
print("mean earth temp",temp_earth_mean)

#correlation between ISS hum & Earth hum
r_hum = data['iss_hum'].corr(data['earth_hum'])
print("correlation between ISS hum & Earth hum", r_hum)

hum_iss_mean = data['iss_hum'].mean()
print("mean iss hum", hum_iss_mean)

hum_earth_mean = data['earth_hum'].mean()
print("mean earth hum", hum_earth_mean)

#correlation between ISS press & Earth press
r_press = data['iss_press'].corr(data['earth_press'])
print("correlation between ISS press & Earth press", r_press)

press_iss_mean = data['iss_press'].mean()
print("mean iss press", press_iss_mean)

press_earth_mean = data['earth_press'].mean()
print("mean earth press", press_earth_mean)


#correlation between ISS hum & ISS temp
r_hum_temp_iss = data['iss_hum'].corr(data['iss_temp'])
print("correlation between ISS hum & ISS temp", r_hum_temp_iss)

# plot ISS hum & ISS temp
plt.scatter(data['iss_hum'], data['iss_temp'])
plt.xlabel("Humidity (%)")
plt.ylabel('Temperature (°C)')
plt.title('ISS Humidity vs ISS Temperature')
plt.text(0.5, 0.95, f'Correlation: {r_hum_temp_iss:.2f}', ha='center', va='center', transform=plt.gca().transAxes)
plt.show()

#correlation between ISS hum & ISS press
r_hum_press_iss = data['iss_hum'].corr(data['iss_press'])
print("correlation between ISS hum & ISS press", r_hum_press_iss)

# plot ISS hum & ISS press
plt.scatter(data['iss_hum'], data['iss_press'])
plt.xlabel("Humidity (%)")
plt.ylabel('Pressure (hPa)')
plt.title('ISS Humidity vs ISS Pressure')
plt.text(0.5, 0.95, f'Correlation: {r_hum_press_iss:.2f}', ha='center', va='center', transform=plt.gca().transAxes)
plt.show()

#correlation between ISS temp & ISS press
r_temp_press_iss = data['iss_temp'].corr(data['iss_press'])
print("correlation between ISS temp & ISS press", r_temp_press_iss)

# plot ISS temp & ISS press
plt.scatter(data['iss_temp'], data['iss_press'])
plt.xlabel("Temperature (°C)")
plt.ylabel('Pressure (hPa)')
plt.title('ISS Temperature vs ISS Pressure')
plt.text(0.5, 0.95, f'Correlation: {r_temp_press_iss:.2f}', ha='center', va='center', transform=plt.gca().transAxes)
plt.show()