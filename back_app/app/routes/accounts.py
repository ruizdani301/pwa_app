from flask import Blueprint, jsonify, request
import requests
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.register_link import register_link
from werkzeug.security import check_password_hash
from models.model import Usuario
import time
#from app.conection_db import session

accounts_bp = Blueprint('accounts', __name__)

api_user = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
api_pass = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'

def get_accounts(link_reg):

    data_link = {
            'link': link_reg
        }
    url = f"https://sandbox.belvo.com/api/accounts/"
    response = requests.get(url, auth=(api_user, api_pass), json=data_link)
    return response

@accounts_bp.route('/', methods=['POST'])
def accounts():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400
        
        institution = data['institution']
        email = data['email']
        user = email.split("@")[0]
        password = data['password']
        username_type = data['username_type']
        registered_link = data.get('register_link',None)
        print(registered_link)

        db_user = Usuario.query.filter_by(email=email).first()
        if not db_user or not check_password_hash(db_user.password, password):    
            return jsonify({'error': 'password invalido'}), 401
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    print("password correcto")
    if not registered_link:
        print("registrando link")
        data = register_link(user, password, institution, username_type)
        json_data = data.json()
        registered_link = json_data['id']
        
        print(f"Link registrado es: {registered_link}")
    time.sleep(7)
    response = get_accounts(registered_link)
    if response.json()['count'] == 0:
        print("CUANDO ES CERO")
        print(f"{registered_link}- {type(registered_link)}")
    
        return jsonify({"error": "No se encontraron cuentas"}), 400

    print(f"Respuesta de la API: {response.status_code}")
    if response.status_code == 200 or response.status_code == 201:
        dic_account = {}
        accounts_json = response.json()
        #cuentas_dict = {account["id"]: account["name"] for account in accounts_json["results"]}
        for account in accounts_json["results"]:
            dic_account[account["id"]] = [account["link"],account["name"]]
  
        return jsonify({'cuentas': dic_account, "link_account":registered_link}), response.status_code
    else:
        print('Error:', response.status_code, response.text)
        return jsonify({'Error': response.text}), response.status_code
