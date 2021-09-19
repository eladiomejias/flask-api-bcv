from flask import Flask
from bs4 import BeautifulSoup
from flask import Response
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

   # try:

        # DECLARACIONES
        page = requests.get("http://www.bcv.org.ve");
        soup = BeautifulSoup(page.content, 'html.parser')
        dolarContenedor = soup.find(id="dolar")
        elements = dolarContenedor.find_all(class_="centrado")
        dolarValues = []

        #FOR
        for item in elements:
            dolarValues.append(item.find("strong").get_text())
       
        #JSON
        dolar = {
        'dolar': {
            'SIN_CONVERTIR': dolarValues[0],
            'CONVERTDO': dolarValues[1]
            }
        }  

        return jsonify(dolar)

   # except:

    #    return "Error"

@app.route('/demo')
def demo():
    return "Otro route"