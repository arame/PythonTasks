import pandas as pd
import logging, sys
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def main():
    logging.info("---------------- Started ----------------")
    df_diabetes = pd.read_csv("diabetes.csv")
    logging.info("Original values")
    logging.info(df_diabetes["SkinThickness"].head(10))
    df_mean = df_diabetes["SkinThickness"].copy()
    df_median = df_diabetes["SkinThickness"].copy()
    mean_skinthickness = df_mean.mean()
    median_skinthickness = df_median.median()
    logging.info(f"Mean value is {mean_skinthickness}")
    logging.info(f"Median value is {median_skinthickness}")
    df_mean.fillna(mean_skinthickness, inplace=True)
    df_median.fillna(median_skinthickness, inplace=True)
    logging.info("Null values replaced with mean")
    logging.info(df_mean.head(10))
    logging.info("Null values replaced with median")
    logging.info(df_median.head(10))

if __name__ == "__main__":
    main()