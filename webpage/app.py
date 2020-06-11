from flask import Flask, render_template, request
from flask import Flask, request, jsonify, render_template
from flask import Flask, render_template, request
# import requests
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, inspect, func
import sqlite3 as sql
import pickle
import numpy as np

#################################################
# Database Setup - Housing Data
#################################################
# engine = create_engine("sqlite:///Resources/petdbUpdated.sqlite")

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# # Create a database session object.
# session = Session(engine)

# # Save a reference to the listings table as "Listings".
# Listings = Base.classes.listings

app = Flask(__name__)

# prediction function 
@app.route('/index')
def index():
    return render_template ("index.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")

@app.route('/')
def home():
    return render_template ("home.html")

def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 52) 
    loaded_model = pickle.load(open("rf_modelOneHot2.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values()) 
        new_list=list(map(lambda x: int(x.replace(",", "")), to_predict_list))

        zero_list = []
        for x in range(52):
            zero_list.append(0)
        for x in new_list:
            zero_list[x] = 1

        result = ValuePredictor(zero_list)       
        if result == 1: 
            outcome ='Accept'
        else: 
            outcome ='Expert Review Required'         
        return render_template("result.html", prediction = outcome) 

# @app.route('/enternew')
# def new_dog():
#    return render_template('dog_intake.html')

# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#     if request.method == 'POST':
#         try:
#             dog_color2 = request.form['PrimaryColor']
#             dog_category2 = request.form['BreedCategory']
#             dog_behavior2 = request.form['IntakeStatus']
#             dog_age2 = request.form['PetAgeCategory']
#             dog_sex2 = request.form['Sex']
#             dog_breed2 = request.form['PetBreed']
         
#             with sql.connect("petdatabase.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO dogTable (PrimaryColor, BreedCategory, IntakeStatus ,PetAgeCategory , Sex, TopBreed) VALUES (?,?,?,?,?,?)", (dog_color2, dog_category2, dog_behavior2, dog_age2, dog_sex2, dog_breed2) )
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.rollback()
#             msg = "error in insert operation"
      
#         finally:
#             return render_template("resultrec.html",msg = msg)
#             con.close()

# @app.route('/list')
# def list():
#    con = sql.connect("petdatabase.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from dogTable")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)