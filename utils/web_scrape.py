import requests
import json


urls = {
    "Enhancement Material" : "https://www.lostarkmarket.online/api/export-market-live/North America East?category=Enhancement Material"
}

def update_locations(type, x_pos, y_pos_start):
    url = urls[type]
    response = requests.request("GET", url)

    json_data = response.json()
    market_locations = []

    count = y_pos_start
    for market_item in json_data:
        new_json = {}
        new_json["id"] = market_item["id"]
        new_json["name"] = market_item["name"]
        new_json["y_pos"] = count
        new_json["x_pos"] = x_pos
        count += 1
        market_locations.append(new_json)

    with open("json_data/enhancement.json", 'w', encoding='utf-8') as f:
        json.dump(market_locations, f, ensure_ascii=False, indent=4)

def get_prices():
    url = "https://www.lostarkmarket.online/api/export-market-live/North America East?category=Enhancement Material"
    response = requests.request("GET", url)

    json_data = response.json()