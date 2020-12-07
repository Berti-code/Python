import math

def read():
    n_string=input('N=')
    n_int=0
    n_int=int(n_string)
    search_prime_number(n_int)

def is_prime(number):
    count=0
    sqrt_n=int(math.sqrt(number)+1)
    for i in range(2,sqrt_n):
        if number%i == 0:
            count=count+1
            break
    if count>0: return 0
    else:  return 1
    
def search_prime_number(number):
    while is_prime(number) == False:
        number=number+1
    print("The first prime number larger than N is: " , number)

read()