import requests
import json
from flask import request


username = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
password = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'


# @transactions_bp.route('/actualizar', methods=['POST'])
def update_transactions(link_id, id_account):

    data_link = {
        "link":link_id,
        "account":id_account,
        "date_from":"2024-04-01",
        "date_to":"2025-04-30"
    }
    url = f"https://sandbox.belvo.com/api/transactions/"
    response = requests.get(url, auth=(username, password), json=data_link)
    return response
    
def get_transactions(id_account, link_id):
    url = f"https://sandbox.belvo.com/api/transactions/?account={id_account}&link={link_id}"
    response = requests.get(url, auth=(username, password))
    return response