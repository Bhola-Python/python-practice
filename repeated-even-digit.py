def repeated_even_digit_from_odd_indexes(n):
    
    odd_indexes = []
    even_indexes = []
    final = []
    freq = {}
    
    
    cleaned = n.replace(' ','') # removing spaces 
    print('String : ',cleaned)
    
    for index, char in enumerate(cleaned):
        if index % 2 != 0  and char.isdigit():
            digit = int(char)
            odd_indexes.append(digit)
            
    
    for index, char in enumerate(odd_indexes):
        if char % 2 == 0:
            even_indexes.append(char)
            
    
    
    for i in even_indexes:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    
    for digit, count in freq.items():
        if count > 1:
            final.append(digit) 
            
    return odd_indexes, even_indexes, final
               
    
n = input('Enter : ')

result_odd, result_even , result_final = repeated_even_digit_from_odd_indexes(n)

print('Digits at odd indexes : ',result_odd)
print('Even indexes : ',result_even)
print('Final Result : ',result_final)