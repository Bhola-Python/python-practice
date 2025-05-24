def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_digit(number):
    digits_at_prime_indexes = []
    total = 0
    
    for index, char in enumerate(number):
        if is_prime(index) and char.isdigit():
            digit = int(char)
            digits_at_prime_indexes.append(digit)
            total += digit

    print("Digits at prime indexes:", digits_at_prime_indexes)
    print("Sum of those digits:", total)

number = input('Enter number: ')
sum_digit(number)
