# Global Temperature Trend Dashboard
This Streamlit application provides an interactive dashboard to explore global temperature trends over time. 

**Features:**
* **Animated Line Chart:** Visualizes global temperature anomalies over time for the selected region. 
* **Interactive Map:** (Optional) Displays regional temperature anomalies on a world map, with animations to show changes over time.
* **10-Year Rolling Average:** Highlights long-term temperature trends.
* **Region and Time Period Selection:** Allows users to customize the analysis based on their interests.
* **Average Temperature:** Displays the average temperature for the selected time period.
* **Animated Data Points:** Visually emphasizes the data points with animated circles moving along the line chart.
* **Summary:** Provides a concise overview of the project and its findings.

**Requirements:**

* Python 
* Streamlit
* Pandas
* Plotly
* (Optional) GeoPandas (for map visualization)

**Installation:**

1. Install the required libraries:
   ```bash
    pip install streamlit pandas plotly geopandas

**Run the application**
Bash
streamlit run app.py 

**Usage:**
Select a region from the dropdown menu.
Choose a time period using the sliders.
Observe the animated line chart, which shows the temperature trends over time.
(Optional) Check the "Show Map" checkbox to view the interactive map.
Explore the 10-year rolling average and other visualizations.
