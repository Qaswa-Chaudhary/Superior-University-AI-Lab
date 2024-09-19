# Alphabetical Text Sorter (Python)
# This Python script sorts the characters of a given word or text in alphabetical order without using the built-in sort() function.

word = list(input("Enter a word or a line of text:"))
temp = ""

for i in range(0,len(word)):
    for j in range(i+1, len(word)):
        if word[i].lower() > word[j].lower():
            temp    = word[i]
            word[i] = word[j]
            word[j] = temp 
new_text = " ".join(word)          
print(new_text)