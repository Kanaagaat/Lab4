def gener(n):
    for i in range(1, n + 1):
        yield i*i

n = int(input())
lst = gener(n)
print(*lst)