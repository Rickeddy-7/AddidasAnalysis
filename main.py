
import DataCleaning as dc
import DataDownload as dd
import os


def run_main():
    '''runs the scripts that download and clean the data for analysis'''

    dd.download_data()
    # exch_rate_api_key = os.getenv('api_key')
    exch_rate_api_key = 'a1c6d810970de6cc81ac6273'
    dc.clean_data(exch_rate_api_key)


if __name__ == "__main__":
    run_main()