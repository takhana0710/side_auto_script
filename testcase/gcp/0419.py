from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file,client,tools
import time
import os
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

def delete_driver_service_file(service,file_id):
    service.files().delete(fileId=file_id).exexcute()
    
def update_file(service,update_driver_service_name,local_file_path):
    print("正在上傳檔案....")
    file_metadata = {"name":update_driver_service_name}
    media = MediaFileUpload(local_file_path,)
    file_metadata_size = media.size()
    start = time.time()
    file_id = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    end=time.time()
    print("上傳檔案成功！")
    print('雲端檔案名稱為: ' + str(file_metadata['name']))
    print('雲端檔案ID為: ' + str(file_id['id']))
    print('檔案大小為: ' + str(file_metadata_size) + ' byte')
    print("上傳時間為: " + str(end-start))

    return file_metadata['name'], file_id['id']
def search_file(service, update_drive_service_name, is_delete_search_file=False):
    result = service.files().list(fileds="nextPageToken files(id,name)",space='drive',q="'name='"+update_drive_service_name+"'and trashed = false'",).execute()
    items = result.get('files',[])
    if not items:
        print('not found'+ update_drive_service_name)
    else:
        print('result')
        for item in items:
            time=1
            print('u{0} {1}'.format(items['name'],items['id']))
            delete_driver_service_file(service,file_id=items['id'])
            if time==len(items):
                return item['id']
            else:
                time+=1

def trashed_file(service, is_delete_trashed_file=False):
    results = service.files().list(fields="nextPageToken, files(id, name)", spaces='drive', q="trashed = true",
                                   ).execute()
    items = results.get('files', [])
    if not items:
        print('垃圾桶無任何資料.')
    else:
        print('垃圾桶檔案: ')

        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
            if is_delete_trashed_file is True:
                print("刪除檔案為:" + u'{0} ({1})'.format(item['name'], item['id']))
                delete_driver_service_file(service, file_id=item['id'])

def main(is_update_file_function=False, update_drive_service_name=None, update_file_path=None):
    print('id_update_file_function')
    print(type(is_update_file_function))
    print(is_update_file_function)
    store = file.Storage('token.json')
    creds = store.get()
    
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow,store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    print('*' * 10)

    if is_update_file_function is True:
        print(update_file_path + update_drive_service_name)
        print("=====執行上傳檔案=====")
    
        # 清空 雲端垃圾桶檔案
        # trashed_file(service=service, is_delete_trashed_file=True)
    
        # 搜尋要上傳的檔案名稱是否有在雲端上並且刪除
        # search_file(service=service, update_drive_service_name=update_drive_service_name,
        #             is_delete_search_file=True)
    
        # 檔案上傳到雲端上
        update_file(service=service, update_driver_service_name=update_drive_service_name,
                    local_file_path=os.getcwd() + '/' + update_drive_service_name)
    
        print("=====上傳檔案完成=====")


main(is_update_file_function=bool(True), update_drive_service_name='2022-04-14 21-00-13-Test_Result.html', update_file_path=os.getcwd() + '/')
