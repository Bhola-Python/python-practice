def digit_alpha(text):
    nos_of_alpha = 0
    nos_of_num = 0
    for i in text:
        if i.isalnum(): # identify string contains number and integers
            if i.isalpha(): # identify numbers
                nos_of_alpha += 1 # value added into the empty variable 
            else:
                nos_of_num += 1
                
    return nos_of_alpha, nos_of_num

text = input('Enter : ')

result_alpha, result_num = digit_alpha(text)

print('The number of letter is ',result_alpha)
print('The number of number is ',result_num)