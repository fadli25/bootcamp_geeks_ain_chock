# ------ Exercise 1

my_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

my_list = my_string.split(",")

print(f"They are {len(my_list)} companies in this list.")

my_list.sort(reverse=True)

print("List of companies: ",end="")

for x in my_list:
    if x != my_list[-1]: print(x,end=", ")
    else: print(x,end=".")

print("")

find_o = 0
find_i = 0

for i in my_list:
    if "o" in i : find_o += 1
    if "i" not in i : find_i += 1


print(f"The number of manufacturers’ names have the letter 'o' is: {find_o}")
print(f"The number of manufacturers’ names do not have the letter 'i' is: {find_i}")

new_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
new_list = list(set(new_list))

print(f"The companies is: {", ".join(new_list)}.")
print(f"We have now {len(new_list)} companie")

companie_list= []

for companie in new_list:
    letter_list = list(companie)
    letter_list.reverse()
    companie_list.append("".join(letter_list))

companie_list.sort()

for compaie in companie_list:
    print(compaie)

# ------ Exercise 2

def get_full_name(*args):
    if len(args) > 2:
        first_name , middle_name, last_name = args
        return f"{first_name} {middle_name} {last_name}"
    
    first_name , last_name = args
    return first_name + " " + last_name

print(get_full_name("ahmad","kamal","jamal").title())

# ------ Exercise 3

morse_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-','@': '.--.-.', ' ': '/', ' ': "#"
}

message = input("Enter your message: ").strip()

message = message.split(" ")

message_code = []

for ms in message:
    ms = list(ms)

    print(ms)
    my_code = ""
    for m in ms:
        print(m)
        my_code += str(morse_dict[m.upper()])

    message_code.append(my_code)

print("#".join(message_code))