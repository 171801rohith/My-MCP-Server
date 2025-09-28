import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.send"]


def get_gmail_service():
    creds = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    TOKEN_PATH = os.path.join(BASE_DIR, "token.pickle")
    CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

    if os.path.exists(TOKEN_PATH): 
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=8080)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)


    return build("gmail", "v1", credentials=creds)

  

