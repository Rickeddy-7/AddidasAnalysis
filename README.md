# Adidas Sales Data Pipeline
A simple pipeline that fetches a dataset from the kaggle website through an API call and stores the cleaned data in a new csv file with one click!

## Data Engineering:
- `Extract:` Used the <a href="https://www.kaggle.com/docs/api">kaggle API</a> to download the data directly from the site, which comes in the form of a zip file that contains all the data we need.
- `Transform:` Used Python to clean and preprocess the data for analysis which involved feature engineering using `Pandas` and `Numpy`, currency conversions with the help of the <a href='https://app.exchangerate-api.com/'>ExchangeRates-API</a> and the `Requests` library, and imputing missing values, to name a few.
- `Load:` Once clean, we then write the data onto a new excel sheet
