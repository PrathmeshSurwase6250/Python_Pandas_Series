import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# data= pd.read_csv('./Series/Datasets/subs.csv' )
# print(type(data))
data= pd.read_csv('./Series/Datasets/subs.csv'  ) 
data = data.squeeze("columns")
print(data)


kolhidata = pd.read_csv('./Series/Datasets/kohli_ipl.csv'  ,index_col='match_no')
kolhidata = kolhidata.squeeze("columns")
print(kolhidata)

bollywood = pd.read_csv('./Series/Datasets/bollywood.csv'  ,index_col='movie')
bollywood = bollywood.squeeze("columns")
print(bollywood)


print(data.head())
print(data.head(10))

print(data.tail())
print(data.tail(10))

print(bollywood.sample())

print(bollywood.value_counts())


print(kolhidata.sort_values())
print(kolhidata.sort_values(ascending=False))
print(kolhidata.sort_values(ascending=False).head().values)
kolhidata.sort_values(ascending=False).head().values[0]
# kolhidata.sort_values(inplace=True,ascending=False) 
print(kolhidata)

print(bollywood.sort_index())
bollywood.sort_index(inplace=True )
print(bollywood)


vk = kolhidata
print(vk.count())

print(data.sum())

print(data.prod())

print(data.mean())
print(data.median())
print(data.mode())
print(data.std())
print(data.var())
print(data.min())
print(data.max())
print(data.describe())
print(bollywood.loc["Why Cheat India"])

movies  = bollywood.value_counts().head(20)
movies.plot(kind='bar',color='orange')
plt.show()