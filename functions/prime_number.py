def prime_number(num):
    if num <=1:
            return f"{num} is not prime number"
    else:
        for i in range(2,num):
            if num % i ==0:
                return f"{num} number is not prime number"
            else:
                return f"{num } is prime number"

print(prime_number(11))
