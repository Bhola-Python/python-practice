def even_index_square(n):
    
    output = []
    
    user_input = n.split()
    print('Input : ',user_input)
    
    for i in user_input:
        if i.isdigit():
            digit = int(i)
            if digit % 2 == 0:
                squared = pow(digit,2)
                output.append(squared)
                
    return output 


n = input('Enter : ')
                
result = even_index_square(n)

print('Final result : ',result)            




