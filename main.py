def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes

num = int(input("Введите натуральное число: "))
print(f"Простые числа до {num}: {sieve_of_eratosthenes(num)}")
