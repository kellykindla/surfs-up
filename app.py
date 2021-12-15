#import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import flask dependencies 
from flask import Flask, jsonify

#access the SQLite database 
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes 
Base = automap_base()

#reflect the database tables 
Base.prepare(engine, reflect=True)

#save references for each table 
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to the database
session = Session(engine)

#create a flask application called "app"
app = Flask(__name__)
#create root of routes 
@app.route("/")
def welcome():
    #add precipitation, stations, tobs, and temp routes 
    # in an f-string into return statement
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')
#add route to precipiation 
@app.route("/api/v1.0/precipitation")
def precipitation():
    #calculate the data one year ago from most recent date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query to get the date and precipitation for prev_year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
#add route to stations 
@app.route("/api/v1.0/stations")
def stations():
    #query that allows us to get all of the stations in our database
    results = session.query(Station.station).all()
    #unravel our results and convert them to a list
    stations = list(np.ravel(results))
    #format our list as JSON with jsonify
    return jsonify(stations = stations )
#add route to temperature 
@app.route("/api/v1.0/tobs")
def temp_monthly():
    #query the primary station for all tobs from the previous year 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #unravel results into a 1D array and convert to a list- jsonify results 
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
#create a route for summary statistic report from the starting and end date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    #query to select the min, avg, max temps
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    #add if-not statement to determine starting and ending date  
    if not end:
        # * means there are multiple results for the query
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    #query to get statistics data 
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

