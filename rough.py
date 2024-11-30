import pandas as pd
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

list_of_names = []
list_of_symboles = []
list_of_prices = [] 
list_of_vlos = []
list_of_percentage_changes = []
list_of_market_cap = []

for coin in dataaa['data']:  # Access 'data' from the parsed JSON
    list_of_names.append(coin['name'])
    list_of_symboles.append(coin['symbol'])
    list_of_prices.append(coin['quote']['USD']['price'])
    list_of_vlos.append(coin['quote']['USD']['volume_change_24h'])
    list_of_percentage_changes.append(coin['quote']['USD']['percent_change_24h'])
    list_of_market_cap.append(coin['quote']['USD']['market_cap'])
    

    print("🟣🟣🟣🟣🟣🟣")

# Create a dictionary from the lists
data = {
    'Name': list_of_names,
    'Symbol': list_of_symboles,
    'Price (USD)': list_of_prices,
    'Market Cap (USD)': list_of_vlos,
    'percentage_changes':list_of_percentage_changes,
    'vlos':list_of_vlos
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('crypto_data.xlsx', index=False)

print("Excel file created successfully!")