'''Index Letter Mapper

Write a program that takes a string as input and stores each character with its index
in a dictionary.
'''

def index_letter(inpu):
    for index, char in enumerate(inpu):
        print(index,char)
        
inpu = input('Enter : ').lower().replace(' ','')

result = index_letter(inpu)

print('Index Letter Mapper')

for idx, val in result.items():
    print(f"{idx}: {val}")
        

