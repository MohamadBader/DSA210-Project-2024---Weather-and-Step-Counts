import xml.etree.ElementTree as ET
import csv
from datetime import datetime

# Specify input and output file paths
xml_file = "export.xml" 
csv_file = "step_count_data_with_day.csv"

# Open CSV for writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Day", "Steps"])  # Header row

    daily_steps = {}

    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Iterate through <Record> elements  "HKQuantityTypeIdentifierStepCount"
        for record in root.findall("Record"):
            if (record.get("type") == "HKQuantityTypeIdentifierStepCount" and
                    record.get("sourceName") == "Mohamad’s iphone"):
                # Extract step count and date
                start_date = record.get("startDate")
                step_count = int(record.get("value"))

                # Remove timezone and parse the date
                start_date_without_timezone = start_date.split()[0] + " " + start_date.split()[1]
                date_time = datetime.strptime(start_date_without_timezone, "%Y-%m-%d %H:%M:%S")
                
                # Get only the date part
                date = date_time.date()

                # Aggregate daily steps
                daily_steps[date] = daily_steps.get(date, 0) + step_count

        # Write aggregated data to CSV
        for date, steps in sorted(daily_steps.items()):
            day_of_week = date.strftime("%A")  # Get the day of the week
            writer.writerow([date, day_of_week, steps])

        print(f"Data successfully filtered and converted to {csv_file}")

    except ET.ParseError as e:
        print(f"XML Parsing Error: {e}")
