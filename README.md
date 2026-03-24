# Laboratorio de Recursión
**Juan David Carrillo Rojas**

Dos ejercicios prácticos que demuestran el uso de recursión en Python para resolver problemas sobre estructuras de datos y aritmética de dígitos.

---

## Archivos

| Archivo | Descripción |
|---|---|
| `ejercicio_pila_inversa.py` | Muestra una pila de enteros en orden invertido |
| `ejercicio_suma_pares.py` | Suma los dígitos pares de un número entero |
| `Laboratorio_Recursion_.pdf` | Enunciado, definición formal y explicación de los algoritmos |

---

## Ejercicio 1 — Pila Invertida (`ejercicio_pila_inversa.py`)

Función recursiva que recibe una pila de enteros y muestra sus elementos del tope al fondo. Al finalizar, la pila queda vacía.

**Entrada:** `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  
**Salida:** `9 8 7 6 5 4 3 2 1 0`

### Casos
- **Caso base:** la pila está vacía → retorna sin hacer nada
- **Caso recursivo:** extrae el tope con `pop()`, lo imprime, y se llama recursivamente con la pila reducida

### ¿Por qué funciona sin invertir nada?
Una pila es LIFO (*Last In, First Out*). El último elemento insertado es el primero en salir, por lo que vaciar la pila con `pop()` imprimiendo en cada paso produce el orden invertido de forma natural, sin necesidad de una segunda pila ni comparaciones.

---

## Ejercicio 2 — Suma de Dígitos Pares (`ejercicio_suma_pares.py`)

Función recursiva que recibe un número entero y retorna la suma de sus dígitos pares. Si ningún dígito es par, retorna `0`.

**Entrada:** `16582234` → **Salida:** `22` (6+8+2+2+4)  
**Entrada:** `13553` → **Salida:** `0`

### Casos
- **Caso base:** `n == 0` → retorna `0`, no quedan dígitos
- **Caso recursivo (par):** si el último dígito es par, lo suma y llama recursivamente con `n // 10`
- **Caso recursivo (impar):** si el último dígito es impar, lo ignora y llama recursivamente con `n // 10`

### Operaciones clave
- `n % 10` extrae el último dígito
- `n // 10` elimina el último dígito (división entera)

---

## Requisitos

- Python 3.x
- Sin librerías externas

## Ejecución

```bash
python ejercicio_pila_inversa.py
python ejercicio_suma_pares.py
```
