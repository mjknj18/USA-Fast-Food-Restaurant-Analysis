# USA-Fast-Food-Restaurant-Analysis

The purpose of this project was to build an interactive dashboard from USA fast food restaurant location data using a multi-step approach. First, Python, with Pandas and SQLAlchemy, was used to perform an ETL process to transfer the data to a SQL database. Then, Python, with Flask, SQLAlchemy, and Pandas, was used to create a local application with several user-selectable routes for table conversion and transfer to HTML web pages. Finally, JavaScript, with Charts JS and Leaflet, was used to create the interactive visualizations within each web page.

## Questions

1. What are the zip codes with the most fast food restaurants in the entire country?
2. What are the zip codes with the most fast food restaurants in each state?
3. What are the most common fast food restaurant chains in the entire country?
4. What are the most common fast food restaurant chains in each state?
5. How are fast food restaurants distributed across the country?
6. How are fast food restaurants distributed across each state?

## Datasets

1. https://github.com/mjknj18/USA-Fast-Food-Restaurant-Analysis/blob/master/Data/Fast_Food_Restaurants_Jun19.csv

## Tasks

### ETL Process

1. Import the fast food restaurant CSV data as a Pandas data frame.
2. Clean the data frame by dropping rows and columns with missing and/or unneccessary data.
3. Create separate data frames for each state and Washington DC.
4. Create a PostgreSQL database, and generate tables, with the appropriate primary and foreign keys.
5. Populate the tables with data from the appropriate data frames.

### Application Creation

1. Establish a connection to the PostgreSQL database.
2. Create the different user-selectable routes and internal functions for data processing.
3. For each route, extract the appropriate tables from the database and convert them to JSON format.
4. Export the converted JSON data to the appropriate HTML web page.

### Dashboard Creation

#### Chart Visualization Web Page

1. Import the JSON data passed from the Flask application.
2. Filter the data to find the most common zip codes and restaurant chains.
3. Plot the filtered data in both bar chart and doughnut chart format.
4. Create dropdown menu to allow user to change between chart formats.
5. Attach the web page to the appropriate Flask routes.

#### Map Visualization Web Page

1. Import the JSON data passed from the Flask application.
2. Import different map layers (outdoors/satellite/light/dark) from the Mapbox API.
3. Select the appropriate map center coordinates and zoom level based on the imported data.
4. Add a marker for each restaurant based on its coordinates.
5. Add a popup for each marker containing the restaurant name and address.
6. Attach the web page to the appropriate Flask routes.

## Results

1. http://localhost:5000/ (Must also run the app.py file from the command line.)