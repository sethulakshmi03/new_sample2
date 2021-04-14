"""
1.  Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
    also create a lambda function that multiplies argument x with argument y and print the result
2. Write a Python program to square and cube every number in a given list of integers using Lambda.
3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

   Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
4. Write a Python function that checks whether a passed string is palindrome or not. Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
5. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

"""
#1

def power_(l):
    sqrr = list(map(lambda x:x**2,l))
    cube = list(map(lambda x:x**3,l))
    print("Squares: ",sqrr)
    print("Cubes: ",cube)
def cnt_case(s):
    cnt_u = 0
    cnt_l = 0
    for i in s:
        if(i.isupper()):
            cnt_u+=1
        else:
            cnt_l+=1
    print("Number of Upper case: ",cnt_u)
    print("Number of lower case: ",cnt_l)
def check_palindrome(s):

    if(s==s[::-1]):
        print("Palindrome")
    else:
        print("Not Palindrome")
def sqr_among_the_num(l):
    res = [x**2 for x in l if x**2<max(l)]
    print(res)
c = 1
while(c):
    option = int(input("1. lambda function to find number+15 ns multiply x and y\n"
              "2. lambda function for squares and cubes\n"
              "3. Count upper lower cases in a string\n"
              "4. Check palindrome or not\n"
              "5. find out squares amonth the list\n"
              "6. Exit\n"))
    if option == 1:
        a = lambda x:x+15
        b = lambda x,y:x*y
        f = int(input("enter number to be added with 15"))
        s = int(input("enter x"))
        t = int(input("enter y"))
        print("a({0}) = {1} \nb({2},{3})= {4}".format(f,a(f),s,t,b(s,t)))
        input()
    elif option == 2:
        print("enter number separated by space")
        power_(list(map(int,input().split())))
        input()
    elif option == 3:
        cnt_case(input("enter string"))
        input()
    elif option == 4:
        check_palindrome(input("Enetr string o check palindrome"))
        input()
    elif option == 5:
        sqr_among_the_num(list(range(int(input("enter lower limit")),int(input("enter upper limit")))))
        input()
    else:
        c = 0