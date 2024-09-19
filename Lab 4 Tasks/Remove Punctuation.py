# Task 3: Remove Punctuation from User Input 
# This Python script removes punctuation from a user-provided input string without using any built-in string or list methods like remove().


text = input("Write a text here: ")
Punctuations = """.,?!:;'"()[]{}-—../\\&*@#_|~"""
new_text = ""             
for i in text:
    if i not in Punctuations:
        new_text += i
        

print(new_text)


            
