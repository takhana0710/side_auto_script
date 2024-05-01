import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import sys
# _,token_path,credentials_path=sys_parameter(sys.argv,os_path=os.getcwd(),sys='gcp')
token_path = 'testcase/gcp/token.json'
credentials_path='testcase/gcp/credentials.json'
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
          ]
class auth():
    def __init__(self):
        self.apikey = 'AIzaSyACHHTo6mfAGiOjJfXaXemyNshPo3CeSIQ'
    
    def gettoken(self):
        with open(token_path, 'r', encoding='utf-8') as f:
            token = f.read()
            f.close()
        token = eval(token)
        return token
    
    def refresh_token(self, SCOPES):
        creds = None
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
authToken = auth()
authToken.refresh_token(SCOPES=SCOPES)
token=authToken.gettoken()
headers = {'Authorization': 'Bearer %s' % token['token'], 'Accept': 'application/json'}

def getDriver():
    url='https://www.googleapis.com/drive/v3/files'
    print(requests.get(url,params={'key':authToken.apikey,'includeItemsFromAllDrives':True},headers=headers).text)

def getSheet(**kwargs):
    url='https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}'.format(spreadsheetId=kwargs.get('spreadsheetId'))
    print(requests.get(url,params={'key':authToken.apikey},headers=headers).text)

def getCell(**kwargs):
    url='https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{value}'.format(spreadsheetId=kwargs.get('spreadsheetId'),value=kwargs.get('value'))
    res = requests.get(url,params={'key':authToken.apikey},headers=headers).json()
    return res
    
def SignInData(**kwargs):
    res=getCell(spreadsheetId='10GB_f1UQGYazweEcXzpcW51orCRs72xSMrpc338ardM',value=kwargs.get('sheetName'))
    month = kwargs.get('sheetMonth')
    for i in res['values']:
        while len(i)<8:
            i.append("")
    data = list(zip(*res['values']))[1:] # tuple 各個index 湊合
    sign_list=[]
    for i in data:
        for j in i:
            if '/' in j: # 判斷 日期
                if len(j[j.index('/')+1:]) ==1: # 補0
                    day = '0'+j[j.index('/')+1:]
                else:
                    day =j[j.index('/')+1:]
                if i[i.index(j)+1] != '':
                    sign_list.append({'CreateDay':month+day,'Days': int(j[j.index('/')+1:]),'BonusType':'金幣','BonusNumber': int(i[i.index(j)+1].replace(',',''))})
                if i[i.index(j)+2] != '':
                    sign_list.append({'CreateDay':month+day,'Days': int(j[j.index('/')+1:]),'BonusType':'銀幣','BonusNumber': int(i[i.index(j)+2].replace(',',''))})
    sign_list=sorted(sign_list,key=lambda x:x.get('Days'))
    return sign_list
# process()
# getSheet(spreadsheetId='10GB_f1UQGYazweEcXzpcW51orCRs72xSMrpc338ardM')
def mail(**kwargs):
    reply_name = kwargs.get('send_site') # 不同站台
    get_mail_url='https://gmail.googleapis.com/gmail/v1/users/me/messages'
    res = requests.get(get_mail_url,params={'q':f'no-reply@{reply_name}','key':authToken.apikey},headers=headers).json()
    # print(res)
    get_mail_id = res['messages'][0]['id']
    get_mail_content_url = f'https://gmail.googleapis.com/gmail/v1/users/me/messages/{get_mail_id}'
    res = requests.get(get_mail_content_url, params={'key': authToken.apikey},headers=headers).json()
    return res['snippet']
    
    
# getCell(spreadsheetId='10GB_f1UQGYazweEcXzpcW51orCRs72xSMrpc338ardM',value='6月簽到')
