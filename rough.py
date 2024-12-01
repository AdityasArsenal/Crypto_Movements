try:
    while True:
        # Update the Excel file
        update_excel()
        print("Excel file created successfully!")

        # Wait for the next update
        tt.sleep(70)

except Exception as e:
    print(f"Stopped updating due to: {e}")


data_ana()