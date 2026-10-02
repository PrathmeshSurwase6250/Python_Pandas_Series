import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

num = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(num)

print(num.agg(['sum','mean','std','var','min','max']))

num=num.astype('Int32')
print(num)


print(num.between(3,7))
marks = pd.Series([35, 45, 67, 89, 25, 76])

print(marks[marks.between(40, 80)])


s = pd.Series([10, 20, 30, 40, 50])

print(s.clip(20, 40))

# drop_duplicates() — Remove Duplicate Values
s = pd.Series([10, 20, 20, 30, 30, 30, 40])

print(s.drop_duplicates())

# dropna() — Remove Missing Values
s = pd.Series([10, 20, None, 40, None, 60])

print(s)

print(s.dropna())
#  fillna() — Fill Missing Values
s = pd.Series([10, 20, None, 40, None, 60])

print(s.fillna(0))


s = pd.Series(
    [100, 200, 300, 400, 500],
    index=["a", "b", "c", "d", "e"]
)

print(s.filter(items=["a", "c", "e"]))


s = pd.Series(["M", "F", "M", "F"])

print(s.map({
    "M": "Male",
    "F": "Female"
}))


