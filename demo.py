from Google import Create_Service
from pprint import pprint

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# ID Google Drive (taken from URL)
folder = '1qTcffPGLOIhpYslTKuyIRBmMOWmBpupL'
# First, get the folder ID by querying by mimeType and name
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id = folderIdResult[0].get('id')
results = service.files().list(q="'" + id + "' in parents",
                               fields="nextPageToken, files(name)").execute()
items = results.get('files', [])
for item in items:
    items = item['name']
    my_output = f"{items}"

folder = '12UQCg1mGB_FhfWuSZjEiVambDESvRUSA'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id = folderIdResult[0].get('id')
results = service.files().list(q="'" + id + "' in parents",
                               fields="nextPageToken, files(name)").execute()
items = results.get('files', [])
for item in items:
    items = item['name']
    my_output2 = f"{my_output}/{items}"
 #   print(my_output2)

folder = '1cvT1YUa5Ah1g3vpj_yEBepNx1asnIvZD'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id = folderIdResult[0].get('id')
results = service.files().list(q="'" + id + "' in parents",
                               fields="nextPageToken, files(name)").execute()
items = results.get('files', [])
for f in range(0, len(items)):
    fId = items[f].get('name')
    my_output3 = f"{my_output2}/{fId}"

folder = '1C0B2J2uEio4rteHyu6-iWJajgjDXXZjP'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id = folderIdResult[4].get('id')
results = service.files().list(q="'" + id + "' in parents",
                               fields="nextPageToken, files(name)").execute()
items = results.get('files', [])
for item in items:
    final_data = []
    items = item['name']
    my_output4 = f"gs://project/List1/{my_output3}/{items}"
    print(my_output4)
