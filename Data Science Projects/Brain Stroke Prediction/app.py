#Importing the libraries
import pickle
from flask import Flask, render_template, request
#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('stroke.pkl', 'rb')) 

    
#www.google.co.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    gender = int(request.form['gender'])
    age = int(request.form['age'])
    hypertension = int(request.form['Hypertension'])
    heart_disease = int(request.form['Heart Disease'])
    avg_glucose_level = int(request.form['Glucose'])
    bmi = int(request.form['BMI'])
    smoking_status = int(request.form['Smoking Status'])
    
    Diagnosis = loadedModel.predict([[gender,age,hypertension,heart_disease,avg_glucose_level,bmi,smoking_status]])[0]

    if Diagnosis == 0:
        Diagnosis = "No possibility of brain stroke"
    else:
        Diagnosis = "Possibility of brain stroke"

    return render_template('index.html', output=Diagnosis)

#Main function
if __name__ == '__main__':
    app.run(debug=True)