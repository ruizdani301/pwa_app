from flask import Blueprint, jsonify, request
import requests
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.register_link import register_link
from werkzeug.security import check_password_hash
from models.model import Usuario
#from app.conection_db import session

accounts_bp = Blueprint('accounts', __name__)

api_user = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
api_pass = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'

def get_accounts(link_reg):
    print(f"Validar llamar cuentas link_reg: {link_reg}")
    url = f"https://sandbox.belvo.com/api/accounts/?link={link_reg}"
    response = requests.get(url, auth=(api_user, api_pass))
    print(f"Validar llamar cuentas: {response}")
    return response

@accounts_bp.route('/', methods=['POST'])
def accounts():
    try:
        # Obtener datos del cuerpo en formato JSON
        data = request.get_json()

        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        institution = data['institution']
        email = data['email']
        user = email.split("@")[0]
        password = data['password']
        username_type = data['username_type']
        registered_link = data['register_link']
        print(registered_link)

        db_user = Usuario.query.filter_by(email=email).first()
        if not db_user or not check_password_hash(db_user.password, password):    
            return jsonify({'error': 'password invalido'}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    
    if not registered_link:
        data = register_link(user, password, institution, username_type)
        json_data = data.json()
        registered_link = json_data['id']
    response = get_accounts(registered_link)
    print("Validar llamar cuentas")
    if response.json()['count'] == 0:
        print("es cero")
        # data_link = {
        #     'link':f"{registered_link}",
        # }
        # url = f"https://sandbox.belvo.com/api/accounts/"
        # response = requests.get(url, auth=(api_user, api_pass), json=data_link)


    print(f"Respuesta de la API: {response.status_code}")
    if response.status_code == 200 or response.status_code == 201:
        
        accounts_json = response.json()
        cuentas_dict = {account["id"]: account["name"] for account in accounts_json["results"]}

        print(cuentas_dict)

        return jsonify({'cuentas': cuentas_dict, "link_account":registered_link}), response.status_code
    else:
        print('Error:', response.status_code, response.text)
        return jsonify({'Error': response.text}), response.status_code
