from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


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

    if request.method == "POST":
        Pregnancies = request.form['Pregnancies']
        Glucose = request.form['Glucose']
        BloodPressure = request.form['BloodPressure']
        SkinThickness = request.form['SkinThickness']
        Insulin = request.form['Insulin']
        BMI = request.form['BMI']
        DiabetesPedigreeFunction = request.form['DiabetesPedigreeFunction']
        Age = request.form['Age']
        pred_prob="Your predicted probability is X%"
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
        pred_prob="Here"
    
    return render_template( 'prediction.html' , pred_prob=pred_prob, Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction, Age=Age, 
  )

@app.route('/predictor', methods=['GET', 'POST'])

def predictor():
    age = request.args.get("Age", default=-1)
    
    return jsonify({'output':'Your Name is ' + str(age) + ', right?'})
