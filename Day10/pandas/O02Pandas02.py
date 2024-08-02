# pandas series - one dimension array

import pandas as pd

a = [1, 2, 3, 4, 5]

psrs = pd.Series(a)
print(psrs)
# first value from the series
print(psrs[0])

print('-' * 60)

a = [1, 2, 3, 4, 5]

psrs = pd.Series(a, index=['i', 'j', 'k', 'l', 'm'])
print(f"psrs :\n{psrs}")
print(psrs['k'])

print('-' * 60)
calories = {'day1': 60, 'day2': 48, 'day3': 42 }
print(calories)

psrs = pd.Series(calories)
print(psrs)
