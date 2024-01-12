
import pandas as pd
import numpy as np
import requests as rq


def clean_data():
    '''preprocess the data for analysis'''

    df = pd.read_csv(r'C:\Users\ricke\AddidasAnalysis\adidas_usa.csv')
    
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

    # create a new field for the currency in ZAR

    # create a new field for the revenue in ZAR

    # create a new field for the discounted amount(difference of selling price and original price) in ZAR

    # then write all the changes into a new excel file
    # print("Successfully cleaned data.\n")
    # df.to_csv('adidas_usa_clean.csv', index=False)


def convert_currency():
    '''converts all amounts into South African Rands using the Exchange Rates API'''

    api_key = 'a1c6d810970de6cc81ac6273'
    response = rq.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD")

    rate = response.json()['conversion_rates']['ZAR']
    

