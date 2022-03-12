user_input = input().split(',')

ana = user_input[0]
scooby = user_input[1]
atual = user_input[2]



# if eval(ana [4:]) < eval(scooby [4:]):
#     output = 'true'
    
# elif eval(ana [4:]) > eval(scooby [4:]):
#     output = ' false'
# elif eval(ana[4:]) == eval(scooby [4:]):
#     if eval(ana [2:4]) < eval(scooby [2:4]):
#         output = 'true'
#     elif eval(ana [2:4]) > eval(scooby [2:4]):
#         output = 'false'
#     elif eval(ana [2:4]) == eval(scooby [2:4]):
#         if eval(ana [0:2]) < eval(scooby [0:2]):
#             output = 'true'
#         elif eval(ana [0:2]) >= eval(scooby [0:2]):
#             output = 'false'




def calculateAge(yb,ym,yd,y,m,d):
	try:
		birthday = yb.replace(year = y)

	except ValueError:
		birthday = born.replace(year = y,
				month = mb + 1, day = 1)

	if birthday > today:
		return today.year - born.year - 1
	else:
		return today.year - born.year
		


ana = calculateAge(date(eval(ana [4:]), eval(ana [2:4]), eval(ana [0:2]), eval(atual [4:]),eval(atual [2:4]),eval(atual [0:2])))

scooby = 7* calculateAge(date(eval(scooby [4:]), eval(scooby [2:4]), eval(scooby [0:2]), eval(atual [4:]),eval(atual [2:4]),eval(atual [0:2])))

print(output)
