from gettext import install
from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        print(request)
        a = float(request.form['Credit_History'])
        b = request.form['Gender_Male']

        if b.upper() == "MALE":
            b = 0
        else:
            b = 1

        c = float(request.form['Married_Yes'])
        d = float(request.form['Property_Area_Semiurban'])
        
        
        prediction=model.predict([[a,b,c,d]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="sorry please enter the positive number")
        else:
            output = "Loan is approved" if output else "Loan is not approved"

            # if output == 1:
            #     output = "Loan is approved"
            # else:
            #     output = "Loan is not approved"


            return render_template('index.html',prediction_text="Your {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)