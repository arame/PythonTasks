import pandas as pd
import logging, sys
from sklearn.preprocessing import StandardScaler

logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

class col:
    price = "price"

def main():
    df_house_data = pd.read_csv("kc_house_data.csv")
    df_price = df_house_data[col.price]
    ss = StandardScaler()
    np_price = df_price.to_numpy().reshape(-1,1)
    Xstd_price = ss.fit_transform(np_price)
    logging.info("Using the sklearn library, the standardisation for price")
    logging.info(f"gives a mean of {round(Xstd_price.mean(), 2)} and a standard deviation of {round(Xstd_price.std(), 2)}")
    
    df_price_std = (df_price - df_price.mean())/df_price.std()

    logging.info("From calculations in Python, the standardisation for price")
    logging.info(f"gives a mean of {round(df_price_std.mean(), 2)} and a standard deviation of {round(df_price_std.std(), 2)}")

if __name__ == "__main__":
    main()