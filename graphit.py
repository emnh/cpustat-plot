#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("cpustat_data.csv") #, skiprows=2)  # Skip the first two lines (Task and Ticks)

# Plot CPU usage for each process over time
plt.figure(figsize=(12, 8))

timestamps = df.iloc[:, 0].to_numpy()
headers = df.iloc[0]

for column, header in zip(df.columns[1:], headers):
    plt.plot(timestamps, df[column].to_numpy() * 100, label=f"{column}")

# Customize the plot
plt.ylim(0, 100)
yt = [0, 25, 50, 75, 100]
ytl = [str(x) + '%' for x in yt]
plt.yticks(yt, ytl)
plt.xlabel('Timestamp')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage Over Time for Each Process')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.savefig('output.png')
