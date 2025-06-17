def square_digit_inside_multi_digit_number(n):
    square_output = []
    even_index = []
    
    user_input = n.split()
    print('Input : ',user_input)
    
    new_string = ''.join(user_input)
    
    for i in new_string:
        if i.isdigit():
            digit = int(i)
            if digit % 2 == 0:
                even_index.append(digit)
                squared = pow(digit,2)
                if squared > 0: 
                    square_output.append(squared)
                
    return even_index , square_output

n = input('Enter numbers: ')
result_even, result_square = square_digit_inside_multi_digit_number(n)

print('Even digits:', result_even)
print('Squared even digits:', result_square)



            
            


        