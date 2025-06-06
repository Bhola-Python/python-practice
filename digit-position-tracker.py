def digit_position(n):
    freq = {}  # Dictionary to store digit positions
    
    for index, char in enumerate(n):
        if char.isdigit():
            if char not in freq:
                freq[char] = []  # Initialize list for new digit
            freq[char].append(index)  # Add index to digit's list
    
    print(freq)

# Input from user
n = input('Enter a string of digits: ')
digit_position(n)

            
            
    