
a = 0
b = 1

for i in range(11):
    c = b + a
    a = b
    b = c
    print(a, end=' ')
