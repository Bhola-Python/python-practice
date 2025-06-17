def space_separated_string(n):
    
    odd_lst = []
    
    user_input = n.split()
    print('User Enter : ',user_input)
    
    user_string = ''.join(user_input)
    
    for i in user_string:
        if i.isdigit():
            digit = int(i)
            if digit % 2 != 0 and digit > 3:
                odd_lst.append(digit) 
    
    
    multiply_lst = [i*2 for i in odd_lst]
    
    print('Multiplied Odd list : ',sorted(multiply_lst))
    
n = input('Enter : ')

space_separated_string(n)