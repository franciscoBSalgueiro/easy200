user_input = input().split(',')
output = ''

for i in range(len(user_input[0])):
    if (ord(user_input[i]) >= 97 and ord(user_input[i]) <=122) or\
        (ord(user_input[i]) >= 65 and ord(user_input[i]) <=90):
        output += user_input[i]


#print(output)