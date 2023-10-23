#Importing the libraries
import pickle
from flask import Flask, render_template, request
#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('l_model.pkl', 'rb')) 

    
#www.google.co.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('lungs.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    GENDER = int(request.form['GENDER'])
    AGE = int(request.form['AGE'])
    SMOKING= int(request.form['SMOKING'])
    YELLOW_FINGERS= int(request.form['YELLOW_FINGERS'])
    ANXIETY = int(request.form['ANXIETY'])
    PEER_PRESSURE = int(request.form['PEER_PRESSURE'])
    CHRONIC_DISEASE= int(request.form['CHRONIC_DISEASE'])
    FATIGUE = int(request.form['FATIGUE'])
    ALLERGY = int(request.form['ALLERGY'])
    WHEEZING = int(request.form['WHEEZING'])
    ALCOHOL_CONSUMING = int(request.form['ALCOHOL_CONSUMING'])
    COUGHING = int(request.form['COUGHING'])
    SHORTNESS_OF_BREATH = int(request.form['SHORTNESS_OF_BREATH'])
    SWALLOWING_DIFFICULTY = int(request.form['CHEST_PAIN'])
    CHEST_PAIN = int(request.form['CHEST_PAIN'])


    Diagnosis = loadedModel.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])[0]

    if Diagnosis == 1:
        Diagnosis = "No presence of lung cancer"
    else:
        Diagnosis = "Presence of lung cancer"

    return render_template('lungs.html', output=Diagnosis)

#Main function
if __name__ == '__main__':
    app.run(debug=True)