def square(a , b):
    for i in range(a, b+1):
        yield i*i

a , b  = int(input()), int(input())

lst = square(a, b)
print(*lst)