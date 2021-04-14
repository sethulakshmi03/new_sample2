r = open("Test","r")
for i in r.read().split():
    if "0X" in i:
        print(eval(i)<<1)
