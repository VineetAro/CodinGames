import sys
import math

num = 0
w, h, count_x, count_y = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
dif_x= []
y =[int(i) for i in input().split()]
dif_y = []
x.append(w)
y.append(h)

for i in sorted(x):
    for j in sorted(x, reverse=True):
        if i!=j:
            dif = j-i
            if dif>0:
                dif_x.append(dif)

for i in sorted(y):
    for j in sorted(y, reverse=True):
        if i!=j:
            dif = j-i
            if dif>0:
                dif_y.append(dif)

x.extend(dif_x)
y.extend(dif_y)

for i in x:
    inc = y.count(i)
    num+=inc 
print (num)