#problema do troco
def troco(list_moedas, valor):
    minimo_moedas = valor
    if valor in list_moedas:
        return 1
    else:
        for i in [c for c in list_moedas if c <=valor]:
            numero_moedas = 1 + troco(list_moedas, valor-i)
            if numero_moedas < minimo_moedas:
                minimo_moedas = numero_moedas
    return minimo_moedas

print(troco([1,2,8,14,25], 28))