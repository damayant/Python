import sys,gc 

x = [1,2,3]
print(sys.getrefcount(x))

y=x 
print(sys.getrefcount(y))

del y
print(sys.getrefcount(x))

gc.collect()


