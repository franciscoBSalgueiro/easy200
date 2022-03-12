user_input ="1,3,2,2"

notas = []
for n in user_input.split(","):
    notas.append(int(n))


for i, n in enumerate(notas):
    if i<len(notas)-1:
        dif = notas[i+1]-n-1
        if dif>=1 and all(c-dif>=1 for c in notas[i+1:]):
            for j, c in enumerate(notas[i+1:]):
                notas[1+i+j] = c-dif

print(sum(notas))
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
