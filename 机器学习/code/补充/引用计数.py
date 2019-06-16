import sys
x=1
print(sys.getrefcount(x))
y=x
print(sys.getrefcount(x))
z=y
print(sys.getrefcount(x))
x=2
print(sys.getrefcount(z))