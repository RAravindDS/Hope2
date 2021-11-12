from logging import NullHandler
from flask import Flask, send_from_directory 
from pywebio.input import *
from pywebio.output import * 
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio import start_server
import time 

import pickle 
import numpy as np
import pandas as pd
import argparse

model = pickle.load(open('ippa.pkl', 'rb'))
app = Flask(__name__)

def predict():
    name = input("Enter Your Sweet Name 😁", type = 'text')
    age = input("Enter Your Age 🧑🏾‍🎤", type = 'number')
    put_markdown('## (っ◔◡◔)っ ♥ Welcome! This app will help to Find the House price in paris ! ♥')
    put_image('https://www.hec.edu/sites/default/files/styles/knowledge_articles_full/public/2018-12/American-houses-Real-estate-finance_knowledge_HEC.jpg?itok=jzUJgaHj')
    category = select("Select the Category [Basic: 0, Luxury: 1] ", [0, 1])
    #put_image(open('hasyard.jpg', 'rb').read())
    hasYard = select("Select the HasYard [0,1]", [0,1])
    hasPool = select("Select the hasPool [0,1]", [0,1])
    isNewBuilt = select("Select the isNewBuilt [0,1]", [0,1])
    hasStormProtector = select("Select the hasStormProtector [0,1]", [0,1])
    numberOfRooms = input("Number of Rooms:", type = NUMBER)
    hasStorageRoom = select("Select the hasStorageRoom [0,1]", [0,1])
    basement = input("Basement, Four Digit Number ex: [1234]:", type = NUMBER)



    Predictions = model.predict([[category, hasYard, hasPool, isNewBuilt, hasStormProtector, numberOfRooms, hasStorageRoom, basement]])
    
    put_table([
        ['Features', 'Value'],
        ['Name', name],
        ['Age', age],
        ['Category', category],
        ['HasYard', hasYard],
        ['HasPool', hasPool],
        ['IsNewBuilt', isNewBuilt],
        ['HasStormProtector', hasStormProtector],
        ['NumberOfRooms', numberOfRooms],
        ['HasStorageRoom', hasStorageRoom],
        ['Basement', basement]])
    
    check = checkbox(options= ['Scrll Up and check All Details are Correct'])
    put_processbar('bar')
    for i in range(1, 11):
        set_processbar('bar', i / 10)
        time.sleep(0.1)
    put_text("Your House price is: ", str(round(Predictions[0], 2)), "Ruppes! ") 
    



app.add_url_rule('/tool', 'webio_view', webio_view(predict), methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=5000)
    args = parser.parse_args()

    start_server(predict, port=args.port)

# app.run(host = 'localhost', port = 5000, debug= True)


# if __name__ == '__main__':
#     app.run(debug=True)


