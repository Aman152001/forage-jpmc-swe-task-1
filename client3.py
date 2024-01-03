import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    
    # Calculate the average of bid and ask as the price
    price = (bid_price + ask_price) / 2
    
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """Get the ratio of price_a and price_b"""
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Initialize variables to hold data for ratio calculation
        price_a = 0
        price_b = 0

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            
            # Print stock information
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            
            # Update variables for ratio calculation
            if price_a == 0:
                price_a = price
            else:
                price_b = price

        # Calculate and print the ratio
        if price_a != 0 and price_b != 0:
            ratio = getRatio(price_a, price_b)
            print("Ratio %s" % ratio)
        else:
            print("Not enough data to calculate ratio.")
