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

# authorize the clientsheet 
client = gspread.authorize(creds)

#open the sheet
sheet = client.open('NA East - Lost Ark - Market Analysis')
sheet_instance = sheet.get_worksheet(8) #Market prices on sheet 9

print('---')
print()


#ws.update_locations("enhancement", 2, 1)
#ws.update_locations("lifeskill", 5, 1)
ws.get_prices("https://www.lostarkmarket.online/api/export-market-live/North America East?category=Enhancement Material", "online-prices-enhancement")
ws.get_prices("https://www.lostarkmarket.online/api/export-market-live/North America East?category=Trader", "online-prices-lifeskills")
ws.get_prices("https://www.lostarkmarket.online/api/export-market-live/North America East?category=Currency Exchange", "online-prices-crystal")


with open('json_data/online-prices-enhancement.json') as json_file:
    enhancement_prices = json.load(json_file)

with open('json_data/online-prices-lifeskills.json') as json_file:
    lifeskill_prices = json.load(json_file)

with open('json_data/online-prices-crystal.json') as json_file:
    crystal_prices = json.load(json_file)

#load json postions from json file
with open('json_data/enhancement.json') as json_file:
    enhancement_sheet_positions = json.load(json_file)

#load json postions from json file
with open('json_data/lifeskill.json') as json_file:
    lifeskill_sheet_positions = json.load(json_file)

#load json postions from json file
with open('json_data/crystal.json') as json_file:
    crystal_sheet_positions = json.load(json_file)

for position in enhancement_sheet_positions:
    time.sleep(3)
    item_id = position["id"]
    name = position["name"]
    price = enhancement_prices[item_id]["avgPrice"]
    sheet_instance.update_cell(position["y_pos"],position["x_pos"]-1, name)
    sheet_instance.update_cell(position["y_pos"],position["x_pos"], price)
    print("Updated " + name + " with " +  str(price))

for position in lifeskill_sheet_positions:
    time.sleep(3)
    item_id = position["id"]
    name = position["name"]
    price = lifeskill_prices[item_id]["avgPrice"]
    sheet_instance.update_cell(position["y_pos"],position["x_pos"]-1, name)
    sheet_instance.update_cell(position["y_pos"],position["x_pos"], price)
    print("Updated " + name + " with " +  str(price))

for position in crystal_sheet_positions:
    time.sleep(3)
    item_id = position["id"]
    name = position["name"]
    price = crystal_prices[item_id]["avgPrice"]
    sheet_instance.update_cell(position["y_pos"],position["x_pos"]-1, name)
    sheet_instance.update_cell(position["y_pos"],position["x_pos"], price)
    print("Updated " + name + " with " +  str(price))