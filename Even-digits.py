def sum_digits(number):
    if not number.isdigit():
        print("Invalid input. Please enter digits only.")
        return [], 0

    empty_lst = []
    sum_lst = 0
    for i in number:
        digit = int(i)
        if digit % 2 == 0:
            empty_lst.append(digit)
            sum_lst += digit

    return empty_lst, sum_lst


number = input('Enter number: ')
no_digit, sum_digit = sum_digits(number)

if no_digit:
    print('Even digits in it:', no_digit)
    print('Sum of even digits:', sum_digit)

            
