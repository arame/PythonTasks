import math
import logging, sys
from sklearn.metrics import mean_squared_error
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def calc_rmse():
    _actual= [34, 37, 44, 47, 48, 48, 46, 43, 32, 27, 26, 24]
    _pred = [37, 40, 46, 44, 46, 50, 45, 44, 34, 30, 22, 23]
    logging.info(f"The ground truth RMSE value is {math.sqrt(mean_squared_error(_actual, _pred))}")
    N = len(_actual)
    squared_error = 0
    for actual, pred in zip(_actual, _pred):
        squared_error += (actual - pred)**2

    logging.info(f"The calculated RMSE value is {math.sqrt(squared_error/N)}")
    
if __name__ == "__main__":
    calc_rmse()

