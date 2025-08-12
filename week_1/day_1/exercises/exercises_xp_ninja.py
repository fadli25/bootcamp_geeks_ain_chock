# ------ Exercise 1

# 3 <= 3 < 9 => True
# 3 == 3 == 3 => True
# bool(0) => False
# bool(4==4) == bool("4" == "4") => True
# true
# false 
# 5
# 10

# ------ Exercise 2

word = ""
user_word = input("Enter a word: ")

while "A" not in user_word and len(user_word) > len(word):
    print("Congratulations!")
    word = user_word
    user_word = input("Enter a word: ")

# ------ Exercise 3

word = ""
user_word = input("Enter a word: ")

while "A" not in user_word and len(user_word) > len(word):
    print("Congratulations!")
    word = user_word
    user_word = input("Enter a word: ")

# Exercise 3:

pargraph = "Programming is like solving a puzzle. Each line of code is a small piece, and when they all come together, they create something meaningful. It requires patience, creativity, and logical thinking. Just like any skill, the more you practice, the better you become."
pargraph_1 = pargraph

print("Number of chararcters: ", len(pargraph))
print("Number of sentences: ", pargraph.count("."))

while "." in pargraph_1:
    pargraph_1 = pargraph_1.replace(".","")

while "," in pargraph_1:
    pargraph_1 = pargraph_1.replace(",","")


pargraph_1 = pargraph_1.split(" ")

print("Number of words: ", len(pargraph_1))

#bonus

pargraph_1 = set(pargraph_1)

print("non-whitespace characters: ",len(pargraph_1))

pargraph = pargraph.split(".")
pargraph.pop()


#bonus
new_paragraph = [];

for sentence in pargraph:
    sentence = sentence.split(" ")
    new_paragraph.append(sentence)



i = 0
for sentence in new_paragraph:
    i += 1
    avg = len(sentence) / len(pargraph)
    print(f"avrage of words in sentnece {i}: {avg:0.2f}")

