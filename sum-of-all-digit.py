def Total_value(num):
    sum_value = 0
    for i in num:
        if i.isdigit():
            sum_value += int(i)
    return sum_value

number = input('Enter Number : ')

final_value = Total_value(number)

print('The final result is ',final_value)