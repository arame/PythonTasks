from collections import Counter
import logging, sys, math
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
logging.getLogger().setLevel(logging.INFO)

def calc_mean(items):
    mean = sum(items)/ len(items)
    return mean

def calc_median(items):
    items.sort()
    is_odd = bool(len(items) % 2)
    if is_odd:
        middle_index = int(math.ceil(len(items) / 2))
        return items[middle_index]
    
    # Even number of items in the list
    # Need to calculate the middle value between the 2 middle items in the list
    index = int(len(items) / 2)
    return (items[index] + items[index + 1]) / 2

def calc_mode(items):
    counts = dict(Counter(items))
    max_count = max(counts.values())
    mode = {i for i in counts if counts[i]==max_count}
    return mode.pop(), max_count

def calc_mode_stack_overflow(items):
    # According to Stack Overflow, the best answer would be;
    mode = max(items, key=items.count)
    return mode, items.count(mode)
    # See https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list

def main():
    items = [2, 4, 45, 16, 7, 12, 13, 14, 23, 30, 47, 88]
    mean = calc_mean(items)
    logging.info(f"Mean: {mean}")
    median = calc_median(items)
    logging.info(f"Median: {median}")
    items2 = [62, 12, 62, 62, 4, 5, 6, 6, 6, 7, 62, 13, 14, 23, 30, 47, 88]
    logging.info("------------New list-------------")
    mean = calc_mean(items2)
    logging.info(f"Mean: {mean}")
    median = calc_median(items2)
    logging.info(f"Median: {median}")
    mode, count = calc_mode(items2)
    logging.info(f"Mode: {mode} with {count} items")
    mode, count = calc_mode_stack_overflow(items2)
    logging.info(f"Mode from Stack Overflow code: {mode} with {count} items")

if __name__ == "__main__":
    main()
