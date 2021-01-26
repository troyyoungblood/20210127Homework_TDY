# 20210127Homework_TDY
Surfs Up - SQLAlchemy Homework

The following homework has 2 parts, the first conducted in jupyter notebook and the second in vs code.  The analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Part I - Climate Analysis and Exploration

Summary of actions, SQLAlchemy was used to `create_engine` for connecting to a sqlite database and `automap_base()` was used to reflect the tables in the database.  This was linked to Python to create dataframes for analysis and plotting.

### A.  Precipitation Analysis

The objective of this section was to create a dataframe containing date and precipitation data for a 12 month period and plot the data.  The analysis started with identifying the most recent date in the data set and then running a query to create a table of the data.  The table was then converted to a dataframe for plotting purposes.

<img src="/images_for_github/recent_date_query.PNG" width = "450">

<img src="/images_for_github/creating_table.PNG" width = "450">


----4) insert plot

Pandas was then used to create a summary statistics for the precipitation data.

----5) insert snip of table

### B. Station Analysis

The objective of this section was to create a histogram of the temperatures from a 12 month period for the most active weather station.  The process started with identifying the number of weather stations in the data set and then finding the most active weather station (the most rows of data).

After the most active weather station was identifed, the lowest (tmin), highest (tmax), and average temperature (tavg) were identified for the station.  This was conducted to create a snapshot of the characteristics of the temerature profile.

---- insert query and results

A query was then created to collect data for the most recent 12 months for the most active station.  The data was then converted to a dataframe and presented in a histogram with 12 bins.

-- insert pic of query
-- insert pic of histogram


## Part II - Climate App

A Flask API is created based on the queries created in Part I.

### Routes created for Part II

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.

  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

## Bonus: Other Recommended Analyses

* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.

* Use the provided [temp_analysis_bonus_1_starter.ipynb](temp_analysis_bonus_1_starter.ipynb) and [temp_analysis_bonus_1_starter](temp_analysis_bonus_2_starter.ipynb) starter notebooks for each bonus challenge.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Use pandas to perform this portion.

  * Convert the date column format from string to datetime.

  * Set the date column as the DataFrame index

  * Drop the date column

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* You are looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. Using historical data in the dataset find out what the temperature has previously looked like.

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use "Trip Avg Temp" as the title.

  * Use the average temperature as the bar height (y value).

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

    ![temperature](Images/temperature.png)

### Daily Rainfall Average

* Now that you have an idea of the temperature lets check to see what the rainfall has been, you don't want a when it rains the whole time!

* Calculate the rainfall per weather station using the previous year's matching dates.

  * Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

  * Set the start and end date of the trip.

  * Use the date to create a range of dates.

  * Strip off the year and save a list of strings in the format `%m-%d`.

  * Use the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

  ![daily-normals](Images/daily-normals.png)

* Close out your session.
