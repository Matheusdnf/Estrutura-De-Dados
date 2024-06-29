import time
import random

def insertion_sort(v,n):
    for i in range(1, n):
        j = i
        while ((j > 0 ) and (v[j] < v[j - 1])):
            aux = v[j]
            v[j] = v[j - 1]
            v[j - 1] = aux
            j=j-1
            
v=[65,4,65,13,48,189,48,1,894,531321,3,2,981,98,105,198,16,840,8]
n=len(v)
insertion_sort(v,n)
print(v)
