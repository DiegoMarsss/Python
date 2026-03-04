# 5. Estructuras de datos
Este capítulo describe en más detalle algunas cosas que ya has aprendido y agrega algunas cosas nuevas también.

### 5.1: Mas de listas

Métodos importantes de las listas en Python

append(x) → Agrega un elemento al final de la lista.

extend(iterable) → Agrega varios elementos al final.

insert(i, x) → Inserta un elemento en una posición específica.

remove(x) → Elimina la primera aparición del valor indicado.

pop([i]) → Elimina y devuelve el elemento en la posición indicada (si no se indica, elimina el último).

clear() → Borra todos los elementos de la lista.

index(x) → Devuelve la posición de la primera aparición del valor.

count(x) → Cuenta cuántas veces aparece un valor en la lista.

sort() → Ordena la lista.

reverse() → Invierte el orden de la lista.

copy() → Crea una copia de la lista.

**Un ejemplo sobre esto**
```py
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)  # Find next banana starting at position 4
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
```

En Python, métodos como insert, remove y sort solo modifican la lista y no devuelven ningún valor, ya que retornan None. Esto forma parte del diseño de las estructuras mutables: cambian el objeto directamente sin necesidad de retornarlo.

Además, no todos los datos pueden compararse u ordenarse. No se pueden mezclar tipos como números, texto o None al ordenar, y algunos, como los números complejos, no tienen un orden definido.

### 5.1.1. Usar listas como pilas
Una lista en Python puede usarse como una pila, siguiendo el principio “último en entrar, primero en salir”. Para agregar elementos a la cima se usa append(), y para retirarlos se usa pop() sin indicar índice, ya que elimina el último elemento agregado.

**Ejemplo**
```py 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]
```

### 5.1.2. Usar listas como colas
También se puede usar una lista como una cola, donde el primer elemento en entrar es el primero en salir. Sin embargo, no es eficiente, porque insertar o eliminar elementos al inicio es lento, ya que los demás deben desplazarse.

Para una cola más eficiente se recomienda usar collections.deque, que permite agregar y quitar elementos rápidamente en ambos extremos.

**Ejemplo**
```py 
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
'Eric'
queue.popleft()                 # The second to arrive now leaves
'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 5.1.3. Comprensión de listas
Las comprensiones de listas permiten crear listas de forma más corta y clara. Se usan para generar nuevas listas aplicando una operación a cada elemento de otra secuencia o para incluir solo los elementos que cumplen una condición específica. Por ejemplo, pueden utilizarse para crear una lista con los cuadrados de ciertos valores.

```py 
squares = []
for x in range(10):
    squares.append(x**2)

squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
``` 

Una comprensión de lista se escribe entre corchetes e incluye una expresión seguida de una o más cláusulas for o if. El resultado es una nueva lista creada al evaluar esa expresión según las condiciones indicadas. Por ejemplo, puede usarse para combinar elementos de dos listas siempre que cumplan cierta condición, como que no sean iguales.

```py
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
y es equivalente a:

```py
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Nótese como el orden de los for y if es el mismo en ambos pedacitos de código.

Si la expresión es una tupla (como el (x, y) en el ejemplo anterior), debe estar entre paréntesis.

```py
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 5.1.4. Listas por comprensión anidadas
La expresión inicial de una comprensión de listas puede ser cualquier expresión arbitraria, incluyendo otra comprensión de listas.

Considerá el siguiente ejemplo de una matriz de 3x4 implementada como una lista de tres listas de largo 4:

```py
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```

### 5.2. La instrucción del
La instrucción del permite eliminar un elemento de una lista usando su índice, a diferencia de pop(), que además devuelve el valor eliminado. También puede utilizarse para borrar partes de una lista o vaciarla completamente.

```py
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a
[1, 66.25, 1234.5]
del a[:]
a
[]
```

del puede usarse también para eliminar variables.

Hacer referencia al nombre a de aquí en más es un error (al menos hasta que se le asigne otro valor). Veremos otros usos para del más adelante.

### 5.3. Tuplas y secuencias
Las listas y las cadenas comparten características como el indexado y las rebanadas porque ambas pertenecen al tipo de datos secuencia. Python incluye varios tipos de secuencia, como list, range y también la tupla.

La tupla es otro tipo de secuencia estándar y se forma con varios valores separados por comas.

```py
t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
([1, 2, 3], [3, 2, 1])
```

En la salida, las tuplas aparecen entre paréntesis para que puedan interpretarse correctamente, especialmente cuando están anidadas. Pueden escribirse con o sin paréntesis, aunque a veces son necesarios dentro de expresiones más grandes. No se pueden modificar sus elementos individuales, aunque sí pueden contener objetos mutables, como listas.

Aunque se parecen a las listas, las tuplas se usan de forma distinta. Son inmutables y suelen almacenar datos heterogéneos que se acceden por desempaquetado o índice. En cambio, las listas son mutables y generalmente contienen elementos del mismo tipo que se recorren con iteraciones.

Para crear tuplas vacías se usan paréntesis (). Si tienen un solo elemento, es necesario agregar una coma después del valor, ya que solo poner paréntesis no es suficiente.

```py
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
0
len(singleton)
1
singleton
('hello',)
```

### 5.4. Conjuntos
Python incluye el tipo de dato set, que representa una colección desordenada y sin elementos repetidos. Se utiliza principalmente para verificar pertenencia y eliminar duplicados, además de permitir operaciones matemáticas como unión, intersección y diferencia.

Los conjuntos pueden crearse usando llaves {} o la función set(). Sin embargo, para crear un conjunto vacío es necesario usar set(), ya que {} crea un diccionario vacío.

```py
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
True
'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

### 5.5. Diccionarios
El diccionario (dict) es un tipo de dato que almacena información en pares clave:valor. A diferencia de las listas u otras secuencias, no se indexa con números, sino con claves, que deben ser tipos inmutables como cadenas, números o tuplas (siempre que no contengan objetos mutables). Las listas no pueden usarse como claves porque pueden modificarse.

Los diccionarios se crean con llaves {} y cada clave debe ser única. Permiten guardar, obtener y eliminar valores mediante su clave. Si se usa una clave que ya existe, el valor anterior se reemplaza. Intentar acceder a una clave inexistente genera un error (KeyError), pero puede evitarse usando el método get(), que devuelve None o un valor por defecto. También es posible obtener la lista de claves con list(d) y verificar si una clave existe usando la palabra clave in.

Un pequeño ejemplo de uso de un diccionario:

```py
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
4098
tel['irv']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'irv'
print(tel.get('irv'))
None
del tel['sape']
tel['irv'] = 4127
tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False
```

El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:
```py
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

Además, las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias de clave y valor:
```py
{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

Cuando las claves son cadenas simples, a veces resulta más fácil especificar los pares usando argumentos por palabra clave:
```py
dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 5.6. Técnicas de iteración
Cuando iteramos sobre diccionarios, se pueden obtener al mismo tiempo la clave y su valor correspondiente usando el método items().

```py
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

gallahad the pure
robin the brave
```

Cuando se itera sobre una secuencia, se puede obtener el índice de posición junto a su valor correspondiente usando la función enumerate().

```py
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

0 tic
1 tac
2 toe
```

### 5.7. Más acerca de condiciones
Las condiciones en while e if pueden usar cualquier operador, no solo comparaciones. Los operadores in y not in verifican pertenencia en una secuencia, mientras que is e is not comprueban si dos variables hacen referencia al mismo objeto. Todas las comparaciones tienen menor prioridad que los operadores numéricos y pueden encadenarse, como en a < b == c.

Las comparaciones también pueden combinarse con and, or y negarse con not. Estos operadores tienen menor prioridad que las comparaciones; not se evalúa antes que and, y and antes que or. Además, and y or son operadores de cortocircuito: evalúan de izquierda a derecha y se detienen cuando el resultado ya está determinado, devolviendo el último valor evaluado.

Es posible asignar el resultado de una comparación u otra expresión booleana a una variable. Por ejemplo,
```py
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
'Trondheim'
```
Nótese que en Python, a diferencia de C, asignaciones dentro de expresiones deben realizarse explícitamente con el operador walrus :=. Esto soluciona algunos problemas comunes encontrados en C: escribiendo = en una expresión cuando se intentaba escribir ==.

### 5.8. Comparando secuencias y otros tipos
Las secuencias pueden compararse con otras del mismo tipo utilizando un orden lexicográfico. Esto significa que se comparan elemento por elemento, empezando por el primero; si son diferentes, ahí se determina el resultado. Si son iguales, se continúa con los siguientes hasta encontrar una diferencia o llegar al final.

Si los elementos comparados también son secuencias del mismo tipo, la comparación se hace de forma recursiva. Si todos los elementos son iguales, las secuencias se consideran iguales. Cuando una es prefijo de la otra, la más corta es menor. En el caso de las cadenas, el orden se basa en los códigos Unicode de cada carácter.

```py
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
Es posible comparar objetos de distintos tipos con < o > siempre que tengan métodos de comparación compatibles. Por ejemplo, los números de diferentes tipos se comparan según su valor numérico, por lo que 0 es igual a 0.0. Sin embargo, si los objetos no pueden compararse correctamente, Python no impone un orden arbitrario y lanza una excepción TypeError.
