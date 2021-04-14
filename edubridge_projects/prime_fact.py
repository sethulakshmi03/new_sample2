import check_factorial
import check_prime

n = int(input("Enter number"))

print("Factorial of the entered number is {0}".format(check_factorial.factorial(n)))
print("The entered number is {0}".format(check_prime.check_prime_number(n)))
print("The entered number is {0}".format(check_factorial.odd_Even(n)))