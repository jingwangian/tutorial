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


columns1 = "OrderID	CustomerID	OrderDate".split()

data1 = """10308	2	1996-09-18
10309	37	1996-09-19
10310	77	1996-09-20
"""

tb1 = pd.DataFrame([x.split() for x in data1.splitlines()], columns=columns1)

print(tb1)


columns2='CustomerID	CustomerName	ContactName	Country'.split()
data2 = """1	Alfreds_Futterkiste	Maria_Anders	Germany
2	y_helados	Ana_Trujillo	Mexico
3	Moreno_Taquería	Antonio_Moreno	Mexico
"""
# print([x.split() for x in data2.splitlines()])
# print(columns2)
tb2 = pd.DataFrame([x.split() for x in data2.splitlines()], columns=columns2)
print_info("tb2")

tb3 = pd.merge(tb1,tb2)

print_info("tb3")

tb4 = pd.merge(tb1,tb2,how='left')

print_info("tb4")

se1 = tb4['CustomerID']

print(se1, type(se1))
print(se1.index)
print(se1.values)

se2 = pd.Series(se1,dtype='int64')

print(se2.values)

tb5 = tb4[se2>2]

print(tb5)
# tb4["Country"]="a"

tb6 = tb4[tb4["Country"].isnull()]
print(tb4["Country"])
print(tb6)
print(tb4["Country"].isnull())
# print(se1[se1>2])
# print_info("tb4[tb4['Country']=='NaN']")