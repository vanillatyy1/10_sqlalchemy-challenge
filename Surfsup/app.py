# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")

def route():
    """List all available api routes."""
    return (
        f"<b>Available Routes: </b> <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start date (yyyy-mm-dd)<br/>"
        f"example /api/v1.0/2015-09-18<br/>"
        f"/api/v1.0/start date (yyyy-mm-dd)/end date (yyyy-mm-dd)<br/>"  
        f"example /api/v1.0/2015-09-18/2017-03-13<br/>"
    )

## Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
## Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")

def prcp_last_year():
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    result = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= query_date).all()
    session.close()

    return_data = []

    for date, prcp in result:
        append_data = {}
        append_data["date"] = date
        append_data["prcp"] = prcp
        return_data.append(append_data)
    
    return jsonify(return_data)



## Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")

def stations():
    session = Session(engine)

    result = session.query(station.station).all()

    session.close()

    all_stations = list(np.ravel(result))
    
    return jsonify(all_stations)


## Query the dates and temperature observations of the most-active station for the previous year of data.
## Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")

def active_station():

    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    mactive_station = session.query(measurement.date, measurement.tobs).\
        filter(measurement.station == "USC00519281").filter(measurement.date >= query_date).all()
    session.close()

    return_data = []

    for date, tobs in mactive_station:
        append_data = {}
        append_data["date"] = date
        append_data["tobs"] = tobs
        return_data.append(append_data)
    
    return jsonify(return_data)


## Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
## For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
## For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/<start>")

def start_date(start):

    session = Session(engine)

    result = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()
    session.close()
    
    return_data = []

    for min_tobs, avg_tobs, max_tobs in result:
        append_data = {}
        append_data["minimum temperature"] = min_tobs
        append_data["average temperature"] = avg_tobs
        append_data["maximum temperature"] = max_tobs
        return_data.append(append_data)
    
    return jsonify(return_data)
    


@app.route("/api/v1.0/<start>/<end>")

def start_end(start, end):

    session = Session(engine)

    result = session.query(func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)).\
        filter(measurement.date >= start).filter(measurement.date < end).all()
    session.close()
    
    return_data = []

    for min_tobs, avg_tobs, max_tobs in result:
        append_data = {}
        append_data["minimum temperature"] = min_tobs
        append_data["average temperature"] = avg_tobs
        append_data["maximum temperature"] = max_tobs
        return_data.append(append_data)
    
    return jsonify(return_data)

if __name__ == '__main__':
    app.run(debug=True) 