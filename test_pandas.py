import pandas as pd
animals = ['Tiger', 'Bear', 'Moose']
s = pd.Series(animals)
print(s)

numbers = [1,2,3]
t = pd.Series(numbers)
print(t)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
v = pd.Series(sports)
result = v.loc['Golf']
print(v)
print(result)
third = v.iloc[3]
print(third)