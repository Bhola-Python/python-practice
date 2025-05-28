def most_frequent_digits(number_str):
    freq = {}

    # Count the frequency of each digit
    for char in number_str:
        if char.isdigit():
            freq[char] = freq.get(char, 0) + 1

    # Find the maximum frequency
    if not freq:
        print("No digits found in input.")
        return

    max_freq = max(freq.values())

    # Find all digits with maximum frequency (to handle ties)
    most_freq_digits = [digit for digit, count in freq.items() if count == max_freq]

    print("Frequencies:", freq)
    print("Most Frequent Digit(s):", most_freq_digits)

# Example usage:
number_str = input("Enter a string of digits: ")
most_frequent_digits(number_str)
