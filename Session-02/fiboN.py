# Fibonacci funtion


def fibon (n):
    a = 0
    b = 1
    for i in range(n+1):
        c = b + a
        a = b
        b = c
        return(a)

print(fibon(5))