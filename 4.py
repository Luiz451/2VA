def maior_numero(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero 
    return maior