def is_even(n):
    
    even_index = []
    even_number = []
    sum_of_them = 1
    
    for index, char in enumerate(n):
        if index % 2 == 0 and char.isdigit(): 
            digit = int(char)
            even_index.append(index)
            even_number.append(digit)
            multi_of_them*=digit
    
    print('Total index : ',even_index)
    print('Numbers at index positio : ',even_number)
    print('Total Number at Even index : ',multi_of_them)
       
    
n = input('Enter : ')

is_even(n)