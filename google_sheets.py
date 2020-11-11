import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# File from Google Developer Console
CREDENTIALS_FILE = 'Valley.json'
# ID Google Sheets doc (we can take from URL)
spreadsheet_id = '1yFl7OR-KDSIMJ1fvNeboor7dFCGYK47C1k0qaCbgSNk'

# an instance of API access
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
worksheet_name = 'Labels!'
# Example of reading a file
"""values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimension='COLUMNS'
).execute()
pprint(values)
"""
# Example of writing to a file
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": worksheet_name + "B1:B23",
             "majorDimension": "ROWS",
             "values": [['gs://project/List1/Sphera Bold/men/Alpha-T-8/03.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/24.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/12.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/01.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/04.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/15.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/26.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/17.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/20.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/02.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/06.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/09.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/13.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/21.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/11.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/19.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/05.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/14.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/25.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/18.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/22.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/07.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/16.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/10.jpg'],
                        ['gs://project/List1/Sphera Bold/men/Alpha-T-8/23.jpg'],
]},
            {"range": "D5:E6",
             "majorDimension": "COLUMNS",
             "values": []}
	]
    }
).execute()