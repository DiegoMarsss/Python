#  Una introducción informal a Python
En este capitulo veremos los siguientes ejemplos, la entrada y la salida se distinguen por la presencia o ausencia de prompts (>>> y …): para repetir el ejemplo, escribe todo después del prompt, cuando aparece; las líneas que no comienzan con un prompt son emitidas desde el intérprete.

Muchos de los ejemplos de este manual, incluso aquellos ingresados en el prompt interactivo, incluyen comentarios. Los comentarios en Python comienzan con el carácter numeral, #, y se extienden hasta el final visible de la línea. Un comentario quizás aparezca al comienzo de la línea o seguido de espacios en blanco o código, pero no dentro de una cadena de caracteres. Un carácter numeral dentro de una cadena de caracteres es sólo un carácter numeral. Ya que los comentarios son para aclarar código y no son interpretados por Python, pueden omitirse cuando se escriben los ejemplos.

- Un ejemplo
```Python
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## 3.1. Usando Python como una calculadora
Usaremos los interpretes, el interprete funciona como una calculadora, debemos usar expreciones y este escribira los valores. La sintaxis es sencilla: los operadores +, -, * y / se pueden usar para realizar operaciones aritméticas; los paréntesis (()) pueden ser usados para agrupar.

- Aqui tenemos un ejemplo
```Python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6
```
Los números enteros (ej. 2, 4, 20) tienen tipo int, los que tienen una parte fraccionaria (por ejemplo 5.0, 1.6) tiene el tipo float. Vamos a ver más acerca de los tipos numéricos más adelante en el tutorial.

Una división matemática que se redondea hacia el entero menor más cercano. El operador de la división entera a la baja es //. Por ejemplo, la expresión 11 // 4 evalúa 2 a diferencia del 2.75 retornado por la verdadera división de números flotantes. Note que (-11) // 4 es -3 porque es -2.75 redondeado para abajo, eso vendria siendo un floor division.

Cuando se usa un sola **/** los dejara asi en decimal y no los pasara a enteros.

- Un ejemplo 
```Python
>>> 17 / 3  #con una diagonal
5.666666666666667
>>> 17 // 3  # con doble diagonal
5
>>> 17 % 3  # el operador % devuelve el resto de la división
2
>>> 5 * 3 + 2  # cociente descompuesto * divisor + resto
17
```
diras que es % ese sirve para ver si un numero es par o impar, para sacar esto es algo asi.

- divides 17 / 3 y te da decimal > 5.666666666666667
- como es decimal ocuparemos 17 // 3 y te dara el numero entero > 5

- despues multiplicamos 5 * 3 que es igual a > 15
- luego de eso restaremos 17 entre 15 que nos dara > 2, el dos significa que el numero es par
- de ahi sale el 2 y para eso sirve el %

También podemos calcular potencias 
```python
>>> 5 ** 2  
25
>>> 2 ** 7  
128
``` 
Para usar el signo =, haremos esto
```Python
>>> width = 20
>>> heigth = 5*9
>>> width * heigth 
900
```


En el modo interactivo, la última expresión impresa se asigna a la variable _. Esto significa que cuando se está utilizando Python como calculadora, es más fácil seguir calculando, por ejemplo:}

```Python
tax = 12.5 / 100
price = 100.50
price * tax
12.5625
price + _
113.0625
round(_, 2)
113.06
```
Esta variable debe ser tratada como de sólo lectura por el usuario. No le asignes explícitamente un valor; crearás una variable local independiente con el mismo nombre enmascarando la variable con el comportamiento mágico.

## 3.1.2. Texto
Python puede manipular texto (representado por el tipo str, conocido como «cadenas de caracteres») al igual que números. Podemos ocupar varias palabras y las podemos citar con ('...') o con ("...")

```python
>>> 'spam eggs' 
'spam eggs'

>>> "Paris rabbit got your back :)! Yay!"  
'Paris rabbit got your back :)! Yay!'

>>> '1975'  
'1975'
```

Algo mas que podemos usar es el print(), esto produce una salida más legible, omitiendo las comillas de encuadre e imprimiendo caracteres escapados y especiales:

```Python
>>> s = 'hola mundo. \nadios mundo.' # \n es cambio de linea nuevo
>>> s # sin el print, el mensaje se pasa igual
'hola mundo. \nadios mundo.'
>>> print(s)
hola mundo.
adios mundo.
```


Algunas oarabras podrian empezar con n y ocurriria un error por el \n entonces en esos casos agregaremos una r, ejemplo:

```Python
print('C:\some\name')  # aquí \n significa nueva línea!
C:\some
ame
print(r'C:\some\name')  # agregar r
C:\some\name
```


Las cadenas literales pueden abarcar varias líneas. Una forma de hacerlo es utilizando comillas triples: """...""" o '''...'''. Los caracteres de fin de línea se incluyen automáticamente en la cadena, pero es posible evitarlo añadiendo un \ al final de la línea. En el siguiente ejemplo, no se incluye el salto de línea inicial:

```python
>>> print("""\
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
>>> 
```
si no ocpamos la / habra un saltp de linea al inicio 
``` Python
>>> print("""
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)
(espacio en blanco)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
>>> 
```
el espacio en blanco significa que salto de linea 

## 3.1.3. Listas
Python tiene varios tipos de datos compuestos, utilizados para agrupar otros valores. El más versátil es la lista, la cual puede ser escrita como una lista de valores separados por coma (ítems) entre corchetes. Las listas pueden contener ítems de diferentes tipos, pero usualmente los ítems son del mismo tipo.

```Python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

La función predefinida len() también sirve para las listas
```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

## 3.2. Primeros pasos hacia la programación
con esto podemos aprender a hacer una serie de fibonicci 
```Python
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

0
1
1
2
3
5
8
```

La función print() escribe el valor de los argumentos que se le proporcionan. Se diferencia de simplemente escribir la expresión que deseas escribir (como hicimos anteriormente en los ejemplos de la calculadora) en la forma en que maneja múltiples argumentos, cantidades de punto flotante y cadenas. Las cadenas se imprimen sin comillas y se inserta un espacio entre los elementos, por lo que puedes darles un formato agradable, como este:

```python
i = 256*256
print('The value of i is', i)
The value of i is 65536
```

con la cadena llamada end podemos evitar que termine e inicie una nueva cadena 
```python 
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```
