def index_wise(text):
    
    freq = {}
    
    for index,char in enumerate(text):
        freq[index] = ord(char) # ord provides unique value of given letter
        
        
    print(freq)
    
text = input('Enter : ')

index_wise(text)