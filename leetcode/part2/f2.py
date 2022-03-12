#user_input = input()
user_input = "e2frase4Isto1uma3"
frase_bem_quase = []

for i in user_input:
    if i.isnumeric():
        frase_bem_quase.append(user_input[0: user_input.index(i)+1:])
        user_input = user_input[user_input.index(i) + 1::]
        continue
    else:
        continue

def numero(word):
    return word.index(-1)
frase_bem_quase = frase_bem_quase.sort(key = numero)
""" for word in frase_bem_quase:
    for letter in word:
        if letter.isnumeric():
            word = word.replace(letter, '')
        else:
            continue """



print(frase_bem_quase)

#print(output)