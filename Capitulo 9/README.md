# 9. Clases
Las clases permiten agrupar datos y funciones en un solo objeto. Al crear una clase se define un nuevo tipo, del cual se pueden generar instancias con atributos y métodos para manejar su estado.

En Python, las clases tienen una sintaxis sencilla pero completa, combinando características de otros lenguajes. Soportan herencia múltiple, sobrescritura de métodos y pueden crearse y modificarse en tiempo de ejecución.

Los miembros de las clases suelen ser públicos y los métodos reciben al objeto como argumento. Además, las clases también son objetos, lo que permite mayor flexibilidad en su uso.

A diferencia de otros lenguajes, en Python se pueden extender tipos de datos integrados y redefinir operadores, lo que amplía las capacidades de las clases.

## 9.1. Unas palabras sobre nombres y objetos
Los objetos tienen identidad y pueden tener varios nombres que se refieren al mismo objeto, lo que se conoce como aliasing. Esto no suele notarse con tipos inmutables como números o cadenas.

Sin embargo, en objetos mutables como listas o diccionarios, el aliasing puede causar efectos inesperados, ya que varios nombres apuntan al mismo objeto.

Este comportamiento también es útil, porque funciona como punteros: pasar objetos es eficiente y si una función los modifica, los cambios se reflejan fuera de ella, evitando la necesidad de distintos tipos de paso de argumentos.

## 9.2. Ámbitos y espacios de nombres en Python
Antes de ver clases, es importante entender las reglas de ámbito en Python, ya que las clases usan espacios de nombres. Este conocimiento es clave para comprender mejor el lenguaje.

Un espacio de nombres es una relación entre nombres y objetos, como los nombres integrados, globales y locales. No hay conflicto entre distintos espacios de nombres, ya que se distinguen usando prefijos como el nombre del módulo.

Un atributo es cualquier elemento después de un punto (como objeto.atributo). Los atributos de módulos son equivalentes a sus nombres globales, ya que comparten el mismo espacio de nombres.

Los atributos pueden ser de solo lectura o modificables. Los modificables pueden cambiarse o eliminarse usando asignación o la instrucción del.

Los espacios de nombres se crean en distintos momentos y tienen diferente duración. Algunos duran toda la ejecución (como los integrados), mientras otros dependen del módulo o del momento en que se ejecutan.

El espacio de nombres local de una función se crea al llamarla y desaparece al terminar. Cada llamada, incluso recursiva, tiene su propio espacio local.

Un ámbito es la parte del programa donde un espacio de nombres es accesible directamente, permitiendo usar nombres sin calificarlos.

Durante la ejecución existen varios ámbitos anidados: local, no local, global y el de nombres integrados, que se buscan en ese orden.

La palabra clave global permite modificar variables del ámbito global, y nonlocal permite modificar variables de ámbitos externos. Sin ellas, las variables externas solo pueden leerse.

El ámbito local normalmente corresponde a una función, pero fuera de ella coincide con el global. Las clases también crean su propio espacio de nombres.

Los ámbitos se determinan por la estructura del código, no por cómo se llama una función. Aunque la búsqueda de nombres ocurre en ejecución, tiende a volverse más estática.

En Python, las asignaciones siempre crean o modifican variables en el ámbito local, a menos que se indique lo contrario. Estas asignaciones solo enlazan nombres a objetos, no copian datos.

Las declaraciones global y nonlocal se usan para indicar que ciertas variables pertenecen a otros ámbitos y deben modificarse allí.

## 9.2.1. Ejemplo de ámbitos y espacios de nombre
Este ejemplo muestra cómo referirse a distintos ámbitos y espacios de nombres en Python, y cómo las declaraciones global y nonlocal influyen en la asignación de variables.
```js 
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Resultado:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 9.3. Un primer vistazo a las clases
Las clases introducen un poquito de sintaxis nueva, tres nuevos tipos de objetos y algo de semántica nueva.


## 9.3.1. Sintaxis de definición de clases
La forma más sencilla de definición de una clase se ve así:
```py
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Las definiciones de clases, al igual que las funciones, deben ejecutarse para tener efecto. Incluso pueden colocarse dentro de estructuras como if o funciones.

Dentro de una clase, la mayoría de las declaraciones son funciones, aunque también se permiten otras. Estas funciones tienen una forma especial de argumentos debido a cómo funcionan los métodos.

Al definir una clase, se crea un nuevo espacio de nombres que actúa como ámbito local. Todas las asignaciones y definiciones dentro de la clase se guardan ahí.

Al finalizar la definición, se crea el objeto clase usando ese espacio de nombres. Luego, este objeto se asigna al nombre de la clase y se regresa al ámbito anterior.

## 9.3.2. Objetos clase
Los objetos clase permiten dos operaciones principales: acceder a atributos e instanciar objetos.

Para acceder a atributos se usa la sintaxis objeto.nombre. Los atributos válidos son los que estaban definidos en el espacio de nombres de la clase cuando fue creada.
```py
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
MyClass.i y MyClass.f son atributos válidos que devuelven un valor entero y una función. Los atributos pueden modificarse, y doc permite acceder a la documentación de la clase.

La instanciación se realiza como si la clase fuera una función, creando una nueva instancia sin parámetros.

*x = MyClass()*

Se crea una nueva instancia de la clase y se asigna a la variable x.

La instanciación crea un objeto vacío, pero se puede usar el método especial **init**() para inicializarlo con un estado específico.

```py
def __init__(self):
    self.data = []
```

Cuando una clase define init(), este se ejecuta automáticamente al crear una instancia, permitiendo obtener un objeto ya inicializado.
*x = MyClass()*

## 9.3.3. Objetos instancia
Los objetos instancia solo permiten acceder a atributos. Existen dos tipos: atributos de datos y métodos.

Los atributos de datos son como variables de instancia y no necesitan declararse; se crean al asignarles un valor por primera vez.

```py
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Un método es un atributo de instancia que corresponde a una función que pertenece al objeto.

Los métodos válidos dependen de la clase: si un atributo de clase es una función, se convierte en método de la instancia. Por eso, x.f es un método válido y x.i no. Además, x.f es un objeto método, distinto de MyClass.f que es una función.

## 9.3.4. Objetos método
Generalmente, un método se llama directamente con x.f(), lo que ejecuta la función y devuelve su resultado.

Sin embargo, no es necesario llamarlo de inmediato; x.f es un objeto método que puede guardarse y ejecutarse después.

```py
xf = x.f
while True:
    print(xf())
```

El método seguirá imprimiendo “hello world” cada vez que se ejecute.

Cuando se llama a un método como x.f(), parece que no se pasa el argumento requerido, pero en realidad Python lo hace automáticamente.

El objeto se pasa como primer argumento, por lo que x.f() es equivalente a MyClass.f(x). Si hay más argumentos, se agregan después del objeto.

En general, al acceder a un método, Python busca en la clase, crea un objeto método con la instancia y la función, y al llamarlo, pasa automáticamente la instancia junto con los demás argumentos.

## 9.3.5. Variables de clase y de instancia
Las variables de instancia guardan datos propios de cada objeto, mientras que las variables de clase son compartidas entre todas las instancias.
```py
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

Los datos compartidos pueden causar efectos inesperados con objetos mutables como listas o diccionarios, ya que se comparten entre instancias; por eso no se recomienda usarlos como variables de clase.
```py
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

El diseño correcto de esta clase sería usando una variable de instancia:
```py
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 9.4. Algunas observaciones
Si el mismo nombre de atributo aparece tanto en la instancia como en la clase, la búsqueda del atributo prioriza la instancia:
```py
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
storage east
```

Los atributos de datos pueden ser accedidos tanto por métodos como por usuarios, ya que Python no impone ocultamiento de datos; todo se basa en convenciones.

Los usuarios deben tener cuidado al modificar atributos, ya que pueden romper el funcionamiento interno del objeto. También pueden agregar nuevos atributos si evitan conflictos de nombres.

No existe un atajo para acceder a atributos dentro de métodos, lo que mejora la claridad al diferenciar variables locales de las de instancia.

El primer argumento de un método suele llamarse self, aunque no es obligatorio; es solo una convención para mejorar la legibilidad.

Cualquier función definida como atributo de clase se convierte en método de sus instancias, incluso si no fue definida directamente dentro de la clase.
```py
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
Las funciones f, g y h se convierten en métodos de la clase, siendo h equivalente a g, aunque este tipo de práctica puede resultar confusa.

Los métodos pueden llamar a otros métodos de la misma instancia utilizando el argumento self.
```py
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Los métodos pueden acceder a nombres globales como cualquier función. Su ámbito global es el módulo donde se definen, y aunque no es común usar datos globales, sí es útil para usar funciones, módulos o clases definidas ahí.

Todo valor en Python es un objeto y tiene una clase (tipo), la cual se puede consultar con objeto.__class__.

## 9.5. Herencia
Por supuesto, una característica del lenguaje no sería digna del nombre «clase» si no soportara herencia. La sintaxis para una definición de clase derivada se ve así:
```py
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

El nombre BaseClassName debe existir en un ámbito accesible al definir la clase derivada.

También se pueden usar expresiones en lugar de un nombre directo, lo cual es útil cuando la clase base proviene de otro módulo.
```py
class DerivedClassName(modname.BaseClassName):
```

La definición de una clase derivada funciona igual que una base, pero al crearse se toma en cuenta la clase base. Si un atributo no se encuentra en la clase, se busca en la clase base de forma recursiva.

La instanciación no cambia: DerivedClassName() crea una nueva instancia. Los métodos se buscan en la clase y, si no están, en sus clases base hasta encontrarlos.

Las clases derivadas pueden redefinir métodos, y cuando un método llama a otro, puede ejecutarse la versión redefinida en la clase derivada.

Un método redefinido puede extender al de la clase base llamándolo directamente con BaseClassName.methodname(self, arguments), siempre que la clase base sea accesible.

Python tiene dos funciones integradas que funcionan con herencia:
 - Usar isinstance() para verificar el tipo de una instancia: isinstance(obj, int) será True sólo si obj.__class__ es int o alguna clase derivada de int.
 - Usar issubclass() para verificar la herencia de clases: issubclass(bool, int) es True ya que bool es una subclase de int. Sin embargo, issubclass(float, int) es False ya que float no es una subclase de int.

## 9.5.1. Herencia múltiple
Python también soporta una forma de herencia múltiple. Una definición de clase con múltiples clases base se ve así:
```py
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
En casos simples, la búsqueda de atributos en herencia se puede entender como un recorrido en profundidad de izquierda a derecha, revisando primero la clase derivada y luego sus clases base sin repetirlas.

En realidad, el orden de búsqueda es más complejo, ya que se ajusta dinámicamente para soportar el uso de super() y permitir llamadas cooperativas entre clases.

Esto es necesario en herencia múltiple, especialmente en estructuras tipo “diamante”. Python usa un algoritmo que organiza el orden de búsqueda sin repetir clases, respetando el orden y permitiendo un diseño más consistente y extensible.

## 9.6. Variables privadas
En Python no existen variables privadas reales, pero por convención, los nombres con un guion bajo (como _spam) se consideran no públicos y sujetos a cambios.

Para evitar conflictos de nombres, existe un mecanismo donde los identificadores con doble guion bajo (como __spam) se transforman automáticamente a _nombredeclase__spam dentro de la clase.

La modificación de nombres es útil para dejar que las subclases sobreescriban los métodos sin romper las llamadas a los métodos desde la misma clase. Por ejemplo:
```py
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
El mecanismo de nombres con doble guion bajo evita conflictos entre clases, ya que cada uno se transforma según su clase (por ejemplo, _Mapping__update y _MappingSubclass__update).

Estas reglas solo buscan evitar errores, ya que es posible acceder o modificar estos atributos “privados” si es necesario.

Sin embargo, funciones como exec, eval, getattr, setattr y delattr no aplican esta modificación de nombres, ya que operan fuera del contexto normal de la clase.

## 9.7. Detalles y Cuestiones Varias
A veces es útil tener un tipo de datos similar al «registro» de Pascal o la «estructura» de C, que sirva para juntar algunos pocos ítems con nombre. El enfoque idiomático es utilizar dataclasses con este propósito:
```py
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
john.dept
'computer lab'
john.salary
1000
```
En Python, una clase puede sustituir a un tipo de dato si implementa los mismos métodos, permitiendo usar objetos diferentes mientras cumplan con la misma interfaz.

Los métodos de instancia también tienen atributos: m.self representa la instancia y m.func la función asociada al método.

## 9.8. Iteradores
Es probable que hayas notado que la mayoría de los objetos contenedores pueden ser recorridos usando una sentencia for:
```py
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Este estilo de acceso con iteradores es claro y unifica el funcionamiento de Python. Internamente, el bucle for usa iter() para obtener un iterador.

El iterador usa el método next() para devolver elementos uno a uno, y cuando se terminan, lanza la excepción StopIteration para finalizar el bucle.

```py
s = 'abc'
it = iter(s)
it
<str_iterator object at 0x10c90e650>
next(it)
'a'
next(it)
'b'
next(it)
'c'
next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

Para hacer una clase iterable, se define iter() que retorne un objeto con next(); si la clase ya tiene next(), entonces iter() puede retornar self.
```py
lass Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
```py
rev = Reverse('spam')
iter(rev)
<__main__.Reverse object at 0x00A1DB50>
for char in rev:
    print(char)

m
a
p
s
```

## 9.9. Generadores
Los generadores son una forma simple de crear iteradores usando funciones con yield, que permiten pausar y reanudar la ejecución, recordando su estado en cada llamada a next().
```py
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

f
l
o
g
```
Todo lo que hacen los generadores también se puede lograr con clases, pero los generadores son más simples porque crean automáticamente iter() y next().

Además, guardan automáticamente su estado y variables entre llamadas, lo que hace el código más claro y fácil de escribir.

Cuando terminan, lanzan StopIteration automáticamente, facilitando la creación de iteradores como si fueran funciones normales.

## 9.10. Expresiones generadoras
Los generadores también pueden escribirse como expresiones similares a las listas, usando paréntesis. Son más compactos y eficientes en memoria, aunque menos flexibles que los generadores completos.

Ejemplos:
```py
sum(i*i for i in range(10))                 # sum of squares
285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

unique_words = set(word for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```
