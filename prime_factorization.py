mylist = [ ]

def prime_factors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2


    # n must be odd at this point
    # so adding 2 in i could be used
    for i in range(3, (int(n ** 0.5) + 1)):

        # while i divides n , print i ad divide n
        while n % i == 0:
            mylist.append(int(i))

            n = n / i
        i += 2

    # append n if n is a prime
    # and is greater than 2
    if n > 2:
        mylist.append(int(n))

    return mylist

print(prime_factors(34352))
