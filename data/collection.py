import os
import json
from ast import literal_eval
import requests

BASE_URL = "https://api.coingecko.com/api/v3/"
ENDPOINTS = {"market_chart": "coins/{id}/market_chart",
             "ping": "ping",
             "current_price": "price"}
QUERY_PARAMS = {"ids": "{ids}",
                "vs_currencies": "{vs_currencies}"}

def format_url(base_url, endpoint, query_params):
    url = base_url + endpoint + "?"
    url += "&".join([f"{key}={value}" for key, value in query_params.items()])
    return url

def generate_coingecko_url():
    base_url = "https://api.coingecko.com/api/v3/"

    action = input("Enter the action (e.g., market_chart, current_price): ")

    if action == "market_chart":
        endpoint = "coins/{cryptocurrency}/market_chart"
        query_params = {
            "vs_currency": input("Enter the currency: "),
            "days": input("Enter the number of days (or 'max' for all available historical data): "),
            "interval": input("Enter the interval (e.g., daily): ")
        }
    elif action == "current_price":
        endpoint = "simple/price"
        query_params = {
            "ids": input("Enter the cryptocurrency ID(s) (comma-separated if multiple): "),
            "vs_currencies": input("Enter the currency/currencies (comma-separated if multiple): ")
        }
    else:
        print("Invalid action. Please try again.")
        return None

    cryptocurrency = input("Enter the cryptocurrency: ")
    endpoint = endpoint.format(cryptocurrency=cryptocurrency)

    url = base_url + endpoint + "?"
    url += "&".join([f"{key}={value}" for key, value in query_params.items()])
    return url

if __name__ == "__main__":




    # endpoint = "search/trending"
    # response = requests.get(os.path.join(base_path, endpoint))
    complete_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=max&interval=daily"
    response = requests.get(complete_url)
    content = response.content
    content_decode = content.decode('utf-8')
    content_dict = json.loads(content_decode)
    with open('btc_market_chart.json', 'w') as file:
        json.dump(content_dict, file)
    su = None