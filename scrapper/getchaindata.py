import san
import matplotlib.pyplot as plt

def get_price_data(start_date, end_date):
    ohlc_df = san.get(
    "ohlc/ethereum",
    from_date=start_date,
    to_date=end_date,
    interval="1w")
    
    return ohlc_df

def get_onchain_data(start_date, end_date):
    """
    Get network growth metric
    """
    network_growth_df = san.get(
        "network_growth/ethereum",
        from_date = start_date,
        end_date = end_date,
        interval = "1d"
    )
    network_growth_df.plot()

def get_social_data(start_date, end_date):
    soc_df = san.get(
        "social_volume/bitcoin",
        interval="1d",
        from_date = start_date,
        to_date = end_date,
        social_volume_type = "TELEGRAM_CHATS_OVERVIEW"
    )
    print(soc_df)
    soc_df.plot()
    plt.show()
    return soc_df

def get_developer_data():
    pass

def main():
    get_price_data("2022-01-01","2022-03-01")
    get_onchain_data("2022-01-01","2022-03-01")
    get_social_data(
        "2022-01-01",
        "2022-03-01")

if __name__ == "__main__":
    main()