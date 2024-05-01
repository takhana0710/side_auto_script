import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.readonly',
          'https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive.metadata',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.readonly',
          ]  # 授權範圍

class auth():
    def __init__(self):
        self.mail = ''
        self.apikey= ''
    
    def gettoken(self):
        with open('token.json', 'r', encoding='utf-8') as f:
            token = f.read()
            f.close()
        token = eval(token)
        return token
    
    def refresh_token(self,SCOPES):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        print(SCOPES)
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    
    def file_create(self):
        self.refresh_token(SCOPES)
        token = self.gettoken()
        uploadtype = 'media'
        params = {'uploadtype':uploadtype}
        header = {'Authorization':'Bearer %s'%token['token'],"Accept": "application/json",'Content-Type':'application/octet-stream'}
        url = 'https://www.googleapis.com/upload/drive/v3/files'
        with open('2022-04-14 21-00-13-Test_Result.html', 'r', encoding='utf-8') as f :
            file = requests.post(url,headers=header,params=params,files={'files':f.read()})
            f.close()
        print(file.text)
    
auth().file_create()