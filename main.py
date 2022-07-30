import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import web_scrape as ws
import json
import datetime
import time

epoch = int(time.time())
local_time_new_date = datetime.datetime.fromtimestamp(epoch)
new_date = local_time_new_date.strftime("%d%m%Y-%H%M")

print('---' + str(new_date) + '---')

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets-api.json', scope)

#load json postions from json file
with open('utils/sheet-positions.json') as json_file:
    sheet_positions = json.load(json_file)

# authorize the clientsheet 
client = gspread.authorize(creds)

#open the sheet
sheet = client.open('NA East - Lost Ark - Market Analysis')
sheet_instance = sheet.get_worksheet(3) #Market prices on sheet 4

#get currency price
sheet_instance.update_cell(18,14, 'Test')


print('---')
print()

ws.update_locations("Enhancement Material", 2, 1)