import math
import numpy as np
from scipy.stats.stats import pearsonr
import logging, sys
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def calc_euclid_distance(p, q):
    logging.info(f"Calculate Euclidian distance between {p} and {q}")
    N = len(p)
    M = len(q)
    if N != M:
        sys.exit(f"!! Error! Both points must have same dimensions. Instead p has {N} and q has {M}")

    pn = np.array(p)
    qn = np.array(q)
    logging.info(f"From Numpy, the Euclidian distance is {np.linalg.norm(pn - qn)}")
    tot_dist_squared = 0
    for pi, qi in zip(p, q):
        tot_dist_squared += (pi - qi) **2

    euclidian_distance = math.sqrt(tot_dist_squared)
    logging.info(f"From Python, the Euclidian distance is {euclidian_distance}")
    logging.info("\n")

def main():
    logging.info("*"*20)
    p = (3, 1, 6)
    q = (5, -2, -7)
    calc_euclid_distance(p, q)
    p = (3.14, 123, 6.5, -3.2, 34.7)
    q = (5.92, -22, -751.34, 0, 5.34)
    calc_euclid_distance(p, q)
    p = (3, 0)
    q = (5, 0)
    calc_euclid_distance(p, q)
    p = (3, 1, 6, 5)
    q = (5, -2, -7)
    #calc_euclid_distance(p, q)

if __name__ == "__main__":
    main()