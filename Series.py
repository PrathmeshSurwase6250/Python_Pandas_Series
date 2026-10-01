import numpy as np
import pandas as pd

country = pd.Series(['USA', 'Germany', 'USSR', 'Japan'])
print(country)

country =  ['Usa' , 'Germany', 'USSR', 'Japan']
country = pd.Series(country)
print(country)


runs = pd.Series([890, 765, 567, 435] , dtype = np.int32)
print(runs)

marks = pd.Series([89.5, 78.0, 56.7, 43.5] , dtype = np.float32, index=['English', 'Maths', 'Science', 'Social Science'])
print(marks)


marks = pd.Series([22,33,55],index=['a','b','c'] , name="Prathamesh Marks")
print(marks)

names = pd.Series(
    {'a': 'Alice', 'b': 'Bob', 'c': 'Charlie'} , name="Names"
)
print(names)


#Series Attributes :

#size 

print("Size of Series : ",marks.size)

#dtype

print("Data type of Series : ",marks.dtype)

#name 

print("Name of Series : " , marks.name)

#is_unique

print("Is Series Unique : ",marks.is_unique)

marks = pd.Series([1,1,1,2,3,4,5,6,7,8,9] , name = "Marks"  , index = ['a','b','c','d','e','f','g','h','i','j','k'])
print("Is Series Unique : ",marks.is_unique)

# index

print("Index of Series : ",marks.index)

#values

print("Values of Series : ",marks.values)