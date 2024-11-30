import requests
import pprint

# Base URL
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Headers with your API key
headers = {
    "X-CMC_PRO_API_KEY": "99b495dd-1690-4354-834d-3fadaf8bfb7b"
}

# Query parameters
params = {
    "sort": "market_cap",
    "limit":4
}

# Send GET request
response = requests.get(url, headers=headers, params=params)

# Check response status and process data
if response.status_code == 200:
    dataaa = response.json()
    #pprint.pprint(dataaa)
else:
    print(f"Error: {response.status_code}, {response.text}")



for coin in dataaa['data']:  # Access 'data' from the parsed JSON
    coin_name = coin['name']
    coin_symbol = coin['symbol']
    price = coin['quote']['USD']['price']
    volume_change_24h = coin['quote']['USD']['volume_change_24h']
    percent_change_24h = coin['quote']['USD']['percent_change_24h']
    market_cap = coin['quote']['USD']['market_cap']
    
    # Print the extracted data
    print(f"Name: {coin_name}, Symbol: {coin_symbol}")
    print(f"Price: {price}")
    print(f"24h Volume Change: {volume_change_24h}")
    print(f"24h Percent Change: {percent_change_24h}")
    print(f"Market Cap: {market_cap}")
    print("🟣🟣🟣🟣🟣🟣")

