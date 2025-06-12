from flask import Blueprint, jsonify
import requests
import json
from flask import request
from ..utils.transaction_utils import get_transactions, update_transactions


transactions_bp = Blueprint('transactions', __name__)

username = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
password = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'


@transactions_bp.route('/', methods=['POST'])
def transactions():
    outflow_total = 0
    inflow_total = 0
    transacciones_dict = {}
    totales_dict = {}
    
    data = request.json
    data = request.get_json()
    id_account = "3265406b-a08a-45fb-83a9-b0ac3aee690c" #"data['id_account']
    link_id = "96c4a12b-1d59-4e87-a820-39cc3ef65b8e" #" data['link_account']
   

    print(f"{id_account}---{link_id}")   
    response = update_transactions(link_id, id_account)
    print(response.status_code)
    return jsonify({response.status_code: response.text})
    #if response.status_code == 202:
        #print("Se actualizaron las trasacciones")
    #     response = get_transactions(id_account, link_id)
    # elif response.status_code == 400:
    #     print("Error al actualizar las transacciones: ", response.text)
    #     return jsonify({"error": "Error al actualizar las transacciones"}), 400
    # saldos_json = response.json()
    # if len(saldos_json['results']) == 0:
    #     return jsonify({"error": "No hay trasacciones para esta cuenta"}), 200
    
    
    # if response.status_code == 200 or response.status_code == 201:
    #     saldos_json = response.json()
        
    #     for item in saldos_json["results"]:
    #         tipo = item.get("type")
    #         amount = item.get("amount", 0)
    #         description = item.get("description", "SIN DESCRIPCIÓN")

    #         if tipo == "OUTFLOW":
    #             outflow_total += amount
    #             transacciones_dict[description] = round(amount, 2)
    #         elif tipo == "INFLOW":
    #             inflow_total += amount
    #             transacciones_dict[description] = round(amount, 2)
    #         totales_dict["ingreso"] = round(inflow_total, 2)
    #         totales_dict["egreso"] = round(outflow_total, 2)
    #         totales_dict["total"] = round(inflow_total - outflow_total, 2)
    #     return jsonify([transacciones_dict, totales_dict]), response.status_code
        
    # else:
    #     print('Error:', response.status_code, response.text)
    #     return jsonify({'Error': response.text}), response.status_code