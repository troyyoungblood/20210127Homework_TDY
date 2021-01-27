import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Meas = Base.classes.measurement
Sta = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes"""
    """Homework_10_SQLAlchemy"""
    return (
        f"Available Routes:<br/>"
        f"-----------------------------------------------------------<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"-----------------------------------------------------------<br/>"
        f"/api/v1.0/stations<br/>"
        f"-----------------------------------------------------------<br/>"
        f"/api/v1.0/tobs<br/>"
        f"-----------------------------------------------------------<br/>"
        f"/api/v1.0/start_only/<string:2016-01-01><br/>"
        f'enter date after / in form of YYYY-MM-DD<br/>'
        f"-----------------------------------------------------------<br/>"
        f"/api/v1.0/start_end/<string:2016-01-01>/<string:2016-12-31><br/>"
        f"takes 2 dates - enter start between / and end after last /<br/>"
        f"in the form of YYYY-MM-DD"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
### Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of Date and Precipitaton Data for last year of report"""
    # Query all measurements
    wdata = session.query(Meas.date, Meas.prcp).\
            filter(Meas.date.between ("2016-08-23", "2017-08-23")).all()

    session.close()

    # Create a dictionary from the row data and append to a list of weather data
    date_precip = []
    for date, prcp in wdata:
        dpdata_dict = {}
        dpdata_dict[date] = prcp
        date_precip.append(dpdata_dict)

    return jsonify(date_precip)


@app.route("/api/v1.0/stations")
def stations():
### Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations"""
    # Query all measurements
    sta_names = session.query(Sta.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of weather data
    sta_list = []
    for name in sta_names:
        sta_name_dict = {}
        sta_name_dict["name"] = name
        sta_list.append(sta_name_dict)

    return jsonify(sta_list)


@app.route("/api/v1.0/tobs")
def tobs():
### Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temp observations for most active station for last year of report"""
    # Query all measurements
    act_sta_data = session.query(Meas.tobs).\
               filter(Meas.station == 'USC00519281').\
               filter(Meas.date.between ("2016-08-18", "2017-08-18")).all()

    session.close()

    # Create a dictionary from the row data and append to a list of temperature data
    temp_list = []
    for tobs_data in act_sta_data:
        tobs_dict = {}
        tobs_dict["temperature (F)"] = tobs_data
        temp_list.append(tobs_dict)

    return jsonify(temp_list)


@app.route("/api/v1.0/start_only/<start_temp>")

def start_only(start_temp):
    """Fetch the TMIN, TMAX, TMAX for most active station for
       all dates and including start_date supplied by the user."""

### Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all measurements
    active_sta_start = session.query(func.min(Meas.tobs), func.max(Meas.tobs), func.avg(Meas.tobs)).\
                       filter(Meas.date >= start_temp).\
                       filter(Meas.station == 'USC00519281').all()   

    session.close()

 # Create a dictionary from the row data and append to a list of temp data
    start_temp_results = []

    for min, max, avg in active_sta_start:
        temp_gtstart = {}
        temp_gtstart["min"] = min
        temp_gtstart["max"] = max
        temp_gtstart["avg"] = avg
        start_temp_results.append(temp_gtstart)

    return jsonify(start_temp_results)

# if __name__ == '__main__':
#     app.run(debug=True)


@app.route("/api/v1.0/start_end/<u_start_date>/<u_end_date>")

def start_end(u_start_date,u_end_date):
    """Fetch the TMIN, TMAX, TMAX for most active station for
       all dates and including start and end dates supplied by the user."""

### Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all measurements
    act_sta_temp_sande = session.query(func.min(Meas.tobs), func.max(Meas.tobs), func.avg(Meas.tobs)).\
                         filter(Meas.date.between (u_start_date,u_end_date)).\
                         filter(Meas.station == 'USC00519281').all()
    session.close()

 # Create a dictionary from the row data and append to a list of start end temp results
    start_end_temp_results = []

    for min, max, avg in act_sta_temp_sande:
        temp_bse = {}
        temp_bse["min"] = min
        temp_bse["max"] = max
        temp_bse["avg"] = avg
        start_end_temp_results.append(temp_bse)

    return jsonify(start_end_temp_results)

if __name__ == '__main__':
    app.run(debug=True)



