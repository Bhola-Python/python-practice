def is_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter number : "))
is_fibonacci(n)
 