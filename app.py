import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify, app, url_for

app = Flask(__name__)

regmodel = pickle.load(open('regmodel.pkl','rb')) ##loading the model
scaler = pickle.load(open('scaler.pkl','rb')) ##loading the scalar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    new_data = scaler.transform(np.array(data).reshape(1,-1))
    print(new_data)
    output = regmodel.predict(new_data)
    return render_template('index.html',prediction_text=f'''The valuation of the house is {np.round(output[0],2)} 
                           hundred thousand dollars''')
                           
if __name__ == '__main__':
    app.run(port=5000, debug=True)