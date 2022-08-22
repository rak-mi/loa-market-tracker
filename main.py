import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import web_scrape as ws
import json
import datetime
import time
import logging

epoch = int(time.time())
local_time_new_date = datetime.datetime.fromtimestamp(epoch)
new_date = local_time_new_date.strftime("%d%m%Y-%H%M")
logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG)

logging.info('---' + str(new_date) + '---')

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets-api.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

#open the sheet
sheet = client.open('NA East - Lost Ark - Market Analysis')
sheet_instance = sheet.get_worksheet(8) #Market prices on sheet 9

logging.info('---')
logging.info('')


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

sheet_positions = [enhancement_sheet_positions, lifeskill_sheet_positions, crystal_sheet_positions]
price_json_list = [enhancement_prices, lifeskill_prices, crystal_prices]


for x in range(0,3):
    positions= sheet_positions[x]
    price_json = price_json_list[x]
    for position in positions:
        time.sleep(2.5)
        item_id = position["id"]
        name = position["name"]
        price = price_json[item_id]["avgPrice"]
        sheet_instance.update_cell(position["y_pos"],position["x_pos"]-1, name)
        sheet_instance.update_cell(position["y_pos"],position["x_pos"], price)
        logging.info("Updated " + name + " with " +  str(price))

sheet_instance = sheet.get_worksheet(0)
sheet_instance.update_cell(1,15,local_time_new_date.strftime("%m/%d/%Y, %I:%M:%S%p"))