# Tipos de datos y variables en Python

# 1. Números
# Enteros (int)
numero_entero = 42
numero_negativo = -17

# Flotantes (float)
numero_decimal = 3.14
numero_cientifico = 2.5e-3

# Complejos (complex)
numero_complejo = 3 + 4j

# 2. Texto
# Cadenas de texto (str)
texto = "Hola Mundo"
texto_comilla_simple = 'Python'
texto_multilinea = """Este es un texto
que ocupa varias
líneas"""

# 3. Booleanos (bool)
verdadero = True
falso = False

# 4. Secuencias
# Listas (list) - mutables
lista = [1, 2, 3, "python", True]
lista_vacia = []

# Tuplas (tuple) - inmutables
tupla = (1, "hola", 3.14)
tupla_un_elemento = (1,)

# 5. Conjuntos (set)
conjunto = {1, 2, 3, 4, 5}
conjunto_vacio = set()

# 6. Diccionarios (dict)
diccionario = {
    "nombre": "Python",
    "año": 1991,
    "creador": "Guido van Rossum"
}

# 7. None - Tipo especial que representa la ausencia de valor
valor_nulo = None

# Ejemplos de uso
print("=== Ejemplos de uso de variables ===")
print(f"Número entero: {numero_entero}")
print(f"Número decimal: {numero_decimal}")
print(f"Texto: {texto}")
print(f"Lista: {lista}")
print(f"Elemento de la lista: {lista[0]}")
print(f"Diccionario: {diccionario['nombre']}")
print(f"Conjunto: {conjunto}")

# Verificación de tipos
print("\n=== Tipos de variables ===")
print(f"Tipo de numero_entero: {type(numero_entero)}")
print(f"Tipo de numero_decimal: {type(numero_decimal)}")
print(f"Tipo de texto: {type(texto)}")
print(f"Tipo de lista: {type(lista)}")
print(f"Tipo de tupla: {type(tupla)}")
print(f"Tipo de conjunto: {type(conjunto)}")
print(f"Tipo de diccionario: {type(diccionario)}")

