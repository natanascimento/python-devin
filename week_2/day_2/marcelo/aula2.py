

def fibo(n):
    i = 0
    fibos = [1, 1,]
    while i <= n:
        fibos.append(fibos[i] + fibos[i + 1])
        i += 1
    return fibos

print(fibo(15))