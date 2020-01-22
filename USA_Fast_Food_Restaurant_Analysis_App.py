#Import Modules
import flask
from flask import request, jsonify, render_template, redirect, url_for
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from statistics import mean
import json

#Define Flask App Environment
app = flask.Flask(__name__, template_folder = 'C:/Users/mjknj/Desktop/UNCC/Projects/Project 2/MK Test Files/')
app.config["DEBUG"] = True

#Define Variable for Postgres Password
pg_password = ''

#Define PostgreSQL Database Engine
engine = create_engine('postgresql://' + pg_password + '@localhost:5432/fast_food_db')

#Define Path for App Home Screen
@app.route('/', methods = ['GET'])

#Define Function for Home Screen Content
def api_home():

    USA_food = pd.read_sql('SELECT * FROM "USA_Fast_Food"', engine)

    full_data = json.dumps(USA_food.to_dict(orient='records'), indent = 2)

    data = {'chart_data': full_data}

    return render_template("index_data.html", data = data)

@app.route('/<state>', methods = ['GET'])

def api_state(state):

    state_food = pd.DataFrame()

    if state == "AL":
        state_food = pd.read_sql('SELECT * FROM "AL_Fast_Food"', engine)
    elif state == "AK":
        state_food = pd.read_sql('SELECT * FROM "AK_Fast_Food"', engine)
    elif state == "AZ":
        state_food = pd.read_sql('SELECT * FROM "AZ_Fast_Food"', engine)
    elif state == "AR":
        state_food = pd.read_sql('SELECT * FROM "AR_Fast_Food"', engine)
    elif state == "CA":
        state_food = pd.read_sql('SELECT * FROM "CA_Fast_Food"', engine)
    elif state == "CO":
        state_food = pd.read_sql('SELECT * FROM "CO_Fast_Food"', engine)
    elif state == "CT":
        state_food = pd.read_sql('SELECT * FROM "CT_Fast_Food"', engine)
    elif state == "DE":
        state_food = pd.read_sql('SELECT * FROM "DE_Fast_Food"', engine)
    elif state == "FL":
        state_food = pd.read_sql('SELECT * FROM "FL_Fast_Food"', engine)
    elif state == "GA":
        state_food = pd.read_sql('SELECT * FROM "GA_Fast_Food"', engine)
    elif state == "HI":
        state_food = pd.read_sql('SELECT * FROM "HI_Fast_Food"', engine)
    elif state == "ID":
        state_food = pd.read_sql('SELECT * FROM "ID_Fast_Food"', engine)
    elif state == "IL":
        state_food = pd.read_sql('SELECT * FROM "IL_Fast_Food"', engine)
    elif state == "IN":
        state_food = pd.read_sql('SELECT * FROM "IN_Fast_Food"', engine)
    elif state == "IA":
        state_food = pd.read_sql('SELECT * FROM "IA_Fast_Food"', engine)
    elif state == "KS":
        state_food = pd.read_sql('SELECT * FROM "KS_Fast_Food"', engine)
    elif state == "KY":
        state_food = pd.read_sql('SELECT * FROM "KY_Fast_Food"', engine)
    elif state == "LA":
        state_food = pd.read_sql('SELECT * FROM "LA_Fast_Food"', engine)
    elif state == "ME":
        state_food = pd.read_sql('SELECT * FROM "ME_Fast_Food"', engine)
    elif state == "MD":
        state_food = pd.read_sql('SELECT * FROM "MD_Fast_Food"', engine)
    elif state == "MA":
        state_food = pd.read_sql('SELECT * FROM "MA_Fast_Food"', engine)
    elif state == "MI":
        state_food = pd.read_sql('SELECT * FROM "MI_Fast_Food"', engine)
    elif state == "MN":
        state_food = pd.read_sql('SELECT * FROM "MN_Fast_Food"', engine)
    elif state == "MS":
        state_food = pd.read_sql('SELECT * FROM "MS_Fast_Food"', engine)
    elif state == "MO":
        state_food = pd.read_sql('SELECT * FROM "MO_Fast_Food"', engine)
    elif state == "MT":
        state_food = pd.read_sql('SELECT * FROM "MT_Fast_Food"', engine)
    elif state == "NE":
        state_food = pd.read_sql('SELECT * FROM "NE_Fast_Food"', engine)
    elif state == "NV":
        state_food = pd.read_sql('SELECT * FROM "NV_Fast_Food"', engine)
    elif state == "NH":
        state_food = pd.read_sql('SELECT * FROM "NH_Fast_Food"', engine)
    elif state == "NJ":
        state_food = pd.read_sql('SELECT * FROM "NJ_Fast_Food"', engine)
    elif state == "NM":
        state_food = pd.read_sql('SELECT * FROM "NM_Fast_Food"', engine)
    elif state == "NY":
        state_food = pd.read_sql('SELECT * FROM "NJ_Fast_Food"', engine)
    elif state == "NC":
        state_food = pd.read_sql('SELECT * FROM "NC_Fast_Food"', engine)
    elif state == "ND":
        state_food = pd.read_sql('SELECT * FROM "ND_Fast_Food"', engine)
    elif state == "OH":
        state_food = pd.read_sql('SELECT * FROM "OH_Fast_Food"', engine)
    elif state == "OK":
        state_food = pd.read_sql('SELECT * FROM "OK_Fast_Food"', engine)
    elif state == "OR":
        state_food = pd.read_sql('SELECT * FROM "OR_Fast_Food"', engine)
    elif state == "PA":
        state_food = pd.read_sql('SELECT * FROM "PA_Fast_Food"', engine)
    elif state == "RI":
        state_food = pd.read_sql('SELECT * FROM "RI_Fast_Food"', engine)
    elif state == "SC":
        state_food = pd.read_sql('SELECT * FROM "SC_Fast_Food"', engine)
    elif state == "SD":
        state_food = pd.read_sql('SELECT * FROM "SD_Fast_Food"', engine)
    elif state == "TN":
        state_food = pd.read_sql('SELECT * FROM "TN_Fast_Food"', engine)
    elif state == "TX":
        state_food = pd.read_sql('SELECT * FROM "TX_Fast_Food"', engine)
    elif state == "UT":
        state_food = pd.read_sql('SELECT * FROM "UT_Fast_Food"', engine)
    elif state == "VT":
        state_food = pd.read_sql('SELECT * FROM "VT_Fast_Food"', engine)
    elif state == "VA":
        state_food = pd.read_sql('SELECT * FROM "VA_Fast_Food"', engine)
    elif state == "WA":
        state_food = pd.read_sql('SELECT * FROM "WA_Fast_Food"', engine)
    elif state == "WV":
        state_food = pd.read_sql('SELECT * FROM "WV_Fast_Food"', engine)
    elif state == "WI":
        state_food = pd.read_sql('SELECT * FROM "WI_Fast_Food"', engine)
    elif state == "WY":
        state_food = pd.read_sql('SELECT * FROM "WY_Fast_Food"', engine)

    if state_food.empty == True:
        return render_template("index_blank.html", data = state)
    else:
        partial_data = json.dumps(state_food.to_dict(orient='records'), indent = 2)

        data = {'chart_data': partial_data}

        return render_template("index_data.html", data = data)

@app.route('/map', methods = ['GET'])

def api_map():

    USA_food = pd.read_sql('SELECT * FROM "USA_Fast_Food"', engine)

    full_data = json.dumps(USA_food.to_dict(orient='records'), indent = 2)

    data = {'chart_data': full_data}

    return render_template("index_map.html", data = data)

#Initialize Flask App
app.run()