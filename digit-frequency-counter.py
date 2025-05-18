def digit_frequency_counter(number):
    
    freq = {str(i): 0 for i in range(10)}
    
    for char in number:
        if char.isdigit():
          freq[char] += 1
        
    for digit in freq:
        print(f'Digit {digit} appears {freq[digit]} times')
        
        
number_input = input('Enter a positive number : ')
    
    
digit_frequency_counter(number_input)