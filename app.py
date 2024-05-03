# app.py
from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import random

app = Flask(__name__)

# Yüklü modeli ve scaleri yükleyin
model = joblib.load('anomaly_detection_model_RFC.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    data = pd.read_csv(file)

    n_data = cat_col_manipulation(data)
    X = n_data.drop(['outcome','level'], axis=1)
    X = scaler.transform(X)

    y_pred = model.predict(X)
    
    predictions = []
    df = data.drop('outcome', axis=1)
    for i in range(len(df)):
        prediction = {
            'Data Point': i,
            'Predicted Outcome': y_pred[i],
            'Details': df.iloc[i].to_dict()
        }
        predictions.append(prediction)

    random_predictions = random.sample(predictions, 3)

    return render_template('prediction.html', predictions=random_predictions)

def cat_col_manipulation(data):
    data['outcome'] = data.outcome.map(lambda x: 0 if x == 'normal' else 1)

    cat_col = data.select_dtypes(include=['object']).columns
    encoded_data = pd.get_dummies(data[cat_col], columns=cat_col, drop_first=True)
    encoded_data = encoded_data.astype(int)
    temp_data = data.drop(cat_col, axis=1)
    manipulated_data = pd.concat([temp_data, encoded_data], axis=1)

    return manipulated_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
