def sum_fib_index_digits(n):
    
    fib_indexes = []
    a, b = 0, 1
    while a < len(n):
        fib_indexes.append(a)
        a, b = b, a + b


    digits_at_fib = []
    for index in fib_indexes:
        if n[index].isdigit():
            digits_at_fib.append(int(n[index]))


    total = sum(digits_at_fib)

    print("Fibonacci Indexes:", fib_indexes)
    print("Digits at Fibonacci indexes:", digits_at_fib)
    print("Sum : ", total)


n = input("Enter Digits : ")

sum_fib_index_digits(n)
