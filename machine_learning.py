from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

df_sapporo = pd.read_csv('df_sapporo.csv')
df_sapporo = df_sapporo.dropna(subset=['Year', 'BloomDate', 'DayOfYear'])

# Convert the 'Year' column to a 2D array suitable for sklearn
X = df_sapporo['Year'].values.reshape(-1, 1)

# Convert the 'DayOfYear' column to a 1D array
y = df_sapporo['DayOfYear'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a LinearRegression object
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the first bloom date for the next 10 years
years = np.array(range(2023, 2033)).reshape(-1, 1)
predictions = model.predict(years)

# Print the predictions
#for year, prediction in zip(years, predictions):
#    print(f"The predicted first bloom day of year for {year[0]} is: {prediction}")

def convert_day_of_year_to_date(year, day_of_year):
    date = datetime(year, 1, 1) + timedelta(day_of_year - 1)
    return date

# Test the function
years = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]
predicted_days = [117.6921201775155, 117.5538937309131, 117.4156672843107, 117.27744083770835, 117.13921439110595, 117.00098794450355, 116.86276149790115, 116.7245350512988, 116.5863086046964, 116.448082158094]

for year, day in zip(years, predicted_days):
    date = convert_day_of_year_to_date(year, int(day))
    print(f"The predicted first bloom date in Sapporo for {year} is: {date}")


predicted_data = pd.DataFrame({
    'Year': years,
    'PredictedBloomDay': predicted_days,
    'PredictedBloomDate': [convert_day_of_year_to_date(year, int(day)) for year, day in zip(years, predicted_days)]
})

# Save DF to CSV file
predicted_data.to_csv('predicted_bloom_dates.csv', index=False)