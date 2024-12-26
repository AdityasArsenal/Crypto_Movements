import time as tt
from API_calls import get_info
from add_data_to_list import data_to_list
from data_analytics import data_ana
from excelsheet_maker import update_excel

#print(type(litss))
#print(*tuplee_of_data)

try:
    while True:
        # Update the Excel file
        datt = get_info()

        tuplee_of_data = data_to_list(datt)

        data_ana(*tuplee_of_data)

        update_excel(*tuplee_of_data)

        print("Excel file created successfully!")

        # Wait for the next update
        tt.sleep(10)

except Exception as e:
    print(f"Stopped updating due to: {e}")
