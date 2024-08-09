import os
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# for i in range(36):
#     print(i, fib(i))



listing = os.walk('.')


for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)
