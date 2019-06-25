import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/statecancerdata.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
state_data = Base.classes.statedata
cancer_data = Base.classes.incidence



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/api/statecolumns")
def statecolumns():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(state_data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/api/incidencecolumns")
def incidencecolumns():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(cancer_data).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/api/state")
def state():

    # Query all state info
    results = db.session.query(state_data.state_name, state_data.year, 
    	state_data.Smoker, state_data.Obese, state_data.Food_Environment_Index, 
    	state_data.Alcohol, state_data.Mammogram, state_data.Unemployment, 
    	state_data.Air_Polution, state_data.Population).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    state_info = []
    for state_name, year, Smoker, Obese, Food_Environment_Index, Alcohol, Mammogram, Unemployment, Air_Polution, Population in results:
        state_dict = {}
        state_dict["State name"] = state_name
        state_dict["year"] = year
        state_dict["Smoker"] = Smoker
        state_dict["Obese"] = Obese
        state_dict["Food Environment Index"] = Food_Environment_Index
        state_dict["Alcohol"] = Alcohol
        state_dict["Mammogram"] = Mammogram
        state_dict["Unemployment"] = Unemployment
        state_dict["Air Polution"] = Air_Polution
        state_dict["Population"] = Population
        state_info.append(state_dict)

    return jsonify(state_info)

@app.route("/api/incidence")
def incidence():

    # Query all cancers counts
    results = db.session.query(cancer_data.State_name, cancer_data.Bladder_count, 
    	cancer_data.Brain_count, cancer_data.Breast_count, cancer_data.Breastinsitu_count, cancer_data.Cervix_count,
    	cancer_data.colon_rectum_count, cancer_data.Esophagus_count,
    	cancer_data.Kidney_count, cancer_data.Leukemia_count, cancer_data.Liver_count, cancer_data.Lung_count, 
    	cancer_data.Melanoma_count, cancer_data.NonHodgkinL_count,
    	cancer_data.Oral_Pharynx_count, cancer_data.Ovary_count, cancer_data.Pancreas_count, cancer_data.Prostate_count,
    	cancer_data.Stomach_count, cancer_data.Thyroid_count, cancer_data.Uterus_count).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    cancer_counts = []
    for State_name, Bladder_count, Brain_count, Breast_count, Breastinsitu_count, Cervix_count, colon_rectum_count, Esophagus_count, Kidney_count, Leukemia_count, Liver_count, Lung_count, Melanoma_count, NonHodgkinL_count, Oral_Pharynx_count,Ovary_count, Pancreas_count, Prostate_count, Stomach_count, Thyroid_count, Uterus_count in results:
        cancer_dict = {}
        cancer_dict["State"] = State_name
        cancer_dict["Bladder cancer incidence"] = Bladder_count
        cancer_dict["Brain cancer incidence"] = Brain_count
        cancer_dict["Breast cancer incidence"] = Breast_count
        cancer_dict["Breastinsitu cancer incidence"] = Breastinsitu_count
        cancer_dict["Cervix cancer incidence"] = Cervix_count
        cancer_dict["colon rectum cancer incidence"] = colon_rectum_count
        cancer_dict["Esophagus cancer incidence"] = Esophagus_count
        cancer_dict["Kidney cancer incidence"] = Kidney_count
        cancer_dict["Leukemia cancer incidence"] = Leukemia_count
        cancer_dict["Liver cancer incidence"] = Liver_count
        cancer_dict["Lung cancer incidence"] = Lung_count
        cancer_dict["Melanoma cancer incidence"] = Melanoma_count
        cancer_dict["NonHodgkinL cancer incidence"] = NonHodgkinL_count
        cancer_dict["Oral_Pharynx cancer incidence"] = Oral_Pharynx_count
        cancer_dict["Ovary cancer incidence"] = Ovary_count
        cancer_dict["Pancreas cancer incidence"] = Pancreas_count
        cancer_dict["Prostate cancer incidence"] = Prostate_count
        cancer_dict["Stomach cancer incidence"] = Stomach_count
        cancer_dict["Thyroid cancer incidence"] = Thyroid_count
        cancer_dict["Uterus cancer incidence"] = Uterus_count
        cancer_counts.append(cancer_dict)

    return jsonify(cancer_counts)




if __name__ == "__main__":
    app.run()
