numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for k in numbers:
    is_prime = True
    counter = 0
    for i in range(2, k + 1):
        if k % i == 0:
            counter += 1
    if counter == 1:
        primes.append(k)
    elif counter > 1:
        not_primes.append(k)
print(f'Простые числа: ', primes)
print(f'Составные числа: ', not_primes)
