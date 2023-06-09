import json
from datetime import datetime
import pandas as pd

"""
Dates are in UNIX time format, so you need to convert them to human readable
"""

def convert_market_chart_data(fp, sfp, date_format):
    new_market_chart = {}
    with open(fp, 'r') as file:
        market_chart = json.load(file)
    avail_keys = market_chart.keys()
    for k in avail_keys:
        list_values = market_chart[k]
        for pair_values in list_values:
            date = datetime.utcfromtimestamp(pair_values[0] / 1000).strftime(date_format)
            if date not in new_market_chart:
                new_market_chart[date] = {k: pair_values[1]}
            else:
                new_market_chart[date].update({k: pair_values[1]})
    with open(sfp, 'w') as file:
        json.dump(new_market_chart, file)




if __name__ == '__main__':

    fp = "btc_market_chart.json"
    sfp = "btc_market_chart_gud.json"
    date_format = '%Y-%m-%d %H:%M:%S'
    convert_market_chart_data(fp, sfp, date_format)


