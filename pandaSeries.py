import pandas as pd
import numpy as np

data=np.array(['a','s','d','f','g'])

#Series is nothing but the one diametnional arrays in python
#Pandas are creating on the top of the Numpy

#Creating a series in python
ser=pd.Series(data)
#Accessing the series element
#print(ser[:8])

series=pd.Series(data,index=[10,11,12,13,14])
print(series[12])
print(series.count())
print(series.is_unique)

address=pd.read_csv("addresses.csv")


address_series=pd.Series(address['John'])
print(address_series)

#Top Five Rows will be selected
data_top=address.head()
print(data_top)

#calling series with n rows
data_top=address_series.head(n=2)
print(data_top)

#for last n rows, bydefault 5
#address.tail()

#Covert a dataframe to numpyArray
address.dropna(inplace=True)
#pd_to_ndarray=pd.DataFrame(data['8075'].head())
#print(address_series.a)
#print(pd_to_ndarray.to_numpy())

data={
        "No":[1,2,3,4],
        "Name":["Dhiraj","Onakar","Shubya","Swapnil"],
        "Marks":[100,200,300,410]
    }

df=pd.DataFrame(data)

print(df.loc[1]["Name"])

print(df[["Name","Marks"]])

print(df.groupby(["Name","Marks"]).groups)

df["Name"]=df["Name"].str.upper()
print(df["Name"])

import matplotlib.pyplot as plt
plt.style.use('ggplot')
df["Marks"].plot.bar()
plt.show()