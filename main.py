import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r'E:\user\Documents\Sabanci University Courses\CS Courses\CS210\xml_to_csv_project\step_count_data_with_day.csv'
step_data = pd.read_csv(file_path)

# Convert the Date column to a datetime object
step_data['Date'] = pd.to_datetime(step_data['Date'])

# Display the first few rows of the data
print(step_data.head())



# Basic descriptive statistics for the Steps column
step_stats = step_data['Steps'].describe()
print(step_stats)


# Plot the distribution of step counts
plt.figure(figsize=(10, 6))
sns.histplot(step_data['Steps'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Daily Step Counts', fontsize=16)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# Plot step counts over time
plt.figure(figsize=(15, 6))
plt.plot(step_data['Date'], step_data['Steps'], color='blue', alpha=0.7)
plt.title('Daily Step Counts Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.grid(True)
plt.show()


# Group data by day of the week and calculate the average steps
step_data['Day'] = step_data['Date'].dt.day_name()
avg_steps_by_day = step_data.groupby('Day')['Steps'].mean()

# Reorder days of the week for better visualization
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_steps_by_day = avg_steps_by_day.reindex(day_order)

# Bar plot of average steps by day of the week
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_steps_by_day.index, y=avg_steps_by_day.values, palette='viridis')
plt.title('Average Steps by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Average Steps', fontsize=12)
plt.show()



# Calculate a 7-day rolling average
step_data['7_day_avg'] = step_data['Steps'].rolling(window=7).mean()

# Plot daily steps and the 7-day rolling average
plt.figure(figsize=(15, 6))
plt.plot(step_data['Date'], step_data['Steps'], label='Daily Steps', alpha=0.5)
plt.plot(step_data['Date'], step_data['7_day_avg'], label='7-Day Rolling Average', color='red', linewidth=2)
plt.title('Daily Steps with 7-Day Rolling Average', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()



# Define thresholds for outliers (e.g., very low or very high steps)
low_threshold = step_data['Steps'].quantile(0.05)
high_threshold = step_data['Steps'].quantile(0.95)

# Identify outlier days
outliers = step_data[(step_data['Steps'] < low_threshold) | (step_data['Steps'] > high_threshold)]
print(f"Outliers (low threshold: {low_threshold}, high threshold: {high_threshold}):")
print(outliers)







# Load the weather data
weather_file_path = 'weather_data.csv'  
weather_data = pd.read_csv(weather_file_path)

# Convert the date column to datetime for alignment
weather_data['date'] = pd.to_datetime(weather_data['date'])
step_data['Date'] = pd.to_datetime(step_data['Date'])

# Merge step count and weather data on the date column
merged_data = pd.merge(step_data, weather_data, left_on='Date', right_on='date', how='inner')

# Display the first few rows of the merged data
print(merged_data.head())


# Calculate average steps by temperature range
temperature_bins = [0, 50, 70, 90, 110]  # Define temperature ranges (in Fahrenheit)
temperature_labels = ['Low', 'Moderate', 'High', 'Very High']
merged_data['Temp_Range'] = pd.cut(merged_data['temperature'], bins=temperature_bins, labels=temperature_labels)

# Average steps by temperature range
avg_steps_by_temp_range = merged_data.groupby('Temp_Range')['Steps'].mean()
print("Average Steps by Temperature Range:")
print(avg_steps_by_temp_range)

# Average steps by weather description
avg_steps_by_weather = merged_data.groupby('description')['Steps'].mean()
print("\nAverage Steps by Weather Description:")
print(avg_steps_by_weather)



import matplotlib.pyplot as plt
import seaborn as sns

# Scatter Plot: Steps vs. Temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_data, x='temperature', y='Steps', hue='description', alpha=0.7)
plt.title('Scatter Plot of Steps vs Temperature', fontsize=16)
plt.xlabel('Temperature (°F)', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.legend(title='Weather Description')
plt.grid(True)
plt.show()

# Boxplot: Steps by Weather Description
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_data, x='description', y='Steps', palette='coolwarm')
plt.title('Boxplot of Steps by Weather Description', fontsize=16)
plt.xlabel('Weather Description', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Line Plot: Steps and Temperature Trends Over Time
plt.figure(figsize=(15, 6))
plt.plot(merged_data['Date'], merged_data['Steps'], label='Steps', color='blue', alpha=0.6)
plt.plot(merged_data['Date'], merged_data['temperature'], label='Temperature (°F)', color='red', alpha=0.6)
plt.title('Steps and Temperature Trends Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Steps / Temperature', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
 


# Correlation between temperature and step counts
correlation = merged_data['temperature'].corr(merged_data['Steps'])
print(f"Correlation between temperature and step counts: {correlation:.2f}")


sns.lmplot(data=merged_data, x='temperature', y='Steps', scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Steps vs. Temperature with Regression Line')
plt.xlabel('Temperature (°F)')
plt.ylabel('Steps')
plt.show()


import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Extract the features (temperature) and target (steps)
X = merged_data['temperature'].values.reshape(-1, 1)
y = merged_data['Steps']

# Create polynomial features (degree 2 for simplicity)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit a linear regression model on the polynomial features
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
y_pred = model.predict(X_poly)

# Evaluate the model
r2 = r2_score(y, y_pred)
print(f"R-squared for Polynomial Regression (degree 2): {r2:.2f}")

# Visualize the original data and the polynomial fit
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['temperature'], y, color='blue', alpha=0.5, label='Actual Data')
plt.plot(merged_data['temperature'], y_pred, color='red', label='Polynomial Fit (degree 2)')
plt.title('Steps vs. Temperature with Polynomial Regression')
plt.xlabel('Temperature (°F)')
plt.ylabel('Steps')
plt.legend()
plt.grid(True)
plt.show()

