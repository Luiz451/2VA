def IMC(peso, altura):
    if altura <= 0:
        return "Altura inválida."
    if peso <= 0:
        return "Peso inválido."
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade grau 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"
'''
Abaixo de 18.5: Abaixo do peso
18.5 até 24.9: Peso normal
25.0 até 29.9: Sobrepeso
30.0 até 34.9: Obesidade grau 1
35.0 até 39.9: Obesidade grau 2

'''