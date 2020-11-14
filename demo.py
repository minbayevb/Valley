from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.appdata']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder = '12UQCg1mGB_FhfWuSZjEiVambDESvRUSA'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id1 = folderIdResult[0].get('name')
#output: Sphera Bold
folder = '1cvT1YUa5Ah1g3vpj_yEBepNx1asnIvZD'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files')
id2 = folderIdResult[1].get('name')
my_output = (f"{id1}/{id2}")
#Output Sphera Bold/man,woman,toddler

folder_woman = '1H8L8692I6WzvQiPb364ooViMyhSuc7v0'
folder_toddler = '1GicWXVDKiQQHPrxpovQv_VrhqJhbZ-E1'
folder_man = '1C0B2J2uEio4rteHyu6-iWJajgjDXXZjP'
folderId = service.files().list(q="mimeType = 'application/vnd.google-apps.folder'and parents in '" + folder_woman + "' and trashed = false",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files', [])
id3 = folderIdResult[0].get('name')
my_output2 = f"{my_output}/{id3}"
#we define folder name
folder_id = '1Ih-ZjGR6a_-PtVyzT0lxDYbyJX0FB-DP'
# files in folder
folderId = service.files().list(q="'" + folder_id + "' in parents",
                                fields="nextPageToken, files(id, name)").execute()
folderIdResult = folderId.get('files')
for folder in folderIdResult:
    final_output = []
    folderIdResult = folder['name']
    my_output3 = f"gs://project/List1/{my_output2}/{folderIdResult}"
    final_output.append(my_output3)
    print(final_output)

