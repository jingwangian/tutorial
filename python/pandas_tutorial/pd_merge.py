#!/usr/bin/env python3
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})

df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})


df3 = pd.merge(df1, df2)
print(df3)

# df3 = pd.merge(df1,df2, left_index=True, right_index=True)
# print(df3)

df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})

df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})

print(pd.merge(df3, df4))

print(pd.merge(df1, df5))

df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})

print(pd.merge(df1, df3, left_on="employee", right_on="name"))

pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)

df1a=df1.set_index(keys="employee")
df2a=df2.set_index(keys="employee")
print(df1a); print(df1)
