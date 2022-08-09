import requests
import json


urls = {
    "enhancement" : "https://www.lostarkmarket.online/api/export-market-live/North America East?category=Enhancement Material",
    "lifeskill" : "https://www.lostarkmarket.online/api/export-market-live/North America East?category=Trader",
    "crystal" : "https://www.lostarkmarket.online/api/export-market-live/North America East?category=Currency Exchange"
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

    with open("json_data/" + type + ".json", 'w', encoding='utf-8') as f:
        json.dump(market_locations, f, ensure_ascii=False, indent=4)

def get_prices(url, name):
    response = requests.request("GET", url)

    json_data = response.json()
    serialized_json = {}

    for item in json_data:
        serialized_json[item["id"]] = item

    with open("json_data/" + name + ".json", 'w', encoding='utf-8') as f:
        json.dump(serialized_json, f, ensure_ascii=False, indent=4)


def update_prices():
    pass