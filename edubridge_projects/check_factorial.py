def factorial(Number):
    res = 1
    for i in range(1,Number+1):
        res *= i
    return res

def odd_Even(Number):
    if Number%2 == 0:
        return "Even"
    else:
        return "Odd"