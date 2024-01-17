
import DataCleaning as dc
import DataDownload as dd
import os


def run_main():
    '''runs the scripts that download and clean the data for analysis'''

    print('fetching data..'.upper())
    dd.download_data()
    exch_rate_api_key: str = os.getenv('EXCH_API')
    dc.clean_data(exch_rate_api_key)


if __name__ == "__main__":
    run_main()