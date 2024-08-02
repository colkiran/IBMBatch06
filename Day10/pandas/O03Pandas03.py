
import pandas as pd

data = {
    'calories': [450, 375, 400],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

print('-' * 60)

# loc to extract data from one or more rows

print(df.loc[0])

print('-' * 60)
print(df.loc[[0, 1]])

print('-' * 60)
df1 = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df1)
#
print(df1.loc['day2'])