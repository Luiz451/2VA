frase = input("Digite uma frase: ")

vogais = ["a", "e", "i", "o", "u"]
numVogal = 0

for i in frase:
	if i in vogais:
		numVogal += 1

print(numVogal)