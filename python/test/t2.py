#!/usr/bin/env python3


l1=[1,2,3,4,5]
l2=[7,8,9]
l3=['a','b','c','d']
lf=map(lambda x,y,z: (x,y,z), l1,l2,l3)

print(list(lf))


print(list(zip(l1,l2,l3)))