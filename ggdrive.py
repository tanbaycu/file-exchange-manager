from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


SERVICE_ACCOUNT_FILE = r'tệp json chứa key ở đây'


SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

def upload_file(file_path):
    try:

        media = MediaFileUpload(file_path)
        

        request = service.files().create(
            media_body=media,
            body={
                'name': file_path.split('/')[-1],
                'mimeType': 'application/octet-stream'
            },
            fields='id, webViewLink'
        ).execute()
        

        file_id = request.get('id')
        web_view_link = request.get('webViewLink')
        
        return file_id, web_view_link
    except Exception as e:
        print(f'An error occurred: {e}')
        return None, None

def update_permissions(file_id):
    try:
     
        permission = {
            'type': 'anyone',
            'role': 'reader'
        }
        
        service.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id'
        ).execute()
        
        print(f'Permissions updated for file ID: {file_id}')
    except Exception as e:
        print(f'An error occurred while updating permissions: {e}')


file_path = input('Nhập đường dẫn tệp bạn muốn tải lên: ')
file_id, url = upload_file(file_path)
if file_id and url:
    print('URL của file:', url)
    update_permissions(file_id)
else:
    print('Không thể tải tệp lên.')

