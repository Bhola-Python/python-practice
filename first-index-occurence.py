def first_occurence(n):
    
    freq = {}
    
    for index, char in enumerate(n):
        if char.isdigit(): # checks input is integer
            if char not in freq: 
                freq[char] = index
                        
        
    print(freq)
        
n = input('Enter : ')

first_occurence(n)