from Google import Create_Service
from pprint import pprint

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# ID Google Drive (taken from URL)
folder_id = '12UQCg1mGB_FhfWuSZjEiVambDESvRUSA'


query = f"parents: '{folder_id}'"

response = service.files().list(q=query, ).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query, pageToken=nextPageToken).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')


pprint(files)