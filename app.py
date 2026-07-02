from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('floods.save')
scaler = joblib.load('transform.save')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict')
def Predict():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    temp = float(request.form['Temp'])
    humidity = float(request.form['Humidity'])
    cloud = float(request.form['Cloud'])
    annual = float(request.form['Annual'])
    rainfall = float(request.form['Rainfall'])

    data = pd.DataFrame([[temp, humidity, cloud, annual,
                          100, 200, rainfall, 150, 120, 1]],
    columns=['Temp','Humidity','Cloud Cover','ANNUAL',
             'Jan-Feb','Mar-May','Jun-Sep',
             'Oct-Dec','avgjune','sub'])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return render_template('chance.html')

    else:
        return render_template('no_chance.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
