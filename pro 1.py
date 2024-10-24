print("hello baba")

# print the first 10 prime number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2

while len(primes) < 10:
    if is_prime(num):
        primes.append(num)
    num += 1

#print(primes)



#create list of primes multipled by 2
primes_multiplied_by_2 = [p * 2 for p in primes]
print(primes_multiplied_by_2)

