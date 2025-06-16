def list_problem(n):
    
    new_list = []
    user_input = n.split()
    print(user_input)
    new_string = ''.join(user_input)
    for i in  new_string:
        if i.isdigit():
            digit = int(i) 
            new_list.append(digit)
        
    return new_list
 
n = input('enter : ')        
 
result = list_problem(n)

print('The answer is : ',result)

