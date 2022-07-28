# Python Avanzado 🐍

## Clousures

## Decoradores

Un decorador és una función que recibe como parámetro otra función y le añade cosas, retornando otra función diferente. Es como añadir superpoderes a una función.

```python
def decorador(func):
    def envoltura(*args, **kwargs):
        print('Esto se añade a mi función original')
        func(*args, **kwargs) # No importa la cantidad de parámetros nombrados
    return envoltura()


def saludo():
    print('¡Hola!')

# Output
# ¡Hola!

saludo = decorador(saludo)
saludo()
# Output
# Esto se añade a mi función original
# ¡Hola!

```

Los decoradores, también se pueden posicionar de la siguiente manera:

```py

def uppercase(func):
    def wrapping(text):
        return func(text).upper()
    return wrapping

@uppercase
def message(name):
    return f'{name}, are you revided a message'

print(message('Alejandro'))

```

## Iteradores

Son una estructura de datos para guardar datos infinitos. Estos son objetos que podemos recorrer un ciclo de otra manera.

Para construir el ciclo for se forma el siguiente código

```py

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

while True:
    try:
        next iter(my_iter)
    catch StopIteration:
        break

```

## Generadores

Los generadores son funciones que guarda el estado. *yield* pausa la función, actua igual que *return* excepto que continua ejecutando dicha función.

```python
def my_gen():
    print('Hello world!')
    n = 0
    yield n

    print('Hello heaven!')
    n = 1
    yield n

    print('Hello hell!')
    n = 2
    yield n

a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a)) StopIteration

```

Las ventajas de usar generadores.

Es más fácil de escribir que un Iterador y tiene todas las ventajas de este.

```python

my_list = [0, 1, 4, 7, 9, 18]

my_second_list = [x*2 for x in my_list] # List comprehesion
my_second_gen = (x*2 for x in my_list) # Generator expression

````

## Sets

Un Set es una colección desordenada de elementos únicos (no se repiten) e inmutables (no se pueden modificar).

```python
my_set = {3, 4, 5} #

my_set2 = {"Hola", 23.3, False, True} # Out -> Lo mismo, pero posiblemente desordenado para ahorrar memória

my_set3 = {3, 3, 2} # Out 2, 3

my_set4 = {[1, 2, 3], 4} # Out -> Una lista no se puede crear en un Set

```

Para crear un set vacio se haria de la siguiente manera, porqué las llaves vacias se interpreta como un diccionario.

```py
empty_set = {}
print(type(empty_set)) # <class 'dict'>

empty_set = set()
print(type(empty_set)) # <class 'set>
```

### Añadir elementos a un Set

Para añadir elementos a un set se haria de la siguietne manera:

```py
my_set = {1, 2, 3}
print(my_set) # {1, 2, 3}

# Añadir un elemento

my_set.add(4)
print(my_set) # {1, 2, 3, 4}

# Añadir varios elementos

my_set.update([1, 2, 5])
print(my_set) # {1, 2, 3, 4, 5}

my_set.update((1, 7, 2), {6, 8})
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8}
```

### Eliminar elementos a un Set

```py
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set) # {1, 2, 3, 4, 5, 6, 7}

# Borra un elemento del Set con los parametros discard y remove

my_set.discard(1)
print(my_set) # {2, 3, 4, 5, 6, 7}

my_set.remove(2)
print(my_set) # {3, 4, 5, 6, 7}

my_set.discard(10)
print(my_set) # {3, 4, 5, 6, 7}

my_set.discard(12)
print(my_set) # Si no existe, da error

# Borra un elemento aleatorio
my_set.pop()
print(my_set) # {2, 3, 4, 5, 6, 7}

# Borrar todos los elementos del Set
my_set.clear()
print(my_set) # set()
```

### Operaciones con Sets

#### Unión

Combinar todos los elementos que tienen los Sets.

```py
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 | my_set2

# or

set1.union(set2)

print(my_set3) # {3, 4, 5, 6, 7}
```

#### Intersección

Combinar ambos Sets, pero solamente quedarme con los elementos que tienen en común.

```py
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 & my_set2

# or

set1.intersection(set2)
print(my_set3) # {5}
```

#### Diferencia

Es el resultado de tomar 2 sets y quitar todos los elementos que tiene el otro.

```py
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 - my_set2
print(my_set3) # {3, 4}

# or

set1.difference(set2)

my_set4 =  my_set2 - my_set1

# or 

set2.difference(set1)
print(my_set4) # {6, 7}
```

#### Diferencia simétrica

Es el resultado de ambos sets, excepto los que se comparten

```py
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

my_set3 = my_set1 ^ my_set2

# or

set1.symmetric_difference(set2)
print(my_set3) # {3, 4, 6, 7}
```

## Manejo de fechas

```py
import datetime

my_time = datetime.datetime.now()

print(my_time) # 2022-07-27 02:46:24.087480

my_day = datetime.date.today()
print(my_day) # 2022-07-27

print(f'Year: {my_day.year}') # Year: 2022
print(f'Month: {my_day.month}') # Month: 7
print(f'Day: {my_day.day}') # Day: 27
```

### Formatear fechas
En EEUU nos encontraremos fechas en el formato mm/dd/yyyy mientras que en España y latinoamerica és dd/mm/yyyy

Código | Formateado
---|---
%Y | Year
%m | Month
%d | Day
%H | Hour
%M | Minute
%S | Second

Este se codificaria de la siguiente forma:

```py
from datetime import datetime


my_str = my_time.strftime('Formato España: %d/%m/%Y')
print(my_str) # Formato España: 27/07/2022

my_str = my_time.strftime('Formato EEUU: %m/%d/%Y')
print(my_str) # Formato EEUU: 07/27/2022



```