import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import logging, sys
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

class col:
    price = "price"
    bedrooms = "bedrooms"

def main():
    df_house_data = pd.read_csv("kc_house_data.csv")
    df_house_data = df_house_data[[col.price, col.bedrooms]]
    df_price = df_house_data[col.price]
    df_bedrooms = df_house_data[col.bedrooms]
    p = pearsonr(df_price, df_bedrooms)
    logging.info(f"The correct answer is that there is a correlation of {p.statistic}")
    logging.info(f"The probability of the null hypothesis, that there is no correlation is {p.pvalue}")
    N = len(df_bedrooms)
    sum_price = np.sum(df_price)
    sum_bedrooms = np.sum(df_bedrooms)
    # It is quicker to use numpy instead of pandas
    np_house_data = df_house_data.to_numpy()
    product_price_bedroom = 0
    sum_price_squared = 0
    sum_bedroom_squared = 0
    for price, bedrooms in np_house_data:
        product_price_bedroom += (price * bedrooms)
        sum_price_squared += price **2
        sum_bedroom_squared += bedrooms **2

    numerator = N * product_price_bedroom - (sum_price * sum_bedrooms)
    calc = lambda N, a, b : N * a - b**2
    price_part = calc(N, sum_price_squared, sum_price)
    bedroom_part = calc(N, sum_bedroom_squared, sum_bedrooms)
    denominator = np.sqrt(price_part * bedroom_part)
    r = numerator / denominator
    logging.info(f"The calculated answer is that there is a correlation of {r}")

if __name__ == "__main__":
    main()