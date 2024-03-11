# 10_sqlalchemy-challenge

## Main Concept
- analyze climate data using Python and SQLAlchemy, then design a Flask API to share the findings

## Objective
- understand the climate patterns in Honolulu, Hawaii, by examining precipitation and temperature data, and to create an interface for accessing this information easily.

### Part 1: Analyze and Explore the Climate Data

1. Use Pandas Plotting with Matplotlib to print the summary statistics for the precipitation data from 2016-08-13 to 2017-08-23
![Climate Precipitation](https://github.com/vanillatyy1/10_sqlalchemy-challenge/blob/6eb6e159c13a91a405f0837cdfe12fa801b90b9e/Surfsup/climate_prcp.jpg)

3. Previous 12 months of temperature observation (TOBS) data of the most active station
![Temperature Frequency](https://github.com/vanillatyy1/10_sqlalchemy-challenge/blob/6eb6e159c13a91a405f0837cdfe12fa801b90b9e/Surfsup/tem_freq.jpg)

### Part 2 - Climate App
Code: 
Design a Flask API to provide access to climate data analysis results.
Define routes to navigate the API, including a homepage and all available routes.
1. ("/"): serve as the homepage, listing available routes.
2. "/api/v1.0/precipitation": precipitation data for the last 12 months as JSON.
3. "/api/v1.0/stations": to provide a JSON list of weather stations.
4. "/api/v1.0/tobs": to retrieve temperature observations for the previous year from the most-active station.
5. /api/v1.0/<start>/<end>: calculate temperature statistics (min/max/avg) for a specified date range.
