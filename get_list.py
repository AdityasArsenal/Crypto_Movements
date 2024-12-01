import pandas as pd
import requests
import time

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

head = {
    "X-CMC_PRO_API_KEY": "fa2d2137-7fd2-4240-8db6-a5f67ed36ac4"
}

params = {
    "sort": "market_cap",
    "limit": 7
}

def get_info():
    response = requests.get(url, headers=head, params=params)

    if response.status_code == 200:
        metadata = response.json()
        print("🟢🟢🟢🟢🟢🟢")
        return metadata
    else:
        print(f"Error: {response.status_code}, {response.text}")


def data_to_list():
    dataaa = get_info()

    list_of_names = []
    list_of_symboles = []
    list_of_prices = [] 
    list_of_vlos = []
    list_of_percentage_changes = []
    list_of_market_cap = []


    #pprint.pprint(dataaa['data'])

    for coin in dataaa['data']:  
        list_of_names.append(coin['name'])
        list_of_symboles.append(coin['symbol'])
        list_of_prices.append(coin['quote']['USD']['price'])
        list_of_vlos.append(coin['quote']['USD']['volume_change_24h'])

        percentage_change = coin['quote']['USD']['percent_change_24h'] * 10
        list_of_percentage_changes.append(str(round(percentage_change, 2)) + "%")

        list_of_market_cap.append(coin['quote']['USD']['market_cap'])
        
        print("🟣🟣🟣🟣🟣🟣")
    
    return  list_of_names , list_of_symboles, list_of_prices, list_of_vlos, list_of_percentage_changes, list_of_market_cap 
