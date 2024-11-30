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
        return metadata
    else:
        print(f"Error: {response.status_code}, {response.text}")

list_of_names = []
list_of_symboles = []
list_of_prices = [] 
list_of_vlos = []
list_of_percentage_changes = []
list_of_market_cap = []

def data_ana():
    list_of_top5 = list_of_names[0:5]
    print(f"List of top 5 market cap coins : {list_of_top5}")

    higest_percentage = max(list_of_percentage_changes)
    index_hi = list_of_percentage_changes.index(higest_percentage)
    higest_percentage_coin = list_of_names[index_hi]
    print(f"{higest_percentage_coin} has the higest, with :{higest_percentage}change")

    lowest_percentage = min(list_of_percentage_changes)
    index_lo = list_of_percentage_changes.index(lowest_percentage)
    lowest_percentage_coin = list_of_names[index_lo]
    print(f"{lowest_percentage_coin} has the lowest, with :{lowest_percentage}change")

def data_to_list():
    dataaa = get_info()

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


def update_excel():
    data_to_list()
    
    list_of_top5 = list_of_names[0:5]
    higest_percentage = max(list_of_percentage_changes)
    lowest_percentage = min(list_of_percentage_changes)

    data = {
        'Name': list_of_names,
        'Symbol': list_of_symboles,
        'Price': list_of_prices,
        'MCap': list_of_market_cap,
        '24change':list_of_percentage_changes,
        'vlos':list_of_vlos,
        
    }

    # Converted the dictionary into a pandas DataFrame
    df = pd.DataFrame(data)

    df.to_excel('crypto_data.xlsx', index=False)


