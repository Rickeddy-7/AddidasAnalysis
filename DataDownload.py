
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def download_data():
    '''download the dataset using the kaggle api'''

    # We first create an api instance and verify our api key with the authenticate method call
    api = KaggleApi()
    api.authenticate()

    # get the data and store it in the project directory
    api.dataset_download_file(
        dataset='thedevastator/adidas-fashion-retail-products-dataset-9300-prod',
        file_name='adidas_usa.csv'
    )

    # unzip and delete the file
    zip_file = os.getcwd() + '/adidas_usa.csv.zip'
    with zipfile.ZipFile(zip_file, 'r') as file:
        file.extractall()

    os.remove(zip_file)
