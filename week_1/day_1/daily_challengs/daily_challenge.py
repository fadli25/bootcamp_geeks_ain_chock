# ------ Challenge 1

number = int(input("Enter a number: "))
length = int(input("Enter the lenght: "))
multiple_number = 0
multiple_list = []

for i in range(1 , length + 1):
    multiple_number += number
    multiple_list.append(multiple_number)

print(multiple_list) 

# ------ Challenge 2

word = input("Enter a word: ")

result = word[0] if word else ""

for i in range(1 , len(word)):
     if word[i] != result[-1]:
          result += word[i]

print(result)
