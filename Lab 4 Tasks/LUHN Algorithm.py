# Task 4: LUHN Algorithm Credit Card Validator - Python Mini Project


while True:
    card_num = input("Enter a 16-digit card number:").replace("-", "").replace(" ", "")
    if len(card_num) == 16 and card_num.isdigit():
        break
    else:
        print("Invalid input. Please enter exactly 16 digits.")

card_num = list(card_num)


print("\nStep 1")
last_index = card_num[-1]
print("Value at last index:", last_index)
card_num[-1] = "X"

print(card_num)

print("\nStep 2")
reversed_card_num = card_num[::-1]
print(reversed_card_num)

print("\nStep 3")
for i in range(1,len(reversed_card_num), 2):
    if reversed_card_num [i].isdigit():
        reversed_card_num [i] = str(int(reversed_card_num [i]) * 2)
print(reversed_card_num)

print("\nStep 4")
new_card_num = []
for item in reversed_card_num:
    if item.isdigit():
        num = int(item)
        if num > 9:
            x = num - 9
            new_card_num.append(x)
        else:
           new_card_num.append(item)
    else:
        new_card_num.append(item)
print(new_card_num)            

print("\nStep 5")
new_card_num[0] = last_index
print(new_card_num)
# total sum 
new_card_num = [int(item) for item in new_card_num]
total_sum = sum(new_card_num)
print("Total sum of all numbers: ",total_sum)

print("\nStep 6")
if total_sum % 10 == 0:
    print("card is valid")
else:
    print("Card is invalid")
