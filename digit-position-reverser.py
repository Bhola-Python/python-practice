def digit_position_reverser(number):
    
    reverse = number[::-1] # Reverse the original through slicing
    
    print('Original : ',number)
    print('Reversed : ',reverse)
    
    
    for index,digit in enumerate(reverse): 
        print(f" Position is {index} : {digit}")
    
    
number = input('enter : ')

digit_position_reverser(number)