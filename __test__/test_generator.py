def squares(n=10):
    for i in range(n):
        yield(i,i**2)


for x in squares(20):
    print(x)