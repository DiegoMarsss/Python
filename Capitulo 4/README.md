# Más herramientas para control de flujo

### 4.1. La sentencia if

```Py
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```
esto es uno de los if de sentencia mas comun. Puede haber cero o más bloques elif, y el bloque else es opcional. La palabra reservada elif es una abreviación de “else if”, y es útil para evitar un sangrado excesivo. Una secuencia if … elif … elif … sustituye las sentencias switch o case encontradas en otros lenguajes.

### 4.2. La sentencia for
La sentencia for en Python funciona diferente a la de lenguajes como C o Pascal. En lugar de iterar solo sobre números con un paso definido, como en esos lenguajes, en Python el for recorre directamente los elementos de una secuencia (como listas o cadenas de texto) en el orden en que aparecen.

```Py
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

### 4.3. La función range()
Si se necesita iterar sobre una secuencia de números, es apropiado utilizar la función integrada range(), la cual genera progresiones aritméticas:

```py
for i in range(5):
    print(i)
```
El valor final en range() no se incluye en la secuencia. Por ejemplo, range(10) genera 10 valores, del 0 al 9, que corresponden a los índices de una secuencia de longitud 10. También se puede indicar un número inicial distinto y un incremento diferente, incluso negativo, llamado “paso”.

```py
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

### 4.4. Las sentencias break y continue
La sentencia break termina el bucle for o while envolvente más interno:

```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```

La sentencia continue, también tomada de C, continúa con la siguiente iteración del bucle:

```py
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

### 4.5. Cláusulas else en bucles
En los bucles for y while, la cláusula else puede usarse junto con break.

La cláusula else se ejecuta solo si el bucle termina de forma normal, es decir, sin que se ejecute un break.

En un for, el else se ejecuta después de completar todas las iteraciones.
En un while, se ejecuta cuando la condición se vuelve falsa.

Si el bucle termina por un break, return o una excepción, el else no se ejecuta. Esto suele usarse, por ejemplo, en un for que busca números primos.

```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
Sí, el código es correcto: la cláusula else pertenece al bucle for, no al if.

Una forma de entenderlo es imaginar que el else está relacionado con el if dentro del bucle. Durante la ejecución, el ciclo realiza varias comprobaciones if. Si en algún momento la condición es verdadera, se ejecuta un break y el bucle termina. Pero si la condición nunca es verdadera, entonces se ejecuta el else que está fuera del bucle.

Cuando se usa en un bucle, la cláusula else se parece más al else de una sentencia try que al de un if. En una sentencia try, el else se ejecuta si no ocurre ninguna excepción. De manera similar, en un bucle, el else se ejecuta si no ocurre ningún break.

### 4.7. La sentencia match
La sentencia match evalúa una expresión y compara su valor con distintos patrones definidos en bloques case.

Aunque se parece a la sentencia switch de C, Java o JavaScript, en realidad es más similar al pattern matching de lenguajes como Rust o Haskell.

Solo se ejecuta el primer patrón que coincida y, además, puede extraer partes del valor (como elementos de una secuencia o atributos de un objeto) y asignarlos a variables.

Si ningún case coincide, no se ejecuta ningún bloque.

La forma más sencilla consiste en comparar un valor con uno o varios valores literales.

```py
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
Se pueden combinar varios literales en un solo patrón usando | («o»):

case 401 | 403 | 404:
    return "Not allowed"




Si estás usando clases para estructurar tus datos, puedes usar el nombre de la clase seguida de una lista de argumentos similar a la de un constructor, pero con la capacidad de capturar atributos en variables:
```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

### 4.8. Definir funciones
Podemos crear una función que escriba la serie de Fibonacci hasta un límite determinado:

```py
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```
La palabra clave def se utiliza para definir funciones en Python. Después de def se escribe el nombre de la función y sus parámetros entre paréntesis, y el cuerpo de la función debe ir en la siguiente línea con sangría.

Opcionalmente, la primera línea del cuerpo puede ser una cadena de texto llamada docstring, que sirve para documentar la función. Es buena práctica incluirla, ya que puede usarse para generar documentación o facilitar la consulta del código.

Cuando se ejecuta una función, se crea una nueva tabla de símbolos para sus variables locales. Las asignaciones se guardan en esa tabla local, y al buscar una variable Python revisa primero el ámbito local, luego los ámbitos externos, después el global y finalmente los nombres predefinidos. No se pueden modificar variables globales o externas directamente dentro de una función, salvo usando global o nonlocal, aunque sí pueden consultarse.

Los argumentos de una función se pasan por valor (aunque ese valor es una referencia al objeto). Cada llamada a función crea su propia tabla de símbolos local, incluso en llamadas recursivas.

Finalmente, definir una función asocia su nombre con un objeto función en la tabla de símbolos actual. Ese objeto puede tener varios nombres que apunten a él y todos pueden usarse para llamar a la función.

```py
fib
<function fib at 10042ed0>
f = fib
f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

### 4.9.1. Argumentos con valores por omisión
La forma más útil es especificar un valor por omisión para uno o más argumentos. Esto crea una función que puede ser llamada con menos argumentos que los que permite. Por ejemplo:

```py
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
La función puede llamarse de tres maneras:

Pasando solo el argumento obligatorio.

Pasando el obligatorio y uno opcional.

Pasando todos los argumentos, incluidos los opcionales.

El ejemplo también muestra el uso de la palabra clave in, que sirve para comprobar si un valor está contenido dentro de una secuencia.

Además, los valores por defecto de los parámetros se evalúan una sola vez, en el momento en que se define la función y dentro de ese ámbito. Esto significa que no se vuelven a calcular cada vez que se llama a la función.


```py
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
Advertencia importante:
Los valores por defecto se evalúan solo una vez, en el momento en que se define la función.

Esto puede causar problemas si el valor por defecto es un objeto mutable (como una lista o un diccionario). Por ejemplo:
```py
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```

El resultado será:

[1]
[1, 2]
[1, 2, 3]


Esto ocurre porque la lista L se crea una sola vez y se reutiliza en cada llamada, acumulando los valores.

```py
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

Aquí se usa None como valor por defecto y se crea una nueva lista en cada llamada, evitando que se comparta entre ejecuciones.

### 4.9.2. Palabras claves como argumentos
Las funciones también puede ser llamadas usando argumentos de palabras clave (o argumentos nombrados) de la forma kwarg=value. Por ejemplo, la siguiente función:
```py
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
…acepta un argumento obligatorio (voltage)) y tres argumentos opcionales (state, action, y type). Esta función puede llamarse de cualquiera de las siguientes maneras:
```py
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
…pero estas otras llamadas serían todas inválidas:
```
En una llamada a función en Python:
Los argumentos nombrados (keyword arguments) deben ir después de los argumentos posicionales.
Cada argumento nombrado debe coincidir con un parámetro definido en la función.
El orden de los argumentos nombrados no importa.
Incluso los parámetros obligatorios pueden pasarse como nombrados (por ejemplo, parrot(voltage=1000) es válido).
Ningún parámetro puede recibir más de un valor al mismo tiempo.
Por ejemplo, esto produce un error:
```py
def function(a):
    pass

function(0, a=0)
```
Aquí falla porque el parámetro a recibe dos valores:
0 como argumento posicional
0 como argumento nombrado
Esto genera un TypeError indicando que el argumento recibió múltiples valores.

Cuando un parámetro formal de la forma nombre está presente al final, recibe un diccionario (ver Tipos mapa — dict) conteniendo todos los argumentos nombrados excepto aquellos correspondientes a un parámetro formal. Esto puede ser combinado con un parámetro formal de la forma nombre (descrito en la siguiente sección) que recibe una tupla conteniendo los argumentos posicionales además de la lista de parámetros formales. (*nombre debe ocurrir antes de **nombre). Por ejemplo, si definimos una función así:
```py
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```
Puede ser llamada así:
```py
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
…y por supuesto imprimirá:

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
Se debe notar que el orden en el cual los argumentos nombrados son impresos está garantizado para coincidir con el orden en el cual fueron provistos en la llamada a la función.


### 4.9.3 Parámetros especiales 

En Python, los argumentos pueden pasarse por posición o por palabra clave. Sin embargo, es posible restringir cómo deben enviarse usando los símbolos / y * en la definición de la función.

Ejemplo:
```py
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```

Aquí los símbolos / y * indican el tipo de parámetros:
Antes de / → solo posicionales (positional-only)
Deben pasarse únicamente por posición, no por nombre.
Entre / y * → posicional o por palabra clave (positional-or-keyword)
Pueden pasarse de cualquiera de las dos formas.
Después de * → solo por palabra clave (keyword-only)
Deben pasarse obligatoriamente usando nombre=valor.

### 4.9.3.1 Argumentos posicionales o por palabra clave
Si en la definición no aparecen / ni *, todos los parámetros pueden enviarse tanto por posición como por palabra clave.

### 4.9.3.2 Parámetros únicamente posicionales
Se colocan antes de /.
No pueden pasarse usando su nombre.
Si no hay /, no existen parámetros solo posicionales.

### 4.9.3.3 Parámetros únicamente de palabra clave
Se colocan después de *.
Deben enviarse obligatoriamente como nombre=valor.
En resumen, / separa los parámetros que solo pueden pasarse por posición, y * separa los que solo pueden pasarse por palabra clave. Esto mejora la claridad, legibilidad y control sobre cómo se usa una función.

### 4.9.3.4. Ejemplos de Funciones
Considere el siguiente ejemplo de definiciones de funciones prestando especial atención a los marcadores / y *:
```py 
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```
La primer definición de función, standard_arg, la forma mas familiar, no indica ninguna restricción en las condiciones para llamarla y los parámetros deben ser pasados por posición o utilizando palabras clave


La segunda función pos_only_arg está restringida a utilizar únicamente parámetros posicionales ya que existe una / en la definición de la función:

La tercera función kwd_only_argsolo permite argumentos de palabras clave como los que se indican con a *en la definición de la función:

La última utiliza las tres convenciones en una misma definición de función:

### 4.9.3.5. Resumen 
Resumen

La elección entre parámetros solo posicionales, posicional o palabra clave, y solo por palabra clave depende del caso de uso.

Dada la función:
```py
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```
Guía práctica

🔹 Use parámetros solo posicionales (/) cuando:

El nombre del parámetro no es importante para el usuario.

Quiere obligar a que se respete el orden al llamar la función.

Necesita combinar parámetros posicionales fijos con palabras clave arbitrarias.

Está diseñando una API y quiere poder cambiar el nombre del parámetro en el futuro sin romper el código existente.

🔹 Use parámetros solo por palabra clave (*) cuando:

El nombre del parámetro tiene significado importante.

La llamada será más clara usando nombres explícitos.

Quiere evitar que los usuarios dependan del orden de los argumentos.

En resumen:

Solo posicional → control y estabilidad (especialmente en APIs).

Solo palabra clave → claridad y legibilidad.

Ambos → flexibilidad.


### 4.9.4 Listas de argumentos arbitrarios 
Una función en Python puede aceptar un número variable de argumentos usando *args.
Estos argumentos adicionales se agrupan automáticamente en una tupla.

Ejemplo:
```py
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

Aquí:
file y separator son parámetros normales.
*args recoge todos los argumentos extra que se pasen a la función.
 Generalmente, *args se coloca al final porque captura todos los argumentos restantes.
Parámetros después de *args
Cualquier parámetro que aparezca después de *args será solo por palabra clave (keyword-only), es decir, deberá pasarse obligatoriamente usando nombre=valor.

Ejemplo:
```py
def concat(*args, sep="/"):
    return sep.join(args)
```
Uso:
```py
concat("earth", "mars", "venus")
# 'earth/mars/venus'

concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'
```
En este caso:
"earth", "mars" y "venus" se guardan en args.
sep solo puede modificarse usando argumento nombrado

En resumen:
*args permite recibir muchos argumentos posicionales.
Los parámetros después de *args son obligatoriamente por palabra clave.
Esto brinda flexibilidad sin perder claridad en la función.

### 4.9.5 Desempaquetando una lista de argumentos — Resumen

A veces los argumentos ya están guardados en una lista o tupla, pero la función necesita recibirlos como argumentos separados. En ese caso se usa el operador * para desempaquetarlos.

Ejemplo con range():
```py
list(range(3, 6))      # llamada normal
# [3, 4, 5]

args = [3, 6]
list(range(*args))     # desempaquetando la lista
# [3, 4, 5]
```

Aquí, *args toma los elementos de la lista y los pasa como argumentos posicionales individuales.
Desempaquetar diccionarios con **

El operador ** se usa para desempaquetar un diccionario y pasar sus pares clave-valor como argumentos nombrados.

Ejemplo:
```py
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {
    "voltage": "four million",
    "state": "bleedin' demised",
    "action": "VOOM"
}
parrot(**d)
```
Aquí, **d convierte las claves del diccionario en argumentos nombrados para la función.

En resumen
* → desempaqueta listas o tuplas en argumentos posicionales.

** → desempaqueta diccionarios en argumentos nombrados.

Es el proceso inverso a *args y **kwargs en la definición de funciones.

### 4.9.6. Expresiones lambda
Pequeñas funciones anónimas pueden ser creadas con la palabra reservada lambda. Esta función retorna la suma de sus dos argumentos: lambda a, b: a+b Las funciones Lambda pueden ser usadas en cualquier lugar donde sea requerido un objeto de tipo función. Están sintácticamente restringidas a una sola expresión. Semánticamente, son solo azúcar sintáctica para definiciones normales de funciones. Al igual que las funciones anidadas, las funciones lambda pueden hacer referencia a variables desde el ámbito que la contiene:
```py
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
42
f(1)
43
```
El ejemplo anterior utiliza una expresión lambda para devolver una función. Otro uso es pasar una función pequeña como argumento. Por ejemplo, list.sort() se utiliza una función de clave de ordenación , que puede ser una función lambda:
```py
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### 4.9.7 Cadenas de texto de documentación (Docstrings) — Resumen

Las docstrings son cadenas de texto que documentan módulos, clases o funciones. Existen ciertas convenciones para su contenido y formato:

🔹 Primera línea

Debe ser un resumen breve y claro del propósito del objeto.

No debe repetir el nombre del objeto (ya que ya es conocido).

Debe comenzar con mayúscula y terminar con punto.

🔹 Segunda línea

Debe estar en blanco.

Sirve para separar el resumen de la descripción más detallada.

🔹 Líneas siguientes

Contienen una explicación más extensa.

Pueden describir cómo se usa el objeto, sus parámetros, efectos secundarios, etc.

Pueden organizarse en uno o varios párrafos.

Además, Python elimina automáticamente la sangría común en docstrings multilínea cuando pertenecen a módulos, clases o funciones.

Ejemplo de docstring multilínea:
```py 
def my_function(param1, param2):
    """
    Perform an example operation.

    This function demonstrates how to write a multi-line
    docstring following Python conventions. It explains
    the purpose, parameters, and behavior of the function.
    """
    pass
```
En resumen, una buena docstring debe ser clara, estructurada y seguir estas convenciones para facilitar la lectura y generación automática de documentación.

### 4.9.8. Anotación de funciones
Las anotaciones de funciones son información completamente opcional sobre los tipos usadas en funciones definidas por el usuario (ver PEP 3107 y PEP 484 para más información).

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement. The following example has a required argument, an optional argument, and the return value annotated:

```py
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```