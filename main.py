import streamlit as st
import pandas as pd
import plotly 
import plotly.express as px
import plotly.graph_objects as go

# Summary section with animation

st.title("Global Land Temperatures by Major City 🌍")
st.subheader("Summary")
st.markdown(""""
This interactive dashboard provides insights into global temperature trends over time.
- 🌍 Use the animated line chart to explore temperature changes dynamically
- 🗺️ Visualize city-level data on a global map with time-based animation.
- 📈 See how temperatures evolve, with trends highlighted by a 10-year rolling average.

Explore, analyze, and uncover patterns in climate data!
""")
st.image("https://img.freepik.com/free-vector/climate-change-concept-illustration_114360-8728.jpg?t=st=1735372379~exp=1735375979~hmac=1b5e3b02fbafcd4399155946836fbea9d12495c547f6617758eef2ebc4f2bd95&w=1060")
# Load temperature data
data = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv")

# Preprocess the data
data["Year"] = pd.to_datetime(data["dt"]).dt.year
data = data.rename(columns={
    "AverageTemperature": "Temperature",
    "AverageTemperatureUncertainty": "Uncertainty",
    "City": "Region"
})

# Region selection
selected_region = st.selectbox("Select City", data["Region"].unique())

# Time period selection
start_year, end_year = st.slider("Select Time Period",
                                int(data["Year"].min()),
                                int(data["Year"].max()),
                                (int(data["Year"].min()), int(data["Year"].max())))

# Filter data
filtered_data = data[(data["Region"] == selected_region) &
                     (data["Year"] >= start_year) &
                     (data["Year"] <= end_year)]

# Line chart
fig = px.line(filtered_data, x="Year", y="Temperature",
              title=f"Temperature Trends for {selected_region}",
              range_y=[filtered_data["Temperature"].min() - 0.5,
                       filtered_data["Temperature"].max() + 0.5])
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Average Temperature (°C)",
    hovermode="x unified"
)
st.plotly_chart(fig)

# Calculate and display average temperature
if not filtered_data.empty:
    average_temp = filtered_data["Temperature"].mean()
    st.write(f"Average Temperature: {average_temp:.2f} °C")
else:
    st.write("No data available for the selected range.")
st.divider()

# Animated Map Visualization
if st.checkbox("Show Animated Map"):
    st.subheader("City Locations and Temperatures Over Time")
    map_data = data.dropna(subset=["Latitude", "Longitude", "Temperature"])
    map_data["Latitude"] = map_data["Latitude"].str[:-1].astype(float) * map_data["Latitude"].str[-1:].map({'N': 1, 'S': -1})
    map_data["Longitude"] = map_data["Longitude"].str[:-1].astype(float) * map_data["Longitude"].str[-1:].map({'E': 1, 'W': -1})
    fig_map = px.scatter_geo(map_data,
                             lat="Latitude",
                             lon="Longitude",
                             color="Temperature",
                             hover_name="Region",
                             title="Global Temperature Map (Animated)",
                             animation_frame="Year",
                             color_continuous_scale="RdBu")
    st.plotly_chart(fig_map)


st.divider()

# Trendline in line chart
if not filtered_data.empty:
    fig.add_trace(go.Scatter(x=filtered_data["Year"],
                             y=filtered_data["Temperature"].rolling(window=10).mean(),
                             mode='lines',
                             name='10-Year Rolling Average'))
    st.plotly_chart(fig)

