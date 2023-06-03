import json
from datetime import datetime

"""
Dates are in UNIX time format, so you need to convert them to human readable
"""

if __name__ == '__main__':
    with open("btc_market_chart.json", 'r') as file:
        market_chart = json.load(file)
    avail_keys = market_chart.keys()
    for k in avail_keys:
        list_values = market_chart[k]
        for pair_values in list_values:
            pair_values[0] = datetime.utcfromtimestamp(pair_values[0]/1000).strftime('%Y-%m-%d %H:%M:%S')
    with open("btc_market_chart_date.json", 'w') as file:
        json.dump(market_chart, file)

