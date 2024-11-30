import pandas as pd
import requests
import time
import pickle

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

head = {
    "X-CMC_PRO_API_KEY": "99b495dd-1690-4354-834d-3fadaf8bfb7b"
}

num = 4

params = {
    "sort": "market_cap",
    "limit":num
}

def get_info():
    response = requests.get(url, headers=head, params=params)

    if response.status_code == 200:
        metadata = response.json()
        return metadata
    else:
        print(f"Error: {response.status_code}, {response.text}")


def update_excel():
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
    
    with open('market_caps.pkl', 'wb') as f:
        pickle.dump(list_of_market_cap, f)

    data = {
        'Name': list_of_names,
        'Symbol': list_of_symboles,
        'Price': list_of_prices,
        'MCap': list_of_market_cap,
        '24change':list_of_percentage_changes,
        'vlos':list_of_vlos
    }

    # Converted the dictionary into a pandas DataFrame
    df = pd.DataFrame(data)

    df.to_excel('crypto_data.xlsx', index=False)

try:
    while True:
        update_excel()
        print("Excel file created successfully!")
        time.sleep(70)
except:
    print("Stopped updating due to API overvelmed")

# Save the list of market caps using pickle

