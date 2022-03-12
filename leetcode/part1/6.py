user_input = input()
alunos = user_input.split(",")
i = 0
notas = []
for i in alunos:
    if alunos[i] > alunos[i+1] and alunos[i] > alunos[i-1]:
        nota = (alunos[i] + 1)

    if i == alunos[0]:
        if alunos[i] > alunos[i+1]: 

    if i == alunos[-1]:
        if alunos[i] > alunos[i-1]: 


print(output)