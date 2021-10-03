from flask import Flask
from bs4 import BeautifulSoup
from flask import Response
from flask import jsonify
import requests

app = Flask(__name__)

def obtenerValores(idValue):

    # Definicion de Request / BS4
    arrayElements = []
    page = requests.get("http://www.bcv.org.ve");
    soup = BeautifulSoup(page.content, 'html.parser')
    dolarContenedor = soup.find(id=idValue)
    elements = dolarContenedor.find_all(class_="centrado")

    # For in
    for item in elements:
        arrayElements.append(item.find("strong").get_text())
    
    # Variables
    convertido = arrayElements[0].replace(".", "").replace(",", ".").strip()
    convertido = float(convertido)
    convertido = round(convertido, 5)
    #sinConvertir = arrayElements[0].replace(".", "").replace(",", ".").strip()

    # Creacion de diccionario.
    diccionarioValores = {
        idValue: {
            #"SIN_CONVERTIR": sinConvertir,
            "CONVERTIDO": arrayElements[0].strip(),
            "VALOR": convertido
            #"SIN_CONVERTIR_VISUAL": arrayElements[0]
        }
    }

    # Return valores de diccionario.
    return diccionarioValores


@app.route('/', methods=['GET'])
def index():

    try:

        dolar = obtenerValores("dolar")
        euro = obtenerValores("euro")
        yuan = obtenerValores("yuan")

        monedas = { **dolar , **euro, **yuan}

        return jsonify(monedas)
        #return "Good"

    except:

        # Error mensaje
        errorValue = {
        'error': {
            'mensaje': 'No se pudo comunicar con el proveedor.',
            'status': 500
            }
        }  

        return jsonify(errorValue)

@app.route('/demo')
def demo():
    return "Otro route"