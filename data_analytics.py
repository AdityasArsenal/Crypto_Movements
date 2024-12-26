def data_ana(list_of_names , list_of_symboles, list_of_prices, list_of_vlos, list_of_percentage_changes, list_of_market_cap):

    print("\n")    
    print("\n")  
    print("Analized data🟡🟡🟡🟡🟡🟡🟡Analized data")
    print("\n")  
    print("\n")

    list_of_top5 = list_of_names[0:5]
    print(f"List of top 5 market cap coins  : {list_of_top5[0]}")

    higest_percentage = max(list_of_percentage_changes)
    index_hi = list_of_percentage_changes.index(higest_percentage)
    higest_percentage_coin = list_of_names[index_hi]

    print("\n") 
    print(f"{higest_percentage_coin}   has the higest percentage change, with  : {higest_percentage}change")

    lowest_percentage = min(list_of_percentage_changes)
    index_lo = list_of_percentage_changes.index(lowest_percentage)
    lowest_percentage_coin = list_of_names[index_lo]

    print("\n") 
    print(f"{lowest_percentage_coin}   has the lowest percentage change, with   : {lowest_percentage}change")

    print("\n")
    print("\n")
    print("Analized data🟡🟡🟡🟡🟡🟡🟡Analized data")
    print("\n")     
    print("\n") 