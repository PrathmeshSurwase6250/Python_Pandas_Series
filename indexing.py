import pandas as pd
x = pd.Series([1,2,3,4,5 ,6,7,8,9,10 ,11,12,13,14,15])
print(x[0])
print(x[1:5])
print(x[5:])
print(x[:5])
print(x.iloc[-1])
print(x[-5:5])
print(x[-5:])
print(x[[0,3,4,10]])
x[0] = 100
print(x)
x[16] = 200
print(x)
x[1:3] = [1000,2000]
print(x)
x[[0,3,4,10]] = [100,200,300,400]
print(x)