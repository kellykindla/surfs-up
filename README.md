# surfs_up Analysis
## Module 9

## Project Overview
### Purpose of Module 9
In this module, we were introduced to SQLite to further advance our skillset in manipulating our data storage and retrieval. Along with SQLite, we used SQLAlchemy and flask to build our knowledge of SQL and display our data in new ways by creating decoupled systems. Through this module, we are able to use SQLAlchemy to connect to and query a SQLite database. To do this, we created engines to query our database and selected that database into a new model so we could build on it in SQLAlchemy and further query our database by creating session links from Python to the Database. We then created a flask application with routes to our findings to easily display our report. 

### Overview of Assignment 
For this assignment, we were asked to analyze the temperature trends of Oahu to give insight on how the temperature and precipitation trends may impact the success of a Surf and Ice Cream Shop year round. Our initial goal of the module was to present the precipitation trends from August 8, 2016- August 8, 2017. We then analyzed the 9 stations the data was retrieved from. Of the 9 stations, we queried the most active station for specific temperature statistics and further analyzed the temperature variation for August 8, 2016- August 8, 2017 at the most active station. We then were introduced to Flask where we created our application which contained routes for the precipitation, stations, temperature observations, and summary statistic findings from the SQL queries to easily share our results to potential investors. For the challenge, we repeated our analysis for the months of June and December where our goal was to query the SQLite database for the temperature observations to create a dataframe and use summary statistics to analyze the data. 

### Resources
The data for Module 9 came from the following SQLite database: **_hawaii.sqlite_** 
#### Software and Dependncies:
	- Jupyter Notebook 6.3.0
	- Python 7.22.0
	- VS Code 1.62.1 
	- Matplotlib- FiveThirtyEight Style 
	- Numpy
	- Pandas
	- Datetime 

## Surfs-Up Analysis Results:
After reflecting our existing database into a new model and connecting the engine to the database, we are able to compose queries using the SQLAlchemy extract function to find the temperature results for June and December. 
Query to gather the temperatures for June:
  
    resultsJun = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == "06").all()
Query to gather the temperatures for December:

    resultsDec = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == "12").all()
We can then convert this data collection to a list and datafame to gather the summary statistics for each with the **__.describe()__** function. From this, we find the following results. 
### Summary Statistics for June:

<img width="191" alt="JuneSS" src="https://user-images.githubusercontent.com/92558842/147246341-98675131-8ff2-430a-b3df-bc482dc7c29c.png">

### Summary Statistics for December:

<img width="183" alt="DecemberSS" src="https://user-images.githubusercontent.com/92558842/147246360-3255529d-93af-468b-8e77-3089b47da2e3.png">

While comparing summary statistics for June and December, we can see that in general, there are minimal differences in temperature variations for the months. Specifically, we find that: 
1. There is a 3.90 degree difference between the averages of June and December.
2. The minimum temperatures between June and December only vary by 8 degrees- June being the warmer month. 
3. The maximum temperatures between June and December vary by 2 degrees. 
4. There is a 4 degree difference between the upper and lower quartiles of June. 
5. There is a 5 degree difference between the upper and lower quartiles of December. 
6. The standard deviations for June and December are relatively low, meaning the data is generally clustered around the mean. 

## Summary 
Overall, the weather analysis for Oahu is promising. There appears to be minimal temperature differences from month to month and for the majority of the days, the temperature is above 65 degrees. Furthermore, the average precipitation is only 0.177 for 2016. With high temperature and low precipitation, it appears that Oahu is a good location to open the Surf and Ice Cream Shop. 
### Additional Queries to Perform
To gather more weather data, I would suggest the following additional queries:
1. To go into depth on year to year temperature variation, I would perform queries where the temperature for each year is extracted and plotted. An example of this query for 2010 is displayed below and if the investors wanted, I would repeat this query for each year, 2010-2017. 

<img width="616" alt="addquery" src="https://user-images.githubusercontent.com/92558842/147246425-b8d95a34-f6f9-454d-928f-608391ecabe8.png">

2. Since the investors wanted data on June and December, I would also write a query to collect the summary statistics for the precipitation of each month. The precipitation summary statistics for December are shown below. 

<img width="1009" alt="addquerydec" src="https://user-images.githubusercontent.com/92558842/147246458-a44c1aa8-2e58-49a1-be39-6f834cfda192.png">

3. Gather the temperature summary statistics for the entire dataset to grasp a general understanding temperature variations and see how temperatures have changed over the 7-year span. 

<img width="677" alt="addquerytotal" src="https://user-images.githubusercontent.com/92558842/147246493-b4f35492-fb39-4a1b-99eb-041a19992724.png">

4. Beyond this dataset, I would suggest to gather data on water temperatures and wind speed around Oahu and write queries to find their summary statistics to see if there is any variation as this can also potentially affect the frequency of surfers. 
