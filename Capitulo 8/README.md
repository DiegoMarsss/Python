# 8. Errores y excepciones
Hasta ahora los mensajes de error apenas habían sido mencionados, pero si has probado los ejemplos anteriores probablemente hayas visto algunos. Hay (al menos) dos tipos diferentes de errores: errores de sintaxis y excepciones.

### 8.1. Errores de sintaxis
Los errores de sintaxis, también conocidos como errores de interpretación, son quizás el tipo de queja más común que tenés cuando todavía estás aprendiendo Python:
```py
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```
Cuando hay un error, Python muestra la línea donde ocurrió y marca con flechas el lugar detectado. Sin embargo, ese punto no siempre es exactamente donde está el error; a veces es antes, como cuando falta un :.

También se muestra el nombre del archivo y el número de línea para que puedas ubicar fácilmente el problema, especialmente si el código viene de un archivo.

### 8.2. Excepciones
Aunque el código esté bien escrito (sin errores de sintaxis), puede fallar al ejecutarse. A estos errores se les llama excepciones.

Las excepciones no siempre detienen el programa, porque se pueden manejar, pero si no se controlan, muestran mensajes de error como los que normalmente aparecen en Python.
```py
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

La última línea del error indica qué pasó exactamente. También muestra el tipo de excepción, como ZeroDivisionError, NameError o TypeError, que son errores ya definidos por Python. Estos nombres identifican el tipo de problema y normalmente son parte del sistema, aunque también se pueden crear excepciones propias.

Esa misma línea también da más detalles sobre la causa del error. Antes de eso, aparece un seguimiento que muestra en qué parte del código ocurrió (líneas y contexto), lo que ayuda a encontrar el problema más fácilmente.

### 8.3. Gestionando excepciones
Se pueden crear programas que controlen errores (excepciones). Por ejemplo, puedes pedir un dato al usuario hasta que ingrese un número válido.

Además, el programa puede permitir que el usuario lo interrumpa (como con Ctrl + C), lo cual genera una excepción llamada KeyboardInterrupt.
```py
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
La sentencia try se usa para manejar errores. Primero se ejecuta el código dentro de try.

Si no ocurre ningún error, el bloque except se ignora y el programa sigue normal.

Si ocurre una excepción, se detiene el try y se ejecuta el except correspondiente (si coincide con el tipo de error). Luego el programa continúa después del bloque.

Si el error no coincide con ningún except, se pasa a otro try externo. Si nadie lo maneja, el programa se detiene y muestra un error.


Un try puede tener varios except para manejar diferentes errores, pero solo uno se ejecuta según el tipo de excepción.

Los except solo capturan errores que ocurren dentro del try, no dentro de otros except. Además, un mismo except puede manejar varios tipos de excepciones al mismo tiempo.

```py
except RuntimeError, TypeError, NameError:
...     pass
```

En un except, una clase de excepción también captura errores de sus clases derivadas (hijas), pero no al revés. Es decir, una excepción general puede atrapar errores más específicos.

Por eso, el orden importa: primero se ponen las excepciones más específicas y luego las más generales, para que funcionen correctamente.

```py
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

El orden de los except es importante, porque Python usa el primero que coincida. Si se ponen al revés (uno más general antes), puede capturar todos los errores y no dejar pasar a los demás.

Cuando ocurre una excepción, puede tener información adicional (argumentos). En un except, puedes guardarla en una variable para usarla después.

Esa variable representa el error y normalmente guarda sus datos en args, aunque se puede imprimir directamente porque ya está preparado para mostrarse fácilmente.

```py
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
El método __str__() de una excepción es lo que se muestra como mensaje final cuando ocurre un error no manejado.

BaseException es la clase principal de todas las excepciones. De ahí viene Exception, que agrupa la mayoría de errores comunes que sí se pueden manejar. Otras como SystemExit o KeyboardInterrupt no suelen manejarse porque indican que el programa debe terminar.

Se puede usar Exception para atrapar casi todos los errores, pero es mejor ser específico con el tipo de excepción. Una práctica común es mostrar el error y luego volver a lanzarlo para que otro código también pueda manejarlo.

```py
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

La declaración try … except tiene una cláusula else opcional, que, cuando está presente, debe seguir todas las cláusulas except. Es útil para el código que debe ejecutarse si la cláusula try no lanza una excepción. Por ejemplo:

```py
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Usar la cláusula else es mejor que poner más código dentro de try, porque así evitas atrapar errores que no pertenecen a lo que realmente quieres controlar.

Además, el try no solo captura errores que ocurren directamente ahí, sino también los que pasan dentro de funciones que se llaman desde ese bloque, incluso si son llamadas indirectas.
```py
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

Handling run-time error: division by zero
```

### 8.4. Lanzando excepciones
La declaración raise permite al programador forzar a que ocurra una excepción específica. Por ejemplo:
```py
raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
```

La instrucción raise se usa para lanzar una excepción. Puede recibir una instancia de excepción o una clase que herede de BaseException.

Si pasas solo la clase (como ValueError), Python la crea automáticamente como si hubieras escrito ValueError().

Si es necesario determinar si una excepción fue lanzada pero sin intención de gestionarla, una versión simplificada de la instrucción raise te permite relanzarla:

```py
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
```

### 8.5. Encadenamiento de excepciones
Si se produce una excepción no gestionada dentro de una sección except, se le adjuntará la excepción que se está gestionando y se incluirá en el mensaje de error:

```py
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error
```

Para indicar que una excepción es consecuencia directa de otra, la sentencia raise permite una cláusula opcional from:
```py
# exc must be exception instance or None.
raise RuntimeError from exc
```
Esto puede resultar útil cuando está transformando excepciones. Por ejemplo:
```py
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
```

También permite deshabilitar el encadenamiento automático de excepciones utilizando el modismo from None:
```py
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError
```
Para obtener más información sobre la mecánica del encadenamiento, consulte Excepciones incorporadas.


### 8.6. Excepciones definidas por el usuario
En Python puedes crear tus propias excepciones definiendo una clase, normalmente heredando de Exception.

Estas clases suelen ser simples y solo guardan información sobre el error. Por convención, sus nombres terminan en Error, igual que las excepciones de Python.

Además, muchos módulos ya tienen sus propias excepciones para manejar errores específicos de sus funciones.

### 8.7. Definiendo acciones de limpieza
La sentencia try puede tener una cláusula opcional llamada finally, que se usa para ejecutar código de limpieza.

Este bloque se ejecuta siempre, ocurra o no un error, por ejemplo para cerrar archivos o liberar recursos.
```py
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
```

Si existe finally, este bloque siempre se ejecuta al final, haya ocurrido o no una excepción en try.

Si ocurre un error en try, puede ser manejado por except. Si no se maneja, el error se vuelve a lanzar después de ejecutar finally. Lo mismo pasa si el error ocurre en except o else: primero se ejecuta finally y luego el error continúa.

Si dentro de finally se usa break, continue o return, el comportamiento puede ser confuso porque evita que la excepción se vuelva a lanzar, por eso no se recomienda.

Además, si try tiene un break, continue o return, finally se ejecuta justo antes. Y si finally tiene un return, ese valor es el que se devuelve, ignorando el del try, lo cual también puede causar confusión.

Por ejemplo:
```py
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()
False
```
Un ejemplo más complicado:

```py
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
result is 2.0
executing finally clause
divide(2, 0)
division by zero!
executing finally clause
divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
Como se ve, finally siempre se ejecuta. Si ocurre un error (como un TypeError) y no es manejado por except, igual se ejecuta finally y después el error vuelve a lanzarse.

En la práctica, finally se usa para liberar recursos, como cerrar archivos o conexiones, sin importar si hubo errores o no.

### 8.8. Acciones predefinidas de limpieza
Algunos objetos ya tienen acciones de limpieza automáticas cuando dejan de usarse, sin importar si todo salió bien o hubo errores.

Por ejemplo, al trabajar con archivos, se puede abrir uno y mostrar su contenido, y el propio objeto se encarga de cerrarlo correctamente al final.
```py
for line in open("myfile.txt"):
    print(line, end="")
```

El problema es que el archivo puede quedarse abierto por tiempo indefinido después de ejecutarse el código. En programas simples no afecta mucho, pero en aplicaciones grandes sí puede causar problemas.

Para evitar esto, se usa with, que asegura que el archivo se cierre automáticamente y de forma correcta al terminar de usarse.
```py
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Cuando se usa with, el archivo siempre se cierra al terminar, incluso si ocurre un error durante la ejecución.

Los objetos que tienen este tipo de comportamiento (como los archivos) lo indican en su documentación, ya que incluyen limpieza automática.


### 8.9. Lanzando y gestionando múltiples excepciones no relacionadas
A veces es necesario manejar varias excepciones al mismo tiempo, por ejemplo cuando varias tareas fallan en paralelo o cuando se quiere seguir ejecutando el programa y reunir todos los errores en lugar de detenerse en el primero.

Para esto existe ExceptionGroup, que permite agrupar varias excepciones y lanzarlas juntas como una sola, pudiendo manejarse igual que cualquier otra excepción.

```py
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')

caught <class 'ExceptionGroup'>: e
```

Usando except* en lugar de except, se pueden manejar solo ciertas excepciones dentro de un grupo (ExceptionGroup).

Cada except* toma las excepciones del tipo que le corresponde y deja pasar las demás para que otros except* las manejen o, si no, se vuelvan a lanzar.
```py
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
```

En un ExceptionGroup, las excepciones deben ser instancias (objetos ya creados), no solo tipos o clases.

Esto es porque normalmente se agrupan errores que ya ocurrieron y fueron capturados previamente en el programa.
```py
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)
```

### 8.10. Enriqueciendo excepciones con notas
Cuando se crea una excepción, normalmente incluye información sobre el error. Pero también se puede agregar más información después de capturarla.

Para eso existe add_note(note), que permite añadir mensajes extra. Estas notas aparecen en el error final, en el orden en que se agregaron, dando más contexto sobre lo ocurrido.

```py
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
```

Por ejemplo, cuando agrupas varias excepciones en un ExceptionGroup, puedes agregar información extra a cada una.

Así, cada error puede tener una nota que explique mejor el contexto, como cuándo ocurrió, haciendo más fácil entender qué pasó.

```py
def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     raise ExceptionGroup('We have some problems', excs)
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
```