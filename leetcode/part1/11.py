user_input = input()
pw = user_input
inserir = 0 
modificar = 0
remover = 0
passos = inserir + modificar + remover

n_char = len(pw)

if n_char < 8: #preciso inserir
    inserir += 1

if n_char > 20: #preciso remover
    remover += 1

if "!" not in pw or "?" not in pw or "-" not in pw or "_" not in pw or\
    "$" not in pw or "%" not in pw or  "&" not in pw:

    modificar += 1

counter = 0
list_pw = list(pw)
for l in pw: #preciso remover ou inserir ou alterar
    if list_pw[l - 1] == list_pw[l] == list_pw[l + 1]:
        modificar = 


print(output)