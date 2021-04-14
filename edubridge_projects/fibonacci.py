"""
n = 1
m = 0
o = 1
print("0")
for i in range(int(input("enter limit"))):
    print(n)
    o = n
    n = m+n
    m = o
"""
o = 0
n = 0
m = 1
i = 0
while(i<10):
    print(o)
    o = n+m
    n = m
    m = o
    i+=1

