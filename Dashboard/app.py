from flask import Flask, request, render_template, redirect,jsonify,render_template
app = Flask(__name__)

import sqlite3
import pandas as pd
import numpy as np

#Import Enconder and Scaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

#Import Models 

#Logistic Regression
from sklearn.linear_model import LogisticRegression
#Random Forest
from sklearn.ensemble import RandomForestClassifier

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/model', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    input = {
        'VolatileAcidity': request.json['fieldA'],
        'ResidualSugar': request.json['fieldB'],
        'Chlorides': request.json['fieldC'],
        'Density': request.json['fieldD'],
        'pH': request.json['fieldE'],
        'Sulphates': request.json['fieldF'],
        'Alcohol': request.json['fieldG']
    }
    result = yourModel.predict(input)
    return jsonify({'result': result}), 200 # return success

    if __name__ == "__main__":
        app.run(debug=True)