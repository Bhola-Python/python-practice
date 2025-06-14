def digit_frequency_at_even_index(text):
    freq = {str(i) : 0 for i in range(10)}
    
    for i in range(len(text)):
        if i % 2 == 0:
            if text[i].isdigit():
                freq[text[i]] += 1
                
    print('Digit frequency at even indexes')
    
    for digit, count in freq.items():
        if count > 0:
            print(f"{digit} : {count}")
            
            
text = input('Enter : ')

digit_frequency_at_even_index(text)