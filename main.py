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





