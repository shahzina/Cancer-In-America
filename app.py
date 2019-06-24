import pandas as pd
import geojson

from flask import (
    Flask,
    render_template,
    jsonify)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/cancer.sqlite"

db = SQLAlchemy(app)


class Cancer(db.Model):


    __tablename__ = 'incidence'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    bladder_count = db.Column(db.Integer)
    bladder_rate = db.Column(db.Numeric)
    brain_count = db.Column(db.Integer)
    brain_rate = db.Column(db.Numeric)
    breast_count = db.Column(db.Integer)
    breast_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    cervix_count = db.Column(db.Integer)
    cervix_rate = db.Column(db.Numeric)
    child_less_15_count = db.Column(db.Integer)
    child_less_15_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)
    db.Colon_rectum_count = db.Column(db.Integer)
    db.Colon_rectum_rate = db.Column(db.Numeric)
    esophagus_count = db.Column(db.Integer)
    esophagus_rate = db.Column(db.Numeric)
    kidney_count = db.Column(db.Integer)
    kidney_rate = db.Column(db.Numeric)
    leukemia_count = db.Column(db.Integer)
    leukemia_rate = db.Column(db.Numeric)
    liver_count = db.Column(db.Integer)
    liver_rate = db.Column(db.Numeric)
    lung_count = db.Column(db.Integer)
    lung_rate = db.Column(db.Numeric)
    melanoma_count = db.Column(db.Integer)
    melanoma_rate = db.Column(db.Numeric)
    non_HodgkinL_count = db.Column(db.Integer)
    non_HodgkinL_rate = db.Column(db.Numeric)
    oral_pharynx_count = db.Column(db.Integer)
    oral_pharynx_rate = db.Column(db.Numeric)
    ovary_count = db.Column(db.Integer)
    ovary_rate = db.Column(db.Numeric)
    pancreas_count = db.Column(db.Integer)
    pancreas_rate = db.Column(db.Numeric)
    prostate_count = db.Column(db.Integer)
    prostate_rate = db.Column(db.Numeric)
    stomach_count = db.Column(db.Integer)
    stomach_rate = db.Column(db.Numeric)
    thyroid_count = db.Column(db.Integer)
    thyroid_rate = db.Column(db.Numeric)
    uterus_count = db.Column(db.Integer)
    uterus_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)


    __tablename__ = 'mortality'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    bladder_count = db.Column(db.Integer)
    bladder_rate = db.Column(db.Numeric)
    brain_count = db.Column(db.Integer)
    brain_rate = db.Column(db.Numeric)
    breast_count = db.Column(db.Integer)
    breast_rate = db.Column(db.Numeric)
    breast_insitu_count = db.Column(db.Integer)
    breast_insitu_rate = db.Column(db.Numeric)
    cervix_count = db.Column(db.Integer)
    cervix_rate = db.Column(db.Numeric)
    child_less_15_count = db.Column(db.Integer)
    child_less_15_rate = db.Column(db.Numeric)
    child_less_20_count = db.Column(db.Integer)
    child_less_20_rate = db.Column(db.Numeric)
    db.Colon_rectum_count = db.Column(db.Integer)
    db.Colon_rectum_rate = db.Column(db.Numeric)
    esophagus_count = db.Column(db.Integer)
    esophagus_rate = db.Column(db.Numeric)
    kidney_count = db.Column(db.Integer)
    kidney_rate = db.Column(db.Numeric)
    leukemia_count = db.Column(db.Integer)
    leukemia_rate = db.Column(db.Numeric)
    liver_count = db.Column(db.Integer)
    liver_rate = db.Column(db.Numeric)
    lung_count = db.Column(db.Integer)
    lung_rate = db.Column(db.Numeric)
    melanoma_count = db.Column(db.Integer)
    melanoma_rate = db.Column(db.Numeric)
    non_HodgkinL_count = db.Column(db.Integer)
    non_HodgkinL_rate = db.Column(db.Numeric)
    oral_pharynx_count = db.Column(db.Integer)
    oral_pharynx_rate = db.Column(db.Numeric)
    ovary_count = db.Column(db.Integer)
    ovary_rate = db.Column(db.Numeric)
    pancreas_count = db.Column(db.Integer)
    pancreas_rate = db.Column(db.Numeric)
    prostate_count = db.Column(db.Integer)
    prostate_rate = db.Column(db.Numeric)
    stomach_count = db.Column(db.Integer)
    stomach_rate = db.Column(db.Numeric)
    thyroid_count = db.Column(db.Integer)
    thyroid_rate = db.Column(db.Numeric)
    uterus_count = db.Column(db.Integer)
    uterus_rate = db.Column(db.Numeric)


    __tablename__ = 'census'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    crowding_count = db.Column(db.Integer)
    crowding_percent = db.Column(db.Numeric)
    education_bachelors_count = db.Column(db.Integer)
    education_bachelors_percent = db.Column(db.Numeric)
    median_family_income_dollars = db.Column(db.Integer)
    uninsured_count = db.Column(db.Integer)
    uninsured_percent = db.Column(db.Numeric)
    below_150_poverty_count = db.Column(db.Integer)
    below_150_poverty_percent = db.Column(db.Numeric)
    unemployed_count = db.Column(db.Integer)
    unemployed_percent = db.Column(db.Numeric)


    __tablename__ = 'risk'
    State_code = db.Column(db.String(255))
    State = db.Column(db.String(255), primary_key=True)
    FIPS = db.Column(db.Integer)
    smokers_count = db.Column(db.Integer)
    smokers_percent = db.Column(db.Numeric)
    veggie_count = db.Column(db.Integer)
    veggies_percent = db.Column(db.Numeric)
    fruit_count = db.Column(db.Integer)
    fruit_percent = db.Column(db.Numeric)
    overweight_BMI_count = db.Column(db.Integer)
    overweight_BMI_percent = db.Column(db.Numeric)
    obese_BMI_highschool_count = db.Column(db.Integer)
    obese_BMI_highschool_percent = db.Column(db.Numeric)
    obese_BMI_20_plus_count = db.Column(db.Integer)
    obese_BMI_20_plus_percent = db.Column(db.Numeric)
    healthy_BMI_20_plus_count = db.Column(db.Integer)
    healthy_BMI_20_plus_percent = db.Column(db.Numeric)
    no_physical_activity_count = db.Column(db.Integer)
    no_physical_activity_percent = db.Column(db.Numeric)

    def __repr__(self):
        return '<CancerMap %r>' % (self.name)


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


##########################################################
 #                   The Routes
##########################################################

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/pie")
def pie():
    return render_template("state_pie.html")


@app.route("/top5incd")
def top5incd():
    return render_template("topfiveIncidence.html")


@app.route("/top5mort")
def top5mort():
    return render_template("topfiveMortality.html")


@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/map-data_incd")
def map_data_incd():

    df = pd.read_sql_table("incidence", "sqlite:///data/cancer.sqlite")
    df.set_index(['State'])

    #df.to_json(orient='index')
    data = []
    Dict = {}
    c = 0
    for i, row in df.iterrows():
        data.append({

            'State': row["State"],

        })

    

    return jsonify(data)

