def vowels_consonant(text):
    
    vowel = 'aeiou'
    
    no_vowel = 0
    no_consonant = 0
    
    for i in text.lower(): # Input in lower letters
            if i.isalnum(): # Ignore Symbols 
                if i.isalpha(): # Ignore digits 
                    if i in vowel: 
                        no_vowel += 1
                    else:
                        no_consonant += 1
                        
    return no_vowel, no_consonant
                    
text = input('Enter : ') 

total_vowel, total_consonant = vowels_consonant(text)

print('The Total number of vowel : ',total_vowel)
print('The Total number of consonant : ',total_consonant)
                    
                    
                