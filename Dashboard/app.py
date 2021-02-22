from flask import Flask, request, render_template, redirect,jsonify,render_template
app = Flask(__name__)

#Imnport Initial Dependencies

import sqlite3
import pandas as pd
import numpy as np

#retrieve data from SQLite DB

conn = sqlite3.connect(r'C:\Users\wvill\Documents\GitHub\DABProject3\Dashboard\resources\wine_quality.db')
query = 'Select * from wine_quality'
df = pd.read_sql_query(query,conn)
conn.close()

#Set Y
y = df.categorical_quality
y = y.values.reshape(-1,1)

#Set X
X = df.drop('categorical_quality', axis=1).values

#Import Test Train Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

#Scale Values
from sklearn.preprocessing import StandardScaler
scl=StandardScaler()
scl.fit_transform(X,y)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
#Random Forest
from sklearn.ensemble import RandomForestClassifier

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lrmodel', methods=['POST'])
def lrmodel():

    #Create and Train Logistic Regression Model

    lr=LogisticRegression()
    lr.fit(X_train,y_train.ravel())

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
    result = lr.predict(input)
    return jsonify({'result': result}), 200 # return success

@app.route('/rfmodel', methods=['POST'])
def rdmodel():

    # Create and Fit Random Forest Model

    rfc_r=RandomForestClassifier(n_estimators=500,criterion='entropy',max_features=6,max_depth=10,random_state=42)
    rfc_r.fit(X_train,y_train.ravel())
   
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
    result = rfc_r.predict(input)
    return jsonify({'result': result}), 200 # return success

    if __name__ == "__main__":
        app.run(debug=True)