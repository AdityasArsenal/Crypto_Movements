import time as tt
from excel_handl import update_excel
from get_list import data_to_list
from excel_handl import update_excel
from data_ana import data_ana
 


#print(type(litss))
#print(*tuplee_of_data)


try:
    while True:
        # Update the Excel file
        tuplee_of_data = data_to_list()

        data_ana(*tuplee_of_data)

        update_excel(*tuplee_of_data)
        print("Excel file created successfully!")

        # Wait for the next update
        tt.sleep(70)

except Exception as e:
    print(f"Stopped updating due to: {e}")
