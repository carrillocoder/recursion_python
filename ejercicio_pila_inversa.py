
def mostrar_invertida(pila):
    # CASO BASE: pila vacia, no hay nada que mostrar, se detiene la recursion
    if len(pila) == 0:
        return

   
    tope = pila.pop()        
    print(tope, end=" ")     
    mostrar_invertida(pila)  # llamada recursiva con la pila reducida
    
pila = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("  LABORATORIO RECURSION - Pila Invertida")
print("Pila inicial  (fondo -> tope) : " + str(pila))
print("Salida        (tope  -> fondo): ", end="")

mostrar_invertida(pila)

print()
print("Pila al finalizar             : " + str(pila))