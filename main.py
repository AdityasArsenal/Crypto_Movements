import time as tt
from sub import update_excel, data_ana

data_ana()

try:
    while True:
        update_excel()
        print("Excel file created successfully!")
        tt.sleep(70)
except:
    print("Stopped updating due to API overvelmed")

