def word_frequency(sentence):
    words = sentence.lower().split()  # Convert to lowercase & split into words
    freq = {}  # Dictionary to store word counts

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

# Input
sentence = input("Enter a sentence: ")

# Function Call
result = word_frequency(sentence)

# Output
print("Word Frequencies:")
for word, count in result.items():
    print(f"{word}: {count}")
