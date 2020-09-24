import pandas as pd


# 1
df = pd.read_json('dataframe_people.json')
df.set_index("labels", inplace=True)    # df.reset_index(level=0, inplace=True)
print(df.head())

# 2
df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
print(df)
df = df.drop('k')


# 3
df.sort_values(by=['name', 'score'], ascending=[False, True])
print(df)

# 4
df['qualify'] = df['qualify'].map({'yes': True, 'no': False})

# 5
df['name'] = df['name'].replace('James', 'Suresh')


# 6
df.pop('attempts')
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
df['color'] = color
print(df)

# 7
print("Number of NaN values: ", df.isnull().values.sum())

# 8
df = df.fillna(0)

# 9
df = df.sample(frac=1)
print(df)

# 10
print(df.dtypes)
print(df)

# 11
df.score = df.score.astype(int)
print(df.dtypes)
