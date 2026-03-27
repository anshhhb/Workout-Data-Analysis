import pandas as pd
import numpy as np
#Load Data

df = pd.read_csv("w3s.csv")
# print("Shape: ", df.shape)
# print(df.head())


#Find Missing Values
# print("\n Missing Values: ", df.isnull().sum())

df["Calories"] = df["Calories"].fillna(df["Calories"].mean())

df["Colories_per_min"] = df["Calories"]/df["Duration"]
df["Pulse_Level"] = df["Pulse"].apply(lambda x: "High" if x >110 else "Normal")


#Analysis

avg_calories = df.groupby("Duration")["Pulse"].mean()
max_pulse = df.groupby("Duration")["Pulse"].max()
correlation = df.corr(numeric_only = True)

# print("\nAverage Calories: \n", avg_calories)
# print("\n Max Pulse: ", max_pulse)
# print("\nCorrelation: ", correlation)



#Filtering Insights

high_intensity = df[(df["Pulse"] > 110) & (df["Calories"] > 300)]
# print("\n High Intensity Workouts: \n", high_intensity.head())



#Sorting
top_calories = df.sort_values("Calories", ascending = False)
# print("\n Top Calories Burn: \n", top_calories.head())




print("\n Average Calories: \n", avg_calories.head().round(2))
print("\nMax Pulse: \n", max_pulse.head().round(2))
print("\nCorrelation:\n ", correlation.round(2).round(2))
print("\nHigh Intensity: \n", high_intensity.head())
print("\n Top calories: \n", top_calories.head().round(2))




import matplotlib.pyplot as plt


#1 Avg Calories by Duration
df.groupby("Duration")["Calories"].mean().plot(kind = "bar")
plt.title("Average Calories by Duration")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Calories")
plt.show()



#2 Pulse vs Calories
plt.scatter(df["Pulse"], df["Calories"])

# add trend line
z = np.polyfit(df["Pulse"], df["Calories"], 1)
p = np.poly1d(z)
plt.plot(df["Pulse"], p(df["Pulse"]))

plt.title("Pulse vs Calories with Trend Line")
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.show()



