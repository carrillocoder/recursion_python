

def suma_pares(n):
    # Trabajamos siempre con el valor absoluto por si el numero es negativo
    n = abs(n)

    # CASO BASE: no quedan digitos por procesar
    if n == 0:
        return 0

    ultimo_digito = n % 10      # extrae el ultimo digito
    resto         = n // 10     # numero sin el ultimo digito

    # CASO RECURSIVO (digito par): lo suma y continua con el resto
    if ultimo_digito % 2 == 0:
        return ultimo_digito + suma_pares(resto)

    return suma_pares(resto)


entradas = [16582234, 13553]

print("  SUMA DE DIGITOS PARES - Recursion")


for numero in entradas:
    resultado = suma_pares(numero)
    print("Numero  : " + str(numero))
    print("Resultado: " + str(resultado))

