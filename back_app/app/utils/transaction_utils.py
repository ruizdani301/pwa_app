import requests
import json
from flask import request


username = 'c435c4b8-6935-4488-bf18-e747cd0057ef'
password = '9iMJOxaX4Mm6dWuN*WBkVLrLGWByMdlRgyZzGkBjsyuWolH_#aA#@r@ZlPzCS9e@'


def update_transactions(link_id, id_account):
    print(link_id)
    print(id_account)
    data_link = {
        "link":"96c4a12b-1d59-4e87-a820-39cc3ef65b8e",
        "account":"i3265406b-a08a-45fb-83a9-b0ac3aee690c",
        "date_from":"2024-04-01",
        "date_to":"2025-04-30"
    }
    url = f"https://sandbox.belvo.com/api/transactions/"
    response = requests.post(url, auth=(username, password), json=data_link)
    print(response.status_code)
    print(response.json())
    return response
    
def get_transactions(id_account, link_id):
    url = f"https://sandbox.belvo.com/api/transactions/?account={id_account}&link={link_id}"
    response = requests.get(url, auth=(username, password))
    return response