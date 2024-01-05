
import pandas as pd
import numpy as np


def clean_data():
    '''preprocess the data for analysis'''

    df = pd.read_csv(r'C:\Users\ricke\AddidasAnalysis\adidas_usa.csv')
    df = remove_columns(df)
    # call other functions...
    df.to_csv()


def format_price(df: pd.DataFrame):
    '''remove the dollar sign from the price and get the average price to impute missing values'''

    df['original_price'] = pd.to_numeric(df['original_price'].str.replace('$', ''))
    mean_price = int(np.nanmean(df['original_price']))
    df['original_price'] = df['original_price'].fillna(str(mean_price)).astype(int)

    return df


def remove_columns(df: pd.DataFrame):
    '''delete unwanted fields'''

    cols = ['url', 'sku', 'currency', 'availability', 'source', 'source_website', 'description', 'brand', 'images', 'country', 'language']
    return df.drop(columns=cols)


def format_date(df: pd.DataFrame):
    '''rename the 'crawled_at' to 'date' and remove the time'''

    return df
    

def format_gender(df: pd.DataFrame):
    '''rename 'breadcrumbs' to 'gender' and remove the category'''

    return df


def add_features(df: pd.DataFrame):
    '''create new fields for the prices in ZAR'''

    # create a new fields for the currency in ZAR

    # create a new field for the revenue in ZAR

    # create a new field for the discounted amount(difference of selling price and original price) in ZAR

    return df