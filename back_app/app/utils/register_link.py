from flask import Blueprint, jsonify, request
import requests
import json

api_user = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
api_pass = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'
def register_link(usuario, contraseña, institucion, username_type, access_mode='single', fetch_resources=["ACCOUNTS", "TRANSACTIONS"]):
    url = 'https://sandbox.belvo.com/api/links/'
    
    data = {
                'username':usuario,
                'password': contraseña,
                'institution': institucion,
                'access_mode': access_mode,
                'fetch_resources': fetch_resources
            }
    
    if (username_type == "text"):

        pass
    else:
        #username_type != "text"
        data['username_type']= username_type
    print("respuesta de data")
    print(data)
 
    response = requests.post(
        url,
        auth=(api_user, api_pass),        
        json=data                             
    )


    if response.status_code == 200 or response.status_code == 201:
        
        print('Éxito:', response.json())
        return response
        print("fue exitoso")
    else:
        print('Error:', response.status_code, response.text)
        return response
