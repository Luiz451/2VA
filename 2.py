def calculo_troco(valor_pago, valor_total):
    if valor_pago < valor_total:
        return "Valor pago é menor que o valor total."
    elif valor_pago == valor_total:
        return "Não há troco."
    
    troco = valor_pago - valor_total
    return f"Troco: R$ {troco:.2f}"