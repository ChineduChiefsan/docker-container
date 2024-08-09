def fact(n):
    """calculate n interatively"""
    result = 1
    if n> 1:
        for f in range(2,n+1):
            result *=f
    return result

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
for i in range(100):
    print(i, factorial(i))


