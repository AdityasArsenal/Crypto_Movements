import time as tt
from newrough import update_excel, data_ana
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate Google Drive once at the start
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("client_secrets.json")  # Ensure this path is correct
    gauth.LocalWebserverAuth()  # Authenticate via browser
    return GoogleDrive(gauth)

def upload_to_drive(drive):
    try:
        # Search for an existing file
        file_list = drive.ListFile({'q': "title = 'crypto_data.xlsx'"}).GetList()
        if file_list:
            file = file_list[0]  # Use the first matching file
            print("Existing file found. Updating...")
        else:
            file = drive.CreateFile({'title': 'crypto_data.xlsx'})
            print("No existing file found. Creating a new one...")
        
        file.SetContentFile('crypto_data.xlsx')
        file.Upload()
        print(f"File uploaded. Link: {file['webContentLink']}")
    except Exception as e:
        print(f"Failed to upload file: {e}")

# Authenticate and initialize the Google Drive object
drive = authenticate_google_drive()

try:
    while True:
        # Update the Excel file
        update_excel()
        print("Excel file created successfully!")

        # Upload the updated Excel file to Google Drive
        upload_to_drive(drive)
        print("File uploaded successfully!")

        # Wait for the next update
        tt.sleep(70)

except Exception as e:
    print(f"Stopped updating due to: {e}")


data_ana()
data_to_list()