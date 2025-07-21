sum = 0

numInt = int(input("Escolha um número inteiro positivo: "))

for i in range(numInt+1):
	if i % 2 == 0:
		sum += i

print(sum)