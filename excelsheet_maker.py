import pandas as pd

def update_excel(list_of_names , list_of_symboles, list_of_prices, list_of_vlos, list_of_percentage_changes, list_of_market_cap):
    
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

    file_path = r"G:\My Drive\crypto_data.xlsx"
    df.to_excel(file_path, index=False)

    print("4th🔴🔴🔴🔴🔴🔴4th")
