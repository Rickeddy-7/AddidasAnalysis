
import pandas as pd


# def clean_data():
#     '''preprocess the data for analysis'''


df = pd.read_csv(r'C:\Users\ricke\AddidasAnalysis\adidas_usa.csv')

query = df['original_price'].notnull().replace(df['original_price'][:1], '')
query2 = df['original_price']

print(query2)