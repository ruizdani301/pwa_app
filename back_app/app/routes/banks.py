import os
import json
import requests
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
banks_bp = Blueprint('banks', __name__)


all_banks = []
id_set = set()
@banks_bp.route('/', methods=['GET'])
def get_banks():

    """
    Obtiene la lista de bancos disponibles en la API de Belvo.

    Returns:
        json: Un objeto JSON con la lista de bancos, cada uno con sus campos:
            - country_code: C digo de 2 letras del pa s donde se encuentra el banco.
            - display_name: Nombre del banco para mostrar al usuario.
            - icon_logo: Enlace a la imagen del logo del banco.
    """
    #username = os.getenv('USERNAME')
    #password = os.getenv('PASSWORD')
    print(request.cookies.get('email'))
    username = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
    password = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'
    url = 'https://sandbox.belvo.com/api/institutions/?type=bank'
    
   
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        banks_data = response.json()
        print(banks_data)
        for bank in banks_data["results"]:
            info_bank = {}
            if bank["id"] in id_set:
                continue 
            id_set.add(bank["id"])  
            info_bank["id"]= bank["id"]
            info_bank["name"]= bank["name"]
            info_bank["display_name"]= bank["display_name"]
            info_bank["country_code"]= bank["country_code"]
            info_bank["icon_logo"]= bank["icon_logo"]
            if bank["form_fields"][0]["type"] == "select":
                info_bank["username_type"] = bank["form_fields"][0]["values"][0]["code"]
                       
            else:
                info_bank["username_type"] = bank["form_fields"][0]["type"]
 
            all_banks.append(info_bank)
                        
        


        return jsonify({'all_banks': all_banks}), response.status_code
    else:
        return jsonify({'error': 'No se pudo obtener la lista de bancos'}),response.status_code
