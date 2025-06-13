def reversed_index_mapper(text):
    
    freq = {}
    
    new = text[::-1]
    
    print('Reversed : ',new)
    print('Original : ',text)
    
    for i in range(len(text)):
        freq[text[i]] = new[i]
        
    print(freq)
    
    
text = input('Enter : ')

reversed_index_mapper(text)