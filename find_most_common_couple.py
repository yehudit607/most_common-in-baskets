from collections import Counter
from itertools import combinations


def find_most_common_couple(baskets):

    d = Counter()
    for sub in baskets:
        if len(baskets) < 2:
            continue
        sub.sort()
        for comb in combinations(sub, 2):
            d[comb] += 1

    return (d.most_common(1))


baskets = [
['coke', 'ice', 'meat', 'ketchup', 'apple', 'banana'],
['coke', 'bread', 'meat', 'ketchup', 'apple', 'strawberry'],
['coke', 'pepsi', 'meat', 'ketchup', 'apple', 'banana'],
['pepsi', 'ice', 'meat', 'bread', 'tomato', 'cucumber'],
['sprite', 'rum', 'meat', 'ketchup', 'strawberry', 'banana'],
]
print(find_most_common_couple(baskets))
