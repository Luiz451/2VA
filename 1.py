list = [True, False, True, False, True]

numTrue = 0
numFalse = 0

for i in list:
	if i:
		numTrue += 1
	else:
		numFalse += 1
		
print(numTrue,numFalse)