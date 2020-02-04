def fibosum(n):
    a = 0
    b = 1
    d = 0
    for i in range(n):
        c = b + a
        a = b
        b = c
        d = d + a
    return d


print("Sum of the first 5 terms of the Fibonacci series", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series", fibosum(10))
