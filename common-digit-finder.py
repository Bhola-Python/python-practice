def common_digit_finder(num1, num2):
    if num1.isdigit() and num2.isdigit():  # Check if both inputs contain only digits
        set_num1 = set(num1)
        set_num2 = set(num2)

        print('Set of digits in number 1:', set_num1)
        print('Set of digits in number 2:', set_num2)

        result = set_num1.intersection(set_num2)  # Find common elements between sets

        if result:
            print('Common digits:', ", ".join(sorted(result)))
        else:
            print('No common digits found.')
    else:
        print('Invalid input. Please enter only positive whole numbers.')

# User input
num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')

common_digit_finder(num1, num2)
