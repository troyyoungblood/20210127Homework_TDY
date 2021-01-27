# SQLAlchemy Homework - Surfs Up!

The following homework has 2 parts, the first conducted in jupyter notebook and the second in vs code.  The analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

path to Jupyter Notebook /Instructions/ty_homework_climate10.ipynb 

path to python file /Instruction/ty_homework_climate10_flask1.py 

## Part I - Climate Analysis and Exploration

Summary of actions, SQLAlchemy was used to `create_engine` for connecting to a sqlite database and `automap_base()` was used to reflect the tables in the database.  This was linked to Python to create dataframes for analysis and plotting.

### A.  Precipitation Analysis

The objective of this section was to create a dataframe containing date and precipitation data for a 12 month period and plot the data.  The analysis started with identifying the most recent date in the data set and then running a query to create a table of the data.  The table was then converted to a dataframe for plotting purposes.

<img src="/images_for_github/recent_date_query.PNG" width = "400">

<img src="/images_for_github/creating_table.PNG" width = "425">

<img src="/images_for_github/ty_HW10_precip_line.png" width_line = "500">'

Pandas was then used to create a summary statistics for the precipitation data.

<img src="/images_for_github/summary_stat_table.PNG" width = "425">

### B. Station Analysis

The objective of this section was to create a histogram of the temperatures from a 12 month period for the most active weather station.  The process started with identifying the number of weather stations in the data set and then finding the most active weather station (the most rows of data).

<img src="/images_for_github/stat_info.PNG" width = "425">

<img src="/images_for_github/station_info.PNG" width = "425">

After the most active weather station was identifed, the lowest (tmin), highest (tmax), and average temperature (tavg) were identified for the station.  This was conducted to create a snapshot of the characteristics of the temerature profile.

<img src="/images_for_github/act_stat_min_max_avg.PNG" width = "425">

A query was then created to collect data for the most recent 12 months for the most active station.  The data was then converted to a dataframe and presented in a histogram with 12 bins.  That data was then presented in a histogram.

<img src="/images_for_github/station_temp_data.PNG" width = "425">

<img src="/images_for_github/ty_HW10_temp_hist.png" width_line = "500">'

## Part II - Climate App

A Flask API is created based on the queries created in Part I.


### Routes created for Part II

A listing of all routes available

<img src="/images_for_github/api_routes.PNG" width = "425">

Precipitation route and snip of browser display

<img src="/images_for_github/precip_snip.PNG" width = "425">

Stations route and snip of browser display

<img src="/images_for_github/stations_snip.PNG" width = "425">

Observed temperatures (tobs) for most active station over past 12 months route and snip of browser display

<img src="/images_for_github/tobs_snip.PNG" width = "425">

For a single date entered - calculate tmin, tmax, and tavg for all dates greater than and equal to the single date route and snip of browser display

<img src="/images_for_github/single_data_snip.PNG" width = "425">


For two dates entered - calculate tmin, tmax, and tavg for all dates between and equal to both dates route and snip of browser displa

<img src="/images_for_github/two_data_snip.PNG" width = "425">

- - -


