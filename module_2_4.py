numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

#is_prime  = True

for i in numbers:
    if i  ==  1:
        continue
    elif i == 2:
        primes.append(i)

    else:
        for j in range(2, i):
           # print(j)
            if i % j == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)



print('primes', primes)
print('not_primes', not_primes)