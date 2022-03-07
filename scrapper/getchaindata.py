import san

def get_price_data():
    pass

def get_onchain_data(start_date, end_date):
    ohlc_df = san.get(
    "ohlc/ethereum",
    from_date=start_date,
    to_date=end_date,
    interval="1w")
    print(ohlc_df.tail())

def get_social_data():
    pass

def get_developer_data():
    pass

def main():
    get_onchain_data("2022-01-01","2022-03-01")
 

if __name__ == "__main__":
    main()