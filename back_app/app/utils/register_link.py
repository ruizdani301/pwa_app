from flask import Blueprint, jsonify, request
import requests
import json


def register_link(usuario, contraseña, institucion, username_type, access_mode='single', fetch_resources=["ACCOUNTS", "TRANSACTIONS"]):
    url = 'https://sandbox.belvo.com/api/links/'
    
    if username_type == "text":

        data = {
                'username':usuario,
                'password': contraseña,
                'institution': institucion,
                'access_mode': access_mode,
                'fetch_resources': fetch_resources
            }
    elif username_type != "text":
        data['username_type']= username_type
 
    response = requests.post(
        url,
        auth=(api_user, api_pass),        
        json=data                             
    )


    if response.status_code == 200 or response.status_code == 201:
        with open("link.txt", "w") as archivo:
            archivo.write(response.json()['id'])

        print('Éxito:', response.json())
        return response
        print("fue exitoso")
    else:
        print('Error:', response.status_code, response.text)
        return response
