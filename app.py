from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

#Logistic Regression
from sklearn.linear_model import LogisticRegression

#Random Forest
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

#Import Logistic Regression Model
lrmodel=pickle.load(open('lrsommelier.pkl','rb'))

#Import Random Forest Model 
rfmodel=pickle.load(open('rfsommelier.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    lrprediction=lrmodel.predict(final)
    lrresult = ()
    rfresult = ()
    if lrprediction == 0:
        lrresult = "High"
    else:
        lrresult = "Low"
    rfprediction=rfmodel.predict(final)
    if rfprediction == 0:
        rfresult = "High"
    else:
        rfresult = "Low"

    return render_template('index.html',pred=f'The Quality of your wine is {lrresult} according to the Logistic Regression model and {rfresult} according to the Random Forest Classifier')

if __name__ == '__main__':
    app.run(debug=True)