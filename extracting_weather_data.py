import requests
import pandas as pd
from datetime import datetime, timedelta
import time

# Replace with your Visual Crossing API key
API_KEY = "8MCD5ML34CT82T2PVQBJTCUK9"
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

# Define the periods for the cities
city_periods = [
    {"city": "Istanbul", "start_date": "2022-09-18", "end_date": "2023-02-09"},
    {"city": "Beirut", "start_date": "2023-02-09", "end_date": "2023-03-31"},
    {"city": "Istanbul", "start_date": "2023-03-31", "end_date": "2024-01-25"},
    {"city": "Beirut", "start_date": "2024-01-25", "end_date": "2024-02-20"},
    {"city": "Istanbul", "start_date": "2024-02-20", "end_date": "2024-04-10"},
    {"city": "Antalya", "start_date": "2024-04-10", "end_date": "2024-04-15"},
    {"city": "Istanbul", "start_date": "2024-04-15", "end_date": "2024-05-09"},
    {"city": "Beirut", "start_date": "2024-05-09", "end_date": "2024-05-16"},
    {"city": "Istanbul", "start_date": "2024-05-16", "end_date": "2024-12-20"},
]

# Function to split date ranges into smaller chunks (default: 30 days)
def split_date_range(start_date, end_date, max_days=30):
    """Splits a date range into smaller chunks."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_ranges = []
    while start < end:
        chunk_end = min(start + timedelta(days=max_days - 1), end)
        date_ranges.append((start.strftime("%Y-%m-%d"), chunk_end.strftime("%Y-%m-%d")))
        start = chunk_end + timedelta(days=1)
    return date_ranges

# Function to fetch weather data from Visual Crossing API
def fetch_weather(city, start_date, end_date):
    url = f"{BASE_URL}/{city}/{start_date}/{end_date}?key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Data fetched for {city} from {start_date} to {end_date}")
        time.sleep(2)  # Wait 2 seconds between requests to avoid hitting the rate limit
        return response.json()
    else:
        print(f"Error fetching data for {city} from {start_date} to {end_date}: {response.text}")
        return None

# Collect weather data for all periods
all_weather_data = []
for period in city_periods:
    date_chunks = split_date_range(period["start_date"], period["end_date"], max_days=30)
    for start_date, end_date in date_chunks:
        data = fetch_weather(period["city"], start_date, end_date)
        if data and "days" in data:
            for day in data["days"]:
                all_weather_data.append({
                    "city": period["city"],
                    "date": day.get("datetime", None),
                    "temperature": day.get("temp", None),
                    "precipitation": day.get("precip", None),
                    "humidity": day.get("humidity", None),
                    "description": day.get("conditions", None),
                })

# Save the collected data to a CSV file
df = pd.DataFrame(all_weather_data)
if not df.empty:
    df.to_csv("weather_data.csv", index=False)
    print("Weather data saved to 'weather_data.csv'")
else:
    print("No data fetched to save to CSV.")

























'''
import requests
import pandas as pd
from datetime import datetime

# API base URL and key
API_BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
API_KEY = "8MCD5ML34CT82T2PVQBJTCUK9"

# City and date range information
cities = [
    {"name": "Istanbul", "start_date": "2022-09-18", "end_date": "2023-02-08"},
    {"name": "Beirut", "start_date": "2023-02-09", "end_date": "2023-03-30"},
    {"name": "Istanbul", "start_date": "2023-03-31", "end_date": "2024-01-24"},
    {"name": "Beirut", "start_date": "2024-01-25", "end_date": "2024-02-19"},
    {"name": "Istanbul", "start_date": "2024-02-20", "end_date": "2024-04-09"},
    {"name": "Antalya", "start_date": "2024-04-10", "end_date": "2024-04-14"},
    {"name": "Istanbul", "start_date": "2024-04-15", "end_date": "2024-05-08"},
    {"name": "Beirut", "start_date": "2024-05-09", "end_date": "2024-05-15"},
    {"name": "Istanbul", "start_date": "2024-05-16", "end_date": "2024-12-20"},
]

# Function to fetch weather data for a city and date range
def fetch_weather_data(city):
    url = f"{API_BASE_URL}/{city['name']}/{city['start_date']}/{city['end_date']}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Parse daily weather data
        weather_data = []
        for day in data["days"]:
            date_str = day["datetime"]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            day_name = date_obj.strftime("%A")
            weather_data.append({
                "Date": f"{date_str},{day_name}",
                "Temperature": day.get("temp", None),
            })
        return weather_data
    else:
        print(f"Error fetching data for {city['name']}: {response.status_code}")
        return []

# Collect weather data for all cities
all_weather_data = []
for city in cities:
    all_weather_data.extend(fetch_weather_data(city))

# Save data to CSV
df = pd.DataFrame(all_weather_data)
df.to_csv("weather_data_with_days.csv", index=False)
print("Weather data saved to 'weather_data_with_days.csv'")
'''