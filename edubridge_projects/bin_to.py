"""
1. Write a Python program to remove duplicates from a list.
2. Write a Python program to find the list of words that are longer than n from a given list of words.
3. Write a Python program to add an item in a tuple.
4. Write a Python program to find the repeated items of a tuple.


"""

"""
def data_in():
    data = list(input().split())
    return data

#1
print("1. Write a Python program to remove duplicates from a list.")
l = data_in()

print(set(l))
#2
print("2. Write a Python program to find the list of words that are longer than n from a given list of words.")
res = []
m = data_in()
for i in m:
    if(len(i)<=5):
        res.append(i)
print(res)
print("3. Write a Python program to add an item in a tuple.")
t = data_in()
print(tuple(t))
print("4. Write a Python program to find the repeated items of a tuple.")
r = []
for i in tup:
    if(tup.count(i)>1 and i not in res):
        r.append(i)
print(r)


"""



def length(l,n):
    res = []
    for i in l:
        if (len(i)>n):
            res.append(i)
    return res
lis = ["apple","mango","lemonade","jackfruit","brinjal","litchi","orange"]
n = int(input("enter number"))
print(length(lis,n))







