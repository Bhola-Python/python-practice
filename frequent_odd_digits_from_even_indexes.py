def frequent_odd_digit_from_even_indexes(n):
    
    digits_at_even = []
    odd_digit_in_digits = []
    freq = {}
    output = []
    
    
    cleaned = n.replace(' ','')
    print('Cleaned : ',cleaned)
    
    for count,digit in enumerate(cleaned):
        if count % 2 == 0 and digit.isdigit():
            int_digit = int(digit)
            digits_at_even.append(int_digit)
            
    
    for i in digits_at_even:
        if i % 2 != 0:
            odd_digit_in_digits.append(i)
            
    for i in odd_digit_in_digits:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
            
    
    for digit , counts in freq.items():
        if counts > 1:
            output.append(digit)
            
    return digits_at_even,odd_digit_in_digits,output
    

n = input('Enter : ')

result_digit_at_even, result_odd_digit_in_digits , result_output   = frequent_odd_digit_from_even_indexes(n)

print('Result digit at even indexes : ',result_digit_at_even)
print('Result Odd digit in digits : ',result_odd_digit_in_digits)
print('Final Output : ',result_output)