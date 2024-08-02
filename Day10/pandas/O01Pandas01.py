import pandas as pd

mydataset  = {
    'cars' :['BMW', 'AUDI', 'MERC'],
    'ratings': [8, 7.9, 9.3]
}

print(mydataset)

print('-' * 60)
df = pd.DataFrame(mydataset)
print(df)

print(pd.__version__)