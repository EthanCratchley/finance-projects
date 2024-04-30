import requests
import json
import os
from dotenv import load_dotenv

load_dotenv('.env')

def getStockPrice(symbol, api_key):
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2023-01-09/2023-01-09?apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stock_info = {
            "Ticker": data["ticker"],
            "Price": data["results"][0]["c"],
            "Volume": data["results"][0]["v"]
        }
        return stock_info
    else:
        return "Failed to retrieve data"

api_key = os.getenv('POLYGON_KEY')
symbol = 'AAPL'

stock_data = getStockPrice(symbol, api_key)
print(json.dumps(stock_data, indent=4))