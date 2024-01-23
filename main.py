
import DataCleaning as dc
import DataDownload as dd


def run_main():
    '''runs the scripts that download and clean the data for analysis'''

    print('FETCHING DATA..')
    dd.download_data()
    dc.clean_data()


if __name__ == "__main__":
    run_main()