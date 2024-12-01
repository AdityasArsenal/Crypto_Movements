import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

head = {
    "X-CMC_PRO_API_KEY": "fa2d2137-7fd2-4240-8db6-a5f67ed36ac4"
}

params = {
    "sort": "market_cap",
    "limit": 50
}

def get_info():
    response = requests.get(url, headers=head, params=params)

    if response.status_code == 200:
        metadata = response.json()
        print("1st🟢🟢🟢🟢🟢🟢1st")
        return metadata
    else:
        print(f"Error: {response.status_code}, {response.text}")
