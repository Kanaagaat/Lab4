def gener(n):
    for i in range(n , -1, -1):
        yield i




n = int(input())
lst = gener(n)
print(*lst)