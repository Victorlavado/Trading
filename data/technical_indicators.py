import pandas as pd

def add_sma_to_data(fp, sfp):
    """
    Enrich simple data with dates(id), price, market_caps and volumes with simple moving average
    :return:
    """
    df = pd.read_json(fp).T
    print(df.head(n=10))
    df["Sma_50"] = df["prices"].rolling(window=50).mean()
    df.to_csv(sfp)

if __name__ == '__main__':
    fp = "btc_market_chart_gud.json"
    sfp = "btc_sma50.csv"
    add_sma_to_data(fp, sfp)