
import pandas as pd
import numpy as np


def clean_data():
    '''preprocess the data for analysis'''

    df = pd.read_csv(r'C:\Users\ricke\AddidasAnalysis\adidas_usa.csv')
    
    # remove the dollar sign from the price and get the average price to impute missing values
    df['original_price'] = pd.to_numeric(df['original_price'].str.replace('$', ''))
    mean_price = int(np.nanmean(df['original_price']))
    df['original_price'] = df['original_price'].fillna(str(mean_price)).astype(int)
    
    # delete unwanted fields
    cols = ['url', 'sku', 'currency', 'availability', 'source', 'source_website', 'description', 'brand', 'images', 'country', 'language']
    df.drop(columns=cols, inplace=True)
    
    # rename the 'crawled_at' field to 'date' and remove the time
    df.rename(columns={'crawled_at': 'date'}, inplace=True)
    
    # rename 'breadcrumbs' field to 'gender' and remove the category
    df.rename(columns={'breadcrumbs': 'gender'}, inplace=True)
    
    # create a new field for the currency in ZAR

    # create a new field for the revenue in ZAR

    # create a new field for the discounted amount(difference of selling price and original price) in ZAR

    # then write all the changes into a new excel file
    print("Successfully cleaned data.\n")
    df.to_csv('adidas_usa_clean.csv', index=False)

# clean_data()