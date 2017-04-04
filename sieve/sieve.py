def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def sieve(limit):
    if limit < 2:
        return []
    primes = [i for i in range(2, limit) if is_prime(i)]
    if is_prime(limit):        
        primes.append(limit)

    return primes
