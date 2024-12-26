def data_to_list(datt):
    dataaa = datt

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
        
        #print("1st •••••••••••••••••••••1st")
    
    print("2nd 🟣🟣🟣🟣🟣🟣2nd")
    return  list_of_names , list_of_symboles, list_of_prices, list_of_vlos, list_of_percentage_changes, list_of_market_cap 
