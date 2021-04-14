e_cnt = 0
o_cnt = 0
for i in range(int(input("enter upper lmit")),int(input("enter lower limit"))+1):
    if i%2 == 0:
        e_cnt+=1
    else:
        o_cnt+=1
print("Number of Odd",o_cnt)
print("Number of Even",e_cnt)