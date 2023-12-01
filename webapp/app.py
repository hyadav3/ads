from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route('/')
def index():


    return render_template('home.html')

@app.route('/about')

def about():
    return render_template( 'about.html' )

@app.route('/contact')

def contact():
    return render_template( 'contact.html' )

@app.route('/descrptive')

def descrptive():
    return render_template( 'descrptive.html' )

@app.route('/prediction' , methods=['GET','POST'])

def prediction():

    if request.method == "POST": #if form was submitted
        # Variables summitted (needed for form redisplay)
        Pregnancies = request.form['Pregnancies']
        Glucose = request.form['Glucose']
        BloodPressure = request.form['BloodPressure']
        SkinThickness = request.form['SkinThickness']
        Insulin = request.form['Insulin']
        BMI = request.form['BMI']
        DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
        Age = request.form['Age']
 
        # creating the df for model prediction
        d = request.form.to_dict()
        df = pd.DataFrame([d.values()], columns=d.keys())
        #subsetting model (removes Input variables that are needed for the sliders)
        df=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']] 
        
        #load model
        loaded_model = pickle.load(open('best_svm_model.pkl', 'rb'))
        
        # predict diabetes probability
        prob=loaded_model.predict_proba(df)
        
        #turn predicton into text statement
        pred_prob="Your probability of diabetes is "+str(round(prob[0,1]*100))+"%."

        
    else:
        # If not submitted, set values to median
        Pregnancies=3
        Glucose=117
        BloodPressure=72
        SkinThickness=23
        Insulin=31
        BMI=32
        DiabetesPedigreeFunction=0.373
        Age=29
        pred_prob=""
    
    return render_template( 'prediction.html' ,  pred_prob=pred_prob, Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction, Age=Age, 
  )

