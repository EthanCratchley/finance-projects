import pandas as pd
import matplotlib.pyplot as plt

china_gdp = pd.read_csv('CHINAGDP.csv', skiprows=16)
india_gdp = pd.read_csv('INDIAGDP.csv', skiprows=16)
usa_gdp = pd.read_csv('USGDP.csv', skiprows=16)

china_gdp['date'] = pd.to_datetime(china_gdp['date'])
india_gdp['date'] = pd.to_datetime(india_gdp['date'])
usa_gdp['date'] = pd.to_datetime(usa_gdp['date'])

plt.figure(figsize=(12, 8))
plt.plot(china_gdp['date'], china_gdp[' GDP ( Billions of US $)'], label='China')
plt.plot(india_gdp['date'], india_gdp[' GDP ( Billions of US $)'], label='India')
plt.plot(usa_gdp['date'], usa_gdp[' GDP ( Billions of US $)'], label='USA')

plt.title('GDP Comparison: China, India, USA (1960-2024)')
plt.xlabel('Year')
plt.ylabel('GDP (Billions of US $)')
plt.legend()

plt.grid(True)
plt.show()
