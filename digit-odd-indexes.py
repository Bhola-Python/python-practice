def odd_posi_digit(n):
    odd_index_digit = []
    
    # Collect digits at odd indexes
    for index, char in enumerate(n):
        if index % 2 != 0 and char.isdigit():
            digit = int(char)
            odd_index_digit.append(digit)

    print(odd_index_digit)  # Shows the digits at odd indexes
    
    # Prepare frequency dictionary
    freq = {str(i): 0 for i in range(10)}

    # Count frequency of digits found at odd indexes
    for digit in odd_index_digit:
        freq[str(digit)] += 1

    # Filter out digits that were not found
    freq = {k: v for k, v in freq.items() if v > 0}

    print(freq)


odd_posi_digit(n)