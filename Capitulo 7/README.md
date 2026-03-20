# 7- Entrada y salida
Hay diferentes métodos de presentar la salida de un programa; los datos pueden ser impresos de una forma legible por humanos, o escritos a un archivo para uso futuro. Este capítulo discutirá algunas de las posibilidades.

### 7.1. Formateo elegante de la salida
Hay varias formas de mostrar valores en Python: usando expresiones, con print() y también con write(), aunque esta última casi no se usa.

Cuando quieres que la salida se vea mejor o más ordenada, puedes darle formato. Una forma muy común es usar las cadenas con f (f-strings). Estas permiten incluir variables o resultados dentro de {}, haciendo que el texto sea más claro, dinámico y fácil de leer.

```py 
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```
El método str.format() requiere un poco más de trabajo manual. También usa {} para indicar dónde van las variables y permite darles formato, pero aquí tienes que pasar los valores explícitamente.

En pocas palabras, es otra forma de insertar datos en un texto, aunque es menos directa que usar f-strings.

```py 
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```
Aquí se muestra que los números pueden formatearse, por ejemplo agregando espacios o mostrando el signo solo si son negativos. También se puede mostrar un porcentaje multiplicando por 100, con cierto número de decimales y el símbolo %.

Además, puedes controlar totalmente el formato usando concatenación o métodos de cadenas, que ayudan a ajustar el texto al tamaño o forma que quieras.


Cuando no necesitas que la salida se vea bonita, sino solo revisar rápido valores (como al depurar), puedes convertirlos a texto con str() o repr().

str() muestra los datos de forma más clara y fácil de entender para las personas. En cambio, repr() muestra una versión más técnica, pensada para que Python la entienda o incluso pueda volver a interpretarla.

En muchos casos, como con números, listas o diccionarios, ambos muestran casi lo mismo. Pero en las cadenas sí pueden verse diferentes, porque repr() muestra más detalles como comillas o caracteres especiales.


Algunos Ejemplos:

```py
s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

El módulo string incluye otra forma sencilla de trabajar con texto usando plantillas (string.Template). Funciona con marcadores como $x, que luego se reemplazan con valores de un diccionario.

Es una forma fácil y clara de insertar datos en cadenas, pero tiene menos opciones para dar formato en comparación con otros métodos.

### 7.1.1. Formatear cadenas literales
Las f-strings (cadenas con f) permiten meter valores o expresiones directamente dentro de un texto usando {}. Solo tienes que poner una f antes de la cadena.

Además, puedes agregar un formato especial para controlar cómo se ve el resultado, por ejemplo limitar decimales. Esto hace que sea una forma muy práctica y clara de mostrar datos, como redondear números a cierta cantidad de cifras.

```py
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
Pasar un entero después de ':' hará que ese campo sea un número mínimo de caracteres de ancho. Esto es útil para hacer que las columnas se alineen.

```py
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
Se pueden utilizar otros modificadores para convertir el valor antes de formatearlo. '!a' se aplica ascii(), '!s' se aplica str(), y '!r' se aplica repr():

```py
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
El especificador = puede utilizarse para expandir una expresión al texto de la expresión, un signo igual y, a continuación, la representación de la expresión evaluada:

```py
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```
Para más detalles sobre cómo funcionan los formatos, se pueden usar opciones como el especificador =, que ayuda a mostrar tanto la expresión como su valor.

Si quieres aprender todas las formas de dar formato, puedes revisar la guía del “Mini-Lenguaje de formato”, donde vienen todas las opciones disponibles.

### 7.1.2. El método format() de cadenas
El uso básico del método str.format() es como esto:

```py
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

En str.format(), las llaves {} (llamadas campos de formato) se reemplazan con los valores que le pasas al método.

Si pones números dentro de las llaves, estos indican la posición de cada valor. Es decir, puedes controlar qué dato va en cada lugar según el orden en que los envías.

```py
print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
Si se usan argumentos nombrados en el método str.format(), sus valores se referencian usando el nombre del argumento.

```py
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
Se pueden combinar arbitrariamente argumentos posicionales y nombrados:

```py
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
The story of Bill, Manfred, and Georg.
```
Si tienes una cadena muy larga y no quieres confundirte con posiciones, puedes usar nombres en lugar de números en str.format().

Esto se hace pasando un diccionario y usando corchetes [] para llamar a las claves. Así el código es más claro y fácil de entender, porque sabes exactamente qué valor estás usando.

```py
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Esto se podría hacer, también, pasando el diccionario table como argumentos por palabra clave con la notación “**”.

```py
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Esto es muy útil cuando lo combinas con la función vars(), que devuelve un diccionario con todas las variables locales.

Así puedes usar esas variables directamente en el formato de cadenas sin tener que escribirlas una por una, haciendo el código más rápido y sencillo.
```py
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...
```

Como ejemplo, las siguientes líneas producen un conjunto ordenado de columnas que dan enteros y sus cuadrados y cubos:

```py
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

Para entender completamente cómo funciona el formateo con str.format(), puedes consultar la guía de formato personalizado.

Ahí se explican todas las opciones disponibles para modificar y controlar cómo se muestran los datos en las cadenas.

### 7.1.3. Formateo manual de cadenas
Aquí está la misma tabla de cuadrados y cubos, formateados manualmente:
```py
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
print() agrega espacios automáticamente entre los valores, por eso al mostrar columnas aparece separación entre ellas.

Para acomodar texto, existen métodos como str.rjust(), que alinea a la derecha agregando espacios a la izquierda. También están str.ljust() (izquierda) y str.center() (centrado). Estos no imprimen nada, solo devuelven una nueva cadena ya acomodada.

Si el texto es más largo que el espacio definido, no se corta, sino que se muestra completo, aunque desordene la columna. Si quieres recortarlo, puedes usar algo como [:n].

Existe otro método llamado str.zfill(), que sirve para rellenar una cadena numérica con ceros a la izquierda.

Es útil para dar formato a números, y además reconoce signos positivos y negativos, manteniéndolos mientras agrega los ceros necesarios.
```py
'12'.zfill(5)
'00012'
'-3.14'.zfill(7)
'-003.14'
'3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4. Viejo formateo de cadenas
El operador % también se puede usar para dar formato a cadenas. Funciona reemplazando partes del texto con valores usando un formato específico.

A esto se le llama interpolación de cadenas, y permite insertar datos dentro de un texto, aunque es una forma más antigua comparada con otras como f-strings o str.format().
```py
import math
print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

Podés encontrar más información en la sección Formateo de cadenas al estilo *printf*.

### 7.2. Leyendo y escribiendo archivos
La función open() se usa para abrir archivos y devuelve un objeto tipo archivo.

Normalmente recibe el nombre del archivo, el modo en que se abrirá (por ejemplo lectura o escritura) y opcionalmente el encoding, que indica cómo se manejarán los caracteres.

```py
f = open('workfile', 'w', encoding="utf-8")
```

El primer argumento de open() es el nombre del archivo y el segundo indica cómo se va a usar, como leer ('r'), escribir ('w'), agregar ('a') o ambos ('r+'). Si no se especifica, se usa 'r' por defecto.

Normalmente los archivos se abren en modo texto, usando una codificación. Se recomienda usar encoding="utf-8". Si se agrega 'b', se abre en modo binario y se manejan bytes en lugar de texto.

En modo texto, los saltos de línea se ajustan automáticamente según el sistema. Esto es útil para texto, pero puede dañar archivos binarios, por lo que en esos casos se debe usar modo binario.

Es buena práctica usar with al trabajar con archivos, ya que los cierra automáticamente al terminar, incluso si ocurre un error, y hace el código más limpio.

```py
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed
True
```
Si no usas with, debes cerrar el archivo manualmente con f.close(). Esto sirve para liberar los recursos del sistema y evitar problemas al trabajar con archivos.

```
Advertencia Llamar a f.write() sin usar la palabra clave with o sin llamar a f.close() podría dar como resultado que los argumentos de f.write() no se escriban completamente en disco, incluso si el programa se termina correctamente.
```

Después de que un objeto de archivo es cerrado, ya sea por with o llamando a f.close(), intentar volver a utilizarlo fallará automáticamente:
```py
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1. Métodos de los objetos Archivo
En los ejemplos se asume que ya existe un archivo abierto llamado f.

Para leer su contenido se usa f.read(size), que devuelve texto (o bytes si es binario). El parámetro size es opcional: si no se pone o es negativo, se lee todo el archivo completo, lo cual puede ser un problema si es muy grande.

Si se especifica size, solo se lee esa cantidad de caracteres o bytes como máximo. Cuando se llega al final del archivo, la función devuelve una cadena vacía ('').

```py
f.read()
'This is the entire file.\n'
f.read()
''
```

f.readline() lee una sola línea del archivo y normalmente incluye el salto de línea (\n) al final. Solo no lo incluye en la última línea si el archivo no termina con ese salto.

Esto ayuda a distinguir casos: si devuelve una cadena vacía (''), significa que ya se llegó al final del archivo. En cambio, una línea en blanco se representa como '\n'.

```py
f.readline()
'This is the first line of the file.\n'
f.readline()
'Second line of the file\n'
f.readline()
''
```

Para leer líneas de un archivo, puedes iterar sobre el objeto archivo. Esto es eficiente en memoria, rápido, y conduce a un código más simple:

```py
for line in f:
    print(line, end='')

This is the first line of the file.
Second line of the file
```

f.write(cadena) escribe el contenido de la cadena al archivo, retornando la cantidad de caracteres escritos.
```py
f.write('This is a test\n')
15
```
Otros tipos de objetos necesitan ser convertidos – tanto a una cadena (en modo texto) o a un objeto de bytes (en modo binario) – antes de escribirlos:

```py
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
18
```

f.tell() devuelve un número que indica en qué posición vas dentro del archivo. En modo binario es el número de bytes desde el inicio, y en modo texto es una referencia interna.

Para moverte dentro del archivo se usa f.seek(offset, whence). El offset es cuánto te mueves y whence indica desde dónde:
desde el inicio (0), desde la posición actual (1) o desde el final (2). Si no se indica, se usa el inicio por defecto.

```py
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
16
f.seek(5)      # Go to the 6th byte in the file
5
f.read(1)
b'5'
f.seek(-3, 2)  # Go to the 3rd byte before the end
13
f.read(1)
b'd'
```

En archivos de texto, seek() tiene limitaciones: solo se puede mover desde el inicio (o directamente al final con seek(0, 2)), y los valores válidos son los que devuelve f.tell() o cero. Usar otros valores puede causar errores o comportamientos raros.

Además, los archivos tienen otros métodos como isatty() y truncate(), pero se usan menos. Para conocer todos, se puede consultar la documentación completa.

### 7.2.2. Guardar datos estructurados con json
Las cadenas se pueden leer y escribir fácilmente en archivos, pero los números requieren convertirlos, ya que read() devuelve texto y hay que usar funciones como int() para obtener el valor numérico.

Cuando trabajas con datos más complejos como listas o diccionarios, se vuelve más difícil guardarlos directamente. Para eso se usa JSON, un formato muy común para guardar e intercambiar datos.

El módulo json permite convertir datos de Python a texto (serialización) y luego volver a convertir ese texto a datos originales (deserialización). Esto sirve para guardar información en archivos o enviarla a otros sistemas.

Si tienes un objeto x, puedes ver su representación JSON con una simple línea de código:

```py
import json
x = [1, 'simple', 'list']
json.dumps(x)
'[1, "simple", "list"]'
```
Otra variante de la función dumps(), llamada dump(), simplemente serializa el objeto a un archivo de texto. Así que, si f es un objeto archivo de texto abierto para escritura, podemos hacer:

```py
json.dump(x, f)
```
Para decodificar un objeto nuevamente, si f es un objeto binary file o text file que fue abierto para lectura:

```py
x = json.load(f)
```

La simple técnica de serialización puede manejar listas y diccionarios, pero serializar instancias de clases arbitrarias en JSON requiere un poco de esfuerzo extra. La referencia del módulo json contiene una explicación de esto.