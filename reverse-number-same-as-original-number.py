def original_reverse(num):
    if num.isdigit(): #Identify The string is in number or not
        original = num 
        reverse = original[::-1] # Assigning new varible to original sliced number
        print('Original Number : ',original)
        print('Reverse Number : ',reverse)
        
        if original == reverse: # Checks if both the variables are same
            print('The Input number is palindrome')
        else:
            print('It is not Palindrome')
            
            
    else:
        print('Invalid Input Enter Valid input')
        
        
number = input('Enter the Number : ')
original_reverse(number)
