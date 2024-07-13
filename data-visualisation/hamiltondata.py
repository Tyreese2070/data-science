import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('lewishamilton.csv')

# Replace 'ab' and 'dsq' with 20
df.loc[df['race_position'] == 'ab', 'race_position'] = 20
df.loc[df['race_position'] == 'dsq', 'race_position'] = 20

# Convert race_position to integer
df['race_position'] = df['race_position'].astype(int)

# Get unique years
years = df['Year'].unique()

# Prepare data for the bar plot
win_counts = []

for year in years:
    # Filter the dataframe for the specific year
    year_df = df[df['Year'] == year]
    # Count the number of wins (race_position == 1)
    win_count = (year_df['race_position'] == 1).sum()
    win_counts.append(win_count)

# Plot the bar chart
plt.bar(years, win_counts)

# Add labels
plt.xlabel('Year')
plt.ylabel('Wins')
plt.title('Lewis Hamilton Race Wins Each Year')
plt.xticks(years)

# Show the plot
plt.show()
