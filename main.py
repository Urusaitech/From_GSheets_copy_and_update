import os
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import urllib.request
from xml.dom import minidom
import time


def get_service():
    creds_json = os.path.dirname(__file__) + "/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


# Change code below to process the `response` dict:
def main():
    service = get_service()
    sheet = service.spreadsheets()

    sheet_id = "1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g"

    resp = sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1"]).execute()
    usd_values = []  # values from the source sheet
    for i in resp['valueRanges'][0]['values'][1:]:
        usd_values.append(i[2])
    usd_values = [int(i) for i in usd_values]

    # get usd/rub today's pair and save to local file
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    webFile = urllib.request.urlopen(url)
    data = webFile.read()
    with open('usd_rub', "wb") as localFile:
        localFile.write(data)

    doc = minidom.parse('usd_rub')
    currency = doc.getElementsByTagName("Valute")
    rates_list = []
    for rate in currency:
        value = rate.getElementsByTagName("Value")[0]

        rates_list.append(value.firstChild.nodeValue)

    usd = rates_list[10]
    usd = usd.replace(',', '.')
    usd = float(usd)  # today's usd/rub value

    # prepare a new column
    rub_sum = [i * usd for i in usd_values]
    rub_sum.insert(0, 'стоимость,₽')

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
        'values': [rub_sum],
        'majorDimension': 'COLUMNS',
    }

    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_,
                                                     valueInputOption=value_input_option, body=value_range_body)
    add_col = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range="Sheet1!E1:E",
                                                     valueInputOption=value_input_option, body=value_range_body_addcol)
    response = request.execute()
    add_col_resp = add_col.execute()

    pprint(response)
    pprint(add_col_resp)

    time.sleep(3)
    main()


if __name__ == '__main__':
    main()
