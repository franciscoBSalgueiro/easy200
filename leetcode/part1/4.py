# user_input = input()
from pprint import pprint


user_input = "182,153,449"

user_input = user_input.split(",")
retangulos = []
for r in user_input:
    retangulos.append([])
    for s in r:
        retangulos[-1].append(int(s))


pontos = []
for r in retangulos:
    for x in range(r[0],r[2]+1):
        for y in range(r[1]+1):
            pontos.append((x,y))

pprint(pontos)
output= ""
cantos=[]

for p in pontos:
    if cantos == []:
        cantos.append(p)
        continue
    if x+1==p[0] and x!=1:
        if cantos[-1][1]!=y:
            cantos.append((x,cantos[-1][1]))
        cantos.append((x,y))
    x=p[0]
    y=p[1]
print(sorted(cantos))

print(output)