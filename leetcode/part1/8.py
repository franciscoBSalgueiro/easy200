user_input = input().split(',')
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])  
        


length = int(user_input[2])
total = str(user_input[0])+ str(user_input[1])
c = 0
cont = 0
temp = 0
out = 0

# while len(total) - length >= length:
#     temp = int(total[cont:length])
#     if temp > out:
#         out = temp
#     cont += 1
#     total = total[length:]

# output = out

for i in range(len(total)- length):
    if total[i]>temp :
        temp = total[i]
        c = i
for i in range (len(total[:c+1])):




while len(total) - length >= length:










print(output)