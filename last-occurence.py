def last_occurence_index_finder(n):
    freq = {}

    for index, char in enumerate(n):
        if char.isdigit():
            freq[char] = index  # Always update with the latest index (last occurrence)

    print(freq)

n = input('Enter: ')
last_occurence_index_finder(n)
