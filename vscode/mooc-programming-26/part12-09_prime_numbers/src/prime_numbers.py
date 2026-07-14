# Write your solution here
def prime_numbers():
    i = 1
    primes = [2, 3, 5, 7, 11, 13]
    while True:
        i += 1
        c = 0
        if i in primes:
           yield i
        for n in primes:
            if i%n == 0:
                c = 1
                break
        if c == 0:
            primes.append(i)
            yield i
            
