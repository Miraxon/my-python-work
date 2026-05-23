def is_prime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n %x==0:
            return False
    return True
n=int(input("Write a number to check if it is prime or not: "))
if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")