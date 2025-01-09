# DSA210-Project-2024---Weather-and-Step-Counts

# Steps vs Weather: Exploring Correlation  

## Project Overview  
This project explores the potential correlation between weather conditions and daily step counts. The hypothesis is that higher temperatures are associated with an increase in my physical activity, measured through my step counts. By analyzing personal step data alongside weather data, this project aims to uncover patterns and insights about how environmental factors influence my movement.  

## Dataset Description  
The project uses two primary datasets:  
1. **Step Count Data**: Sourced from the iPhone Health app, this dataset contains daily step counts recorded over the years 2023 and 2024.  
2. **Weather Data**: Gathered from the Weather app, this dataset includes daily temperature, weather conditions, and other relevant metrics from the same time period.  

### Data Fields  
**Step Count Data:**  
- Date  
- Number of Steps  

**Weather Data:**  
- Date  
- Daily Average Temperature  
- Weather Condition (e.g., sunny, rainy, cloudy)  

## Project Plan  

### Phase 1: Data Collection  
- Export step count data from the iPhone Health app.  
- Scrape or retrieve weather data for the corresponding dates from the Weather app.  

### Phase 2: Data Cleaning and Preprocessing  
- Ensure both datasets are aligned by date.  
- Handle missing or inconsistent data points.  

### Phase 3: Exploratory Data Analysis (EDA)  
- Visualize step count trends over time.  
- Examine weather patterns and distributions.  
- Explore relationships between step counts and weather conditions, with a focus on temperature.  

### Phase 4: Hypothesis Testing  
- Conduct statistical tests to evaluate the hypothesis: *Higher temperatures correlate with an increase in my step counts.*  

### Phase 5: Reporting  
- Summarize findings in a report with visuals and conclusions.  
- Discuss potential factors influencing results and areas for further exploration.  

## Tools and Technologies  
- Data Collection: Python
- Data Analysis and Visualization: Pandas, Matplotlib, Seaborn
- Statistical Testing: Python's scipy library

## Directory Structure

### Data Folder:
- `export_health_app.zip`: Contains raw data exported from the iPhone Health app.
- `step_count_data_with_day.csv`: Cleaned step count data with dates and days of the week.
- `weather_data.csv`: Daily weather data including temperature and conditions.

### Extracting Data Python Codes:
- `extracting_step_counts_data.py`: Script for processing and cleaning step count data.
- `extracting_weather_data.py`: Script for retrieving and formatting weather data.

### Project Figures:
- Contains all the visualizations and diagrams generated during the analysis.

### Project Report:
- `CS210 Project Report.docx`: Final report summarizing the project's objectives, methodology, findings, and conclusions.

### Main Analysis Script:
- `main.py`: Combines all data analysis steps, including cleaning, visualizations, and statistical tests.
