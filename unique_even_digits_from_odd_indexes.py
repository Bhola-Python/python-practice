def unique_Even_digtis_from_odd_indexes(n):
    

    digits_at_odd_index = []
    even_digits_only = []
    output = []
    freq = {}

    
    cleaned = n.replace(' ','')
    
    for counts , digit in enumerate(cleaned):
        if digit.isdigit(): # checks input is in digits 
            int_digit = int(digit) # converts into integer
            if counts % 2 !=0:
                digits_at_odd_index.append(int_digit)
                
    for i in digits_at_odd_index:
        if i % 2 == 0:
            even_digits_only.append(i)
    
    for j in even_digits_only:
        if j not in freq:
            freq[j] = 1
        else:
            freq[j] += 1 
            
    for digits, counts in freq.items():
        if counts == 1:
            output.append(digits)
            
    return digits_at_odd_index, even_digits_only, output


n = input('Enter : ')

result_digits_at_odd_index, result_even_digits_only, result_output =  unique_Even_digtis_from_odd_indexes(n)

print('Result at digits at odd indeex : ',result_digits_at_odd_index)
print('Even digits only : ',result_even_digits_only)
print('Final Result : ',result_output)