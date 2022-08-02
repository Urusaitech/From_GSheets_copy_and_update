import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


def get_service():
    creds_json = os.path.dirname(__file__) + "/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


service = get_service()
sheet = service.spreadsheets()

sheet_id = "1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g"

resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1"]).execute()

# The ID of the spreadsheet to update.
spreadsheet_id = '1zV1L2l4kb1Uu1uMozBHknUWrh80dRr90dvotSTP27EM'

# The A1 notation of the values to update.
range_ = 'Sheet1!A1:E'

# How the input data should be interpreted.
value_input_option = 'RAW'

value_range_body = {
         # resp is a dict inside a list inside a dict
         'values': resp['valueRanges'][0]['values']
}
value_range_body_addcol = {
         # resp is a dict inside a list inside a dict

}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_,
                                                 valueInputOption=value_input_option, body=value_range_body)
add_col = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range="Sheet1!E",
                                                 valueInputOption=value_input_option, body=value_range_body_addcol)
response = request.execute()
add_col_resp = add_col.execute()

# Change code below to process the `response` dict:
pprint(response)
pprint(add_col_resp)