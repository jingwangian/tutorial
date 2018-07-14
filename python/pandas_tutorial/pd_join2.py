#!/usr/bin/env python3
import numpy as np
import pandas as pd

"""
"Orders" table:
OrderID	CustomerID	OrderDate
10308	2	1996-09-18
10309	37	1996-09-19
10310	77	1996-09-20


Customers table:
CustomerID	CustomerName	ContactName	Country
1	Alfreds Futterkiste	Maria Anders	Germany
2	Ana Trujillo Emparedados y helados	Ana Trujillo	Mexico
3	Antonio Moreno Taquería	Antonio Moreno	Mexico

"""
def print_info(msg):
    print("*"*40)
    print("command: {}".format(msg))
    print(eval(msg))
    print('')


df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})

df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],'data2': range(10,15)})

print_info("df1")
print_info("df2")

jointb=pd.merge(df1,df2,on='key')

print(jointb)

tb3 = pd.merge(df1,df2,on='key',how='left')

tb4 = tb3.sort_values(by="key")

print_info("tb3")
print(tb4)




# tb3 = jointb.groupby("data2")
#
# print_info("tb3")