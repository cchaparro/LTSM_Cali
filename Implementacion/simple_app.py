
import logging
import numpy as np
from flask import Flask
from flask import request
from flask import json
from sklearn import metrics
from sklearn import datasets
from numpy import array
from keras.models import model_from_json

app = Flask(__name__)
logging.basicConfig(filename='demo.log', level=logging.DEBUG)



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/prueba', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    else:
        return "415 Unsupported Media Type ;)"


@app.route('/carga-modelo', methods = ['get'])
def cargar_modelo():

    json_file = open('../Modelamiento/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # Cargo el nuevo modelo
    loaded_model.load_weights("../Modelamiento/LTSM_Cali.h5")
    type(loaded_model.summary())
    return loaded_model.summary()