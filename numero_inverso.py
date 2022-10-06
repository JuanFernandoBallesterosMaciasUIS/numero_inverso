
numero = int(input("Digita un número entero y positivo: "))
n1 = numero

inverso = 0

while numero > 0:
    # Tomamos el último número
    ultimo_numero = numero % 10

    # Agregamos al inverso
    inverso = inverso * 10 + ultimo_numero

    # Descuentamos el último número del número original
    numero = numero // 10

print("El número ingresado es:",n1)
print("El  número inverso es :",inverso)
