def even_index_character(text):
    
    freq = {}
    
    for index, char in enumerate(text):
        if index % 2 ==0 :
            freq[index] = char
            
    print(freq)        
        
        

text = input('enter : ').lower().replace(' ','')

even_index_character(text)
