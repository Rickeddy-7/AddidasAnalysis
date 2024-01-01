import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


# We first create an api instance and verify our api key with the authenticate method call
api = KaggleApi()
api.authenticate()

# # get the data and store it in the project directory
api.dataset_download_file(
    dataset='thedevastator/adidas-fashion-retail-products-dataset-9300-prod',
    file_name='adidas_usa.csv'
)

# # unzip the file so we can work with it
# # we use the raw string so the ZipFile method doesn't throw an encoding error
zip_file = r'C:\Users\ricke\AddidasAnalysis\adidas_usa.csv.zip'
with zipfile.ZipFile(zip_file, 'r') as file:
    file.extractall()

# then remove the unnecessary zip file
os.remove(zip_file)