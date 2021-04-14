def check_prime_number(Number):
    flag = 0
    for i in range(2,int(Number/2)+1):
        if Number%i == 0:
            flag = 1
            return "Not prime number"
    if flag == 0:
        return "Prime Number"