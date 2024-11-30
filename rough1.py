# Import modules 
import os
import requests
import pandas as pd

print(os.getcwd())

# Assign base URL 
base_url = 'https://pro-api.coinmarketcap.com'

# Set headers // including API key
headers = {
    'X-CMC_PRO_API_KEY': cmc_key,
    'Content-Type': 'application/json'
}

def get_cmc_data(endpoint, params=None):

    if params == None:
              params = {}

    endpoint_url = base_url + endpoint
    
    try:
        # Send the get request with headers
        response = requests.get(endpoint_url, 
                                params=params,
                                headers=headers)
        print('requesting ' + response.url)
        # Check if request success (status code 200)
        if response.status_code == 200:
            # Parse and format response
            res_data = response.json()
            
        else:
            # Handle errors or other status codes 
            print(f"Request failed with status code {response.status_code}")
            return
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
    return res_data

# CMC ID map 
map_data = get_cmc_data('/v1/cryptocurrency/map')

map_df = pd.DataFrame(map_data['data']) 
print(len(map_df))
print(map_df)
print(map_df.iloc[0])
print(map_df.iloc[-1])
    
map_df.to_excel('map_data.xlsx',
                index=False)
