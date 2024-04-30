import requests
import json
import os
from dotenv import load_dotenv

load_dotenv('.env')

def getStockPrice(symbol, api_key):
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2024-01-01/2024-04-01?apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stock_info = {
            "Ticker": data["ticker"],
            "Price": data["results"][0]["c"],
            "Volume": data["results"][0]["v"]
        }
        return stock_info

def main():
    api_key = os.getenv('POLYGON_KEY')

    while True:
        symbol = input("What ticker should we check out? (type 'quit' to exit): ")
        if symbol.lower() == "quit":
            break

        stock_data = getStockPrice(symbol, api_key)
        print(json.dumps(stock_data, indent=4))

if __name__ == "__main__":
    main()

