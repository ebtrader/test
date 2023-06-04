import pandas as pd

#df = pd.read_csv('olympics.csv')

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)

print(df.head())

name_of_columns = df.columns
print(name_of_columns)

#   a[start:stop]  # items start through stop-1
#   a[start:]      # items start through the rest of the array
#   a[:stop]       # items from the beginning through stop-1
#   a[:]           # a copy of the whole array

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

print(df.head())