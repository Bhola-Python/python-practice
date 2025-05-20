def largest(num):
    max_digit = -1 
    for i in num:
        if i.isdigit(): # checks strings has number or not
            if int(i) > max_digit: 
                max_digit = int(i)
                
    return max_digit

num = input('Enter : ')

if num.isdigit():
    result = largest(num)
    print('The Largest digit is ',result)
else:
    print('Invalid Input ! ')
                