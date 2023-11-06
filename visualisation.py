import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df_melted = pd.read_csv('melted_data.csv')

# Convert 'BloomDate' back to datetime
df_melted['BloomDate'] = pd.to_datetime(df_melted['BloomDate'])

# Calculate the day of the year
df_melted['DayOfYear'] = df_melted['BloomDate'].dt.dayofyear

# Filter data for Sapporo
df_sapporo = df_melted[df_melted['Location'] == 'Sapporo']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(df_sapporo['Year'], df_sapporo['DayOfYear'], marker='o', color='pink')

plt.title('Cherry Blossom First Bloom Dates in Sapporo')
plt.xlabel('Year')
plt.ylabel('Day of Year')

plt.show()

df_sapporo.to_csv('df_sapporo.csv', index=False)