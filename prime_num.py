"""Prime numbers are numbers that can only be cleanly divided by themselves and 1."""

def prime_checker(number):
    is_prime = True
    for i in range(2, 100):
        if number % i == 0:
            is_prime = False
#print("It's not a prime number.")

    if is_prime:
        print("It's a prime number.") 
    else:
        print("It's not a prime number.")         

n = int(input("Check this number: "))
prime_checker(number=n)
