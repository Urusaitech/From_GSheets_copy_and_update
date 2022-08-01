import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'ServiceAccountCredentials.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])


httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.base.APIClient

spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Сие есть название листа',
                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
}).execute()