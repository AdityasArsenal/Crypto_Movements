
def data_ana(list_of_names , list_of_symboles, list_of_prices, list_of_vlos, list_of_percentage_changes, list_of_market_cap):
    
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