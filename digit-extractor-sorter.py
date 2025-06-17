def digit_extractor_sorter(n):
    freq = {}
    
    lst = []
    
    user_input = n.split()
    
    print('Input : ',user_input)
    
    new_string = ''.join(user_input)
    
    for i in new_string:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i]+=1
            
    for index, char in freq.items():
        if index.isdigit():
            digit = int(index) 
            if char < 2: 
                lst.append(digit)
                lst.sort()
            
    return lst

n = input('Enter : ')
    
result = digit_extractor_sorter(n) 

print('The final output : ',result)