import pandas as pd

# Load the data
df_melted = pd.read_csv('melted_data.csv')

# Perform some basic analysis
print(df_melted.describe())

# Save the results to a file
df_melted.describe().to_csv('analysis_results.csv')