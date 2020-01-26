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
pg_password = 'postgres:postgres'

#Define PostgreSQL Database Engine
engine = create_engine('postgresql://' + pg_password + '@localhost:5432/fast_food_db')

#Define Path for USA Fast Food Route
@app.route('/', methods = ['GET'])

#Define Function for Dashboard Content
def api_home():

    #Import USA Fast Food Data Table from SQL DB as Pandas Data Frame
    USA_food = pd.read_sql('SELECT * FROM "USA_Fast_Food"', engine)

    #Convert Data Frame to Dictionary & Convert Dictionary to JSON Object
    full_data = json.dumps(USA_food.to_dict(orient='records'), indent = 2)

    #Add JSON Object to Dictionary
    data = {'chart_data': full_data}
    
    #Call HTML File & Pass in Dictionary with JSON Object
    return render_template("index_data.html", data = data)

#Define Path for State Fast Food Routes
@app.route('/<state>', methods = ['GET'])

#Define Function for Dashboard Content
def api_state(state):

    #Create Variable for SQL DB Table Data & Assign Default Value of Blank Data Frame
    state_food = pd.DataFrame()

    #Set Condition for Alabama Route
    if state.upper() == "AL":

        #Import Alabama Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "AL_Fast_Food"', engine)

    #Set Condition for Alaska Route
    elif state.upper() == "AK":

        #Import Alaska Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "AK_Fast_Food"', engine)

    #Set Condition for Arizona Route
    elif state.upper() == "AZ":

        #Import Arizona Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "AZ_Fast_Food"', engine)

    #Set Condition for Arkansas Route
    elif state.upper() == "AR":

        #Import Arkansas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "AR_Fast_Food"', engine)

    #Set Condition for California Route
    elif state.upper() == "CA":

        #Import California Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "CA_Fast_Food"', engine)

    #Set Condition for Colorado Route
    elif state.upper() == "CO":

        #Import Colorado Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "CO_Fast_Food"', engine)

    #Set Condition for Conneticut Route
    elif state.upper() == "CT":

        #Import Connecticut Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "CT_Fast_Food"', engine)

    #Set Condition for Washington DC Route
    elif state.upper() == "DC":

        #Import Washington DC Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "DC_Fast_Food"', engine)

    #Set Condition for Delaware Route
    elif state.upper() == "DE":

        #Import Delaware Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "DE_Fast_Food"', engine)

    #Set Condition for Florida Route
    elif state.upper() == "FL":

        #Import Florida Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "FL_Fast_Food"', engine)

    #Set Condition for Georgia Route
    elif state.upper() == "GA":

        #Import Georgia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "GA_Fast_Food"', engine)

    #Set Condition for Hawaii Route
    elif state.upper() == "HI":

        #Import Hawaii Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "HI_Fast_Food"', engine)

    #Set Condition for Idaho Route
    elif state.upper() == "ID":

        #Import Idaho Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "ID_Fast_Food"', engine)

    #Set Condition for Illinois Route
    elif state.upper() == "IL":

        #Import Illinois Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "IL_Fast_Food"', engine)

    #Set Condition for Indiana Route
    elif state.upper() == "IN":

        #Import Indiana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "IN_Fast_Food"', engine)

    #Set Condition for Iowa Route
    elif state.upper() == "IA":

        #Import Iowa Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "IA_Fast_Food"', engine)

    #Set Condition for Kansas Route
    elif state.upper() == "KS":

        #Import Kansas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "KS_Fast_Food"', engine)

    #Set Condition for Kentucky Route
    elif state.upper() == "KY":

        #Import Kentucky Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "KY_Fast_Food"', engine)

    #Set Condition for Louisiana Route
    elif state.upper() == "LA":

        #Import Louisiana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "LA_Fast_Food"', engine)

    #Set Condition for Maine Route
    elif state.upper() == "ME":

        #Import Maine Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "ME_Fast_Food"', engine)

    #Set Condition for Maryland Route
    elif state.upper() == "MD":

        #Import Maryland Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MD_Fast_Food"', engine)

    #Set Condition for Massachusetts Route
    elif state.upper() == "MA":

        #Import Massachusetts Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MA_Fast_Food"', engine)

    #Set Condition for Michigan Route
    elif state.upper() == "MI":

        #Import Michigan Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MI_Fast_Food"', engine)

    #Set Condition for Minnesota Route
    elif state.upper() == "MN":

        #Import Minnesota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MN_Fast_Food"', engine)

    #Set Condition for Mississippi Route 
    elif state.upper() == "MS":

        #Import Mississippi Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MS_Fast_Food"', engine)

    #Set Condition for Missouri Route
    elif state.upper() == "MO":

        #Import Missouri Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MO_Fast_Food"', engine)

    #Set Condiiton for Montana Route 
    elif state.upper() == "MT":

        #Import Montana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "MT_Fast_Food"', engine)

    #Set Condition for Nebraska Route
    elif state.upper() == "NE":

        #Import Nebraska Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NE_Fast_Food"', engine)

    #Set Condition for Nevada Route
    elif state.upper() == "NV":

        #Import Nevada Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NV_Fast_Food"', engine)

    #Set Condition for New Hampshire Route
    elif state.upper() == "NH":

        #Import New Hampshire Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NH_Fast_Food"', engine)

    #Set Condition for New Jersey Route
    elif state.upper() == "NJ":

        #Import New Jersey Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NJ_Fast_Food"', engine)

    #Set Condition for New Mexico Route
    elif state.upper() == "NM":

        #Import New Mexico Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NM_Fast_Food"', engine)

    #Set Condition for New York Route
    elif state.upper() == "NY":

        #Import New York Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NY_Fast_Food"', engine)

    #Set Condition for North Carolina Route
    elif state.upper() == "NC":

        #Import North Carolina Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "NC_Fast_Food"', engine)

    #Set Condition North Dakota Route
    elif state.upper() == "ND":

        #Import North Dakota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "ND_Fast_Food"', engine)

    #Set Condition for Ohio Route
    elif state.upper() == "OH":

        #Import Ohio Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "OH_Fast_Food"', engine)
    
    #Set Condition for Oklahoma Route
    elif state.upper() == "OK":

        #Import Oklahoma Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "OK_Fast_Food"', engine)

    #Set Condition for Oregon Route
    elif state.upper() == "OR":

        #Import Oregon Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "OR_Fast_Food"', engine)

    #Set Condition for Pennsylvania Route
    elif state.upper() == "PA":

        #Import Pennsylvania Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "PA_Fast_Food"', engine)

    #Set Condition for Rhode Island Route
    elif state.upper() == "RI":

        #Import Rhode Island Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "RI_Fast_Food"', engine)

    #Set Condition for South Carolina Route
    elif state.upper() == "SC":

        #Import South Carolina Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "SC_Fast_Food"', engine)

    #Set Condition for South Dakota Route
    elif state.upper() == "SD":

        #Import South Dakota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "SD_Fast_Food"', engine)

    #Set Condition for Tennessee Route
    elif state.upper() == "TN":

        #Import Tennessee Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "TN_Fast_Food"', engine)

    #Set Condition for Texas Route
    elif state.upper() == "TX":

        #Import Texas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "TX_Fast_Food"', engine)

    #Set Condition for Utah Route
    elif state.upper() == "UT":

        #Import Utah Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "UT_Fast_Food"', engine)

    #Set Condition for Vermont Route
    elif state.upper() == "VT":

        #Import Vermont Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "VT_Fast_Food"', engine)
    
    #Set Condition for Virginia Route
    elif state.upper() == "VA":

        #Import Virginia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "VA_Fast_Food"', engine)
    
    #Set Condition for Washington Route
    elif state.upper() == "WA":

        #Import Washington Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "WA_Fast_Food"', engine)

    #Set Condition for West Virginia Route
    elif state.upper() == "WV":

        #Import West Virginia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "WV_Fast_Food"', engine)

    #Set Condition for Wisconsin Route
    elif state.upper() == "WI":

        #Import Wisconsin Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "WI_Fast_Food"', engine)

    #Set Condition for Wyoming Route
    elif state.upper() == "WY":

        #Import Wyoming Fast Food Data Table from SQL DB as Pandas Data Frame
        state_food = pd.read_sql('SELECT * FROM "WY_Fast_Food"', engine)

    #Set Condition for Empty Data Frame
    if state_food.empty == True:

        #Call HTML File & Pass in Dictionary with JSON Object
        return render_template("index_blank.html")
    else:

        #Convert Data Frame to Dictionary & Dictionary to JSON Object
        partial_data = json.dumps(state_food.to_dict(orient='records'), indent = 2)

        #Add JSON Object to Dictionary
        data = {'chart_data': partial_data}

        #Call HTML File & Pass in Dictionary with JSON Object
        return render_template("index_data.html", data = data)

#Define Function for USA Map Route
@app.route('/map', methods = ['GET'])

#Define Function for Map Content
def api_map():

    #Import USA Fast Food Data Table from SQL DB as Pandas Data Frame
    USA_map = pd.read_sql('SELECT * FROM "USA_Fast_Food"', engine)

    #Convert Data Frame to Dictionary & Dictionary to JSON Object
    full_map = json.dumps(USA_map.to_dict(orient='records'), indent = 2)

    #Add JSON Object to Dictionary
    data = {'chart_data': full_map}

    #Cll HTML File & Pass in Dictionary with JSON Object
    return render_template("index_map.html", data = data)

#Define Function for State Map Routes
@app.route('/map/<state>', methods = ['GET'])

#Define Function for Map Content
def api_local(state):

    #Create Variable for SQL DB Table Data & Assign Default Value of Blank Data Frame
    state_map = pd.DataFrame()

    #Set Condition for Alabama Route
    if state.upper() == "AL":

        #Import Alabama Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "AL_Fast_Food"', engine)

    #Set Condition for Alaska Route
    elif state.upper() == "AK":

        #Import Alaska Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "AK_Fast_Food"', engine)

    #Set Condition for Arizona Route
    elif state.upper() == "AZ":

        #Import Arizona Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "AZ_Fast_Food"', engine)

    #Set Condition for Arkansas Route
    elif state.upper() == "AR":

        #Import Arkansas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "AR_Fast_Food"', engine)

    #Set Condition for California Route
    elif state.upper() == "CA":

        #Import California Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "CA_Fast_Food"', engine)

    #Set Condition for Colorado Route
    elif state.upper() == "CO":

        #Import Colorado Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "CO_Fast_Food"', engine)

    #Set Condition for Conneticut Route
    elif state.upper() == "CT":

        #Import Connecticut Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "CT_Fast_Food"', engine)

    #Set Condition for Washington DC Route
    elif state.upper() == "DC":

        #Import Washington DC Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "DC_Fast_Food"', engine)

    #Set Condition for Delaware Route
    elif state.upper() == "DE":

        #Import Delaware Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "DE_Fast_Food"', engine)

    #Set Condition for Florida Route
    elif state.upper() == "FL":

        #Import Florida Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "FL_Fast_Food"', engine)

    #Set Condition for Georgia Route
    elif state.upper() == "GA":

        #Import Georgia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "GA_Fast_Food"', engine)

    #Set Condition for Hawaii Route
    elif state.upper() == "HI":

        #Import Hawaii Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "HI_Fast_Food"', engine)

    #Set Condition for Idaho Route
    elif state.upper() == "ID":

        #Import Idaho Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "ID_Fast_Food"', engine)

    #Set Condition for Illinois Route
    elif state.upper() == "IL":

        #Import Illinois Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "IL_Fast_Food"', engine)

    #Set Condition for Indiana Route
    elif state.upper() == "IN":

        #Import Indiana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "IN_Fast_Food"', engine)

    #Set Condition for Iowa Route
    elif state.upper() == "IA":

        #Import Iowa Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "IA_Fast_Food"', engine)

    #Set Condition for Kansas Route
    elif state.upper() == "KS":

        #Import Kansas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "KS_Fast_Food"', engine)

    #Set Condition for Kentucky Route
    elif state.upper() == "KY":

        #Import Kentucky Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "KY_Fast_Food"', engine)

    #Set Condition for Louisiana Route
    elif state.upper() == "LA":

        #Import Louisiana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "LA_Fast_Food"', engine)

    #Set Condition for Maine Route
    elif state.upper() == "ME":

        #Import Maine Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "ME_Fast_Food"', engine)

    #Set Condition for Maryland Route
    elif state.upper() == "MD":

        #Import Maryland Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MD_Fast_Food"', engine)

    #Set Condition for Massachusetts Route
    elif state.upper() == "MA":

        #Import Massachusetts Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MA_Fast_Food"', engine)

    #Set Condition for Michigan Route
    elif state.upper() == "MI":

        #Import Michigan Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MI_Fast_Food"', engine)

    #Set Condition for Minnesota Route
    elif state.upper() == "MN":

        #Import Minnesota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MN_Fast_Food"', engine)

    #Set Condition for Mississippi Route 
    elif state.upper() == "MS":

        #Import Mississippi Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MS_Fast_Food"', engine)

    #Set Condition for Missouri Route
    elif state.upper() == "MO":

        #Import Missouri Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MO_Fast_Food"', engine)

    #Set Condiiton for Montana Route 
    elif state.upper() == "MT":

        #Import Montana Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "MT_Fast_Food"', engine)

    #Set Condition for Nebraska Route
    elif state.upper() == "NE":

        #Import Nebraska Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NE_Fast_Food"', engine)

    #Set Condition for Nevada Route
    elif state.upper() == "NV":

        #Import Nevada Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NV_Fast_Food"', engine)

    #Set Condition for New Hampshire Route
    elif state.upper() == "NH":

        #Import New Hampshire Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NH_Fast_Food"', engine)

    #Set Condition for New Jersey Route
    elif state.upper() == "NJ":

        #Import New Jersey Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NJ_Fast_Food"', engine)

    #Set Condition for New Mexico Route
    elif state.upper() == "NM":

        #Import New Mexico Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NM_Fast_Food"', engine)

    #Set Condition for New York Route
    elif state.upper() == "NY":

        #Import New York Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NY_Fast_Food"', engine)

    #Set Condition for North Carolina Route
    elif state.upper() == "NC":

        #Import North Carolina Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "NC_Fast_Food"', engine)

    #Set Condition North Dakota Route
    elif state.upper() == "ND":

        #Import North Dakota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "ND_Fast_Food"', engine)

    #Set Condition for Ohio Route
    elif state.upper() == "OH":

        #Import Ohio Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "OH_Fast_Food"', engine)
    
    #Set Condition for Oklahoma Route
    elif state.upper() == "OK":

        #Import Oklahoma Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "OK_Fast_Food"', engine)

    #Set Condition for Oregon Route
    elif state.upper() == "OR":

        #Import Oregon Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "OR_Fast_Food"', engine)

    #Set Condition for Pennsylvania Route
    elif state.upper() == "PA":

        #Import Pennsylvania Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "PA_Fast_Food"', engine)

    #Set Condition for Rhode Island Route
    elif state.upper() == "RI":

        #Import Rhode Island Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "RI_Fast_Food"', engine)

    #Set Condition for South Carolina Route
    elif state.upper() == "SC":

        #Import South Carolina Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "SC_Fast_Food"', engine)

    #Set Condition for South Dakota Route
    elif state.upper() == "SD":

        #Import South Dakota Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "SD_Fast_Food"', engine)

    #Set Condition for Tennessee Route
    elif state.upper() == "TN":

        #Import Tennessee Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "TN_Fast_Food"', engine)

    #Set Condition for Texas Route
    elif state.upper() == "TX":

        #Import Texas Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "TX_Fast_Food"', engine)

    #Set Condition for Utah Route
    elif state.upper() == "UT":

        #Import Utah Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "UT_Fast_Food"', engine)

    #Set Condition for Vermont Route
    elif state.upper() == "VT":

        #Import Vermont Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "VT_Fast_Food"', engine)
    
    #Set Condition for Virginia Route
    elif state.upper() == "VA":

        #Import Virginia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "VA_Fast_Food"', engine)
    
    #Set Condition for Washington Route
    elif state.upper() == "WA":

        #Import Washington Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "WA_Fast_Food"', engine)

    #Set Condition for West Virginia Route
    elif state.upper() == "WV":

        #Import West Virginia Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "WV_Fast_Food"', engine)

    #Set Condition for Wisconsin Route
    elif state.upper() == "WI":

        #Import Wisconsin Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "WI_Fast_Food"', engine)

    #Set Condition for Wyoming Route
    elif state.upper() == "WY":

        #Import Wyoming Fast Food Data Table from SQL DB as Pandas Data Frame
        state_map = pd.read_sql('SELECT * FROM "WY_Fast_Food"', engine)

    #Set Condition for Empty Data Frame
    if state_map.empty == True:

        #Call HTML File & Pass in State Name
        return render_template("index_empty.html", data = {'name': state})
    else:

        #Convert Data Frame to Dictionary & Dictionary to JSON Object
        partial_map = json.dumps(state_map.to_dict(orient='records'), indent = 2)

        #Add JSON Object to Dictionary
        data = {'chart_data': partial_map}

        #Call HTML File & Pass in Dictionary with JSON Object
        return render_template("index_map.html", data = data)

#Initialize Flask App
app.run()