# Tipos de dados suportados pelo python

x = str("Hello World")
print(f"Tipo: {type(x)} --- Valor: {x}")
x = int(20)	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = float(20.5)		
print(f"Tipo: {type(x)} --- Valor: {x}")
x = complex(1j)	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = list(("apple", "banana", "cherry"))	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = tuple(("apple", "banana", "cherry"))	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = range(6)
print(f"Tipo: {type(x)} --- Valor: {x}")
x = dict(name="John", age=36)
print(f"Tipo: {type(x)} --- Valor: {x}")
x = set(("apple", "banana", "cherry"))
print(f"Tipo: {type(x)} --- Valor: {x}")
x = frozenset(("apple", "banana", "cherry"))	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = bool(5)	
print(f"Tipo: {type(x)} --- Valor: {x}")
x = bytes(5)		
print(f"Tipo: {type(x)} --- Valor: {x}")
x = bytearray(5)		
print(f"Tipo: {type(x)} --- Valor: {x}")
x = memoryview(bytes(5))
print(f"Tipo: {type(x)} --- Valor: {x}")

# em python temos 3 tipos numericos
# int, float e complex
_int = 1
_float = 1.3
_complexo = 1j

# para verificar o tipo de dado usamos a função type
print(type(_int)) # <class 'int'>

