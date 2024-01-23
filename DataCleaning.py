
import pandas as pd
import numpy as np
import requests as rq
import os


def clean_data():
    '''preprocess the data for analysis'''

    df = pd.read_csv('adidas_usa.csv')
    
    # remove the dollar sign from the price and get the average price to impute missing values
    df['original_price'] = pd.to_numeric(df['original_price'].str.replace('$', ''))
    mean_price = int(np.nanmean(df['original_price']))
    df['original_price'] = df['original_price'].fillna(str(mean_price)).astype(int)
    
    # delete unwanted fields
    cols = [
        'url', 'sku', 'currency', 'availability', 'source', 'source_website', 'description', 
        'brand', 'images', 'country', 'language', 'crawled_at'
    ]
    df.drop(columns=cols, inplace=True)
    
    # rename fields
    df.rename(columns={'breadcrumbs': 'sub_category'}, inplace=True)
    
    # remove the main category from 'sub_category'
    df['sub_category'] = df['sub_category'].str.split('/').str[0]

    rate: float = get_exchange_rate()
    # create a new field for the revenue in ZAR, directly after the selling price in usd
    selling_price_zar = df['selling_price'].map(lambda x: round(x*rate, 2))
    df.insert(3, 'selling_price_zar', selling_price_zar)

    # create a new field for the currency in ZAR, directly after the original price in usd
    original_price_zar = df['original_price'].map(lambda x: round(x*rate, 2))
    df.insert(5, 'original_price_zar', original_price_zar)

    # then write all the changes into a new file
    print("successfully cleaned data.\n".upper())
    df.to_csv('adidas_usa_clean.csv', index=False)


def get_exchange_rate():
    '''returns the current exchange rate for usd/zar as a float'''

    api_key: str = os.getenv('EXCH_API')
    response = rq.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD")
    rate: float = response.json().get('conversion_rates').get('ZAR')
    
    return rate

clean_data()

