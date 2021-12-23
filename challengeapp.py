#import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy import extract
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
    Welcome to the Climate Analysis Challenge API!<br/>
    Available Routes:<br/>
    Temperatures for June:
    /api/v1.0/tobsJun<br/>
    Temperatures for December:
    /api/v1.0/tobsDec<br/>
    ''')
#add route to temperatures for June
@app.route("/api/v1.0/tobsJun")
def temp_june():
    # Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
    resultsJun = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == "06").all()
    tempsJun = list(np.ravel(resultsJun))
    return jsonify(tempsJun = tempsJun)

#add route to temperatures for December
@app.route("/api/v1.0/tobsDec")
def temp_Dec():
    # 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
    resultsDec = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == "12").all()
    tempsDec = list(np.ravel(resultsDec))
    return jsonify(tempsDec=tempsDec)






