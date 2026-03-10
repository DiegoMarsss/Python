# 6. Módulos

Cuando sales del intérprete de Python, las funciones y variables que creaste se pierden. Por eso, para programas más largos es mejor escribir el código en un archivo y ejecutarlo como un script.

Cuando el programa crece, se puede dividir en varios archivos para facilitar su mantenimiento y reutilizar funciones sin copiarlas en cada programa.

Para esto, Python permite guardar definiciones en archivos llamados módulos, que pueden importarse en otros programas. Un módulo es un archivo con extensión .py, y su nombre queda almacenado en la variable global __name__. Como ejemplo, se puede crear un archivo llamado fibo.py con el código deseado.

```py
# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
Ahora entra en el intérprete de Python e importa este modulo con el siguiente comando:
**import fibo**

Importar un módulo como fibo no agrega directamente sus funciones al espacio de nombres actual, sino que solo añade el nombre del módulo. Para usar sus funciones, es necesario llamarlas a través del nombre del módulo (por ejemplo, fibo.función()).

```py
fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo.__name__
'fibo'
```

### 6.1. Más sobre los módulos
Un módulo puede incluir tanto funciones como instrucciones ejecutables, las cuales se ejecutan solo la primera vez que el módulo se importa (o cuando se ejecuta como script).

Cada módulo tiene su propio espacio de nombres, lo que evita conflictos con variables de otros programas. Sin embargo, es posible acceder a sus variables globales usando la notación modname.itemname.

Los módulos pueden importar otros módulos, y normalmente las declaraciones import se colocan al inicio del archivo. También existe una variante de import que permite traer los nombres del módulo directamente al espacio de nombres actual.

```py
from fibo import fib, fib2
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Este tipo de importación no añade el nombre del módulo al espacio de nombres local, por lo que el módulo (por ejemplo, fibo) no queda definido como tal.

También existe una variante que permite importar todos los nombres definidos dentro de un módulo directamente al espacio de nombres actual.

```py
from fibo import *
fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1.1. Ejecutar módulos como scripts
Cuando ejecutes un módulo de Python con

python fibo.py arguments
el código en el módulo será ejecutado, tal como si lo hubieses importado, pero con __name__ con el valor de "__main__". Eso significa que agregando este código al final de tu módulo:

```py
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

puedes hacer que el archivo sea utilizable tanto como script, como módulo importable, porque el código que analiza la línea de órdenes sólo se ejecuta si el módulo es ejecutado como archivo principal:

```py
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
Si el módulo se importa, ese código no se ejecuta:
```py
import fibo
```

Esto es frecuentemente usado para proveer al módulo una interfaz de usuario conveniente, o para fines de prueba (ejecutar el módulo como un script que ejecuta un conjunto de pruebas).

### 6.1.2. El camino de búsqueda de los módulos
Cuando se importa un módulo (por ejemplo, spam), Python primero busca si es un módulo integrado del sistema. Si no lo encuentra, busca un archivo llamado spam.py en los directorios indicados en sys.path.

La variable sys.path incluye:

El directorio del script actual (o el directorio actual si no hay script).

Los directorios definidos en PYTHONPATH.

Los directorios predeterminados de la instalación, como site-packages.

Así, sys.path determina dónde Python busca los módulos al importarlos.

En sistemas que usan enlaces simbólicos, Python calcula el directorio del script después de seguir el enlace, por lo que el directorio del enlace no se agrega a la ruta de búsqueda.

Después de iniciarse, los programas pueden modificar sys.path. El directorio del script en ejecución se coloca al inicio de la búsqueda, antes que la biblioteca estándar.

Esto implica que, si existe un archivo con el mismo nombre que un módulo estándar en ese directorio, Python cargará ese archivo primero, lo cual puede causar errores si no se hace de forma intencional.

### 6.1.3. Archivos «compilados» de Python
Python guarda versiones compiladas de los módulos en la carpeta __pycache__ con extensión .pyc para acelerar su carga. El nombre incluye la versión de Python (por ejemplo, spam.cpython-33.pyc).

El intérprete compara la fecha del archivo fuente .py con la versión compilada para saber si debe recompilarlo. Este proceso es automático y los archivos .pyc son independientes de la plataforma.

No se usa la caché cuando:

El módulo se ejecuta directamente desde la línea de comandos.

No existe el archivo fuente (salvo que el .pyc esté en el directorio correcto para distribución sin código fuente).

Opcionalmente, se pueden usar los modificadores -O y -OO para optimizar y reducir el tamaño del archivo compilado, eliminando assert y/o cadenas __doc__.

Los archivos .pyc no hacen que el programa se ejecute más rápido, solo que se cargue más rápido. El módulo compileall permite generar archivos .pyc para todos los módulos de un directorio.

### 6.2. Módulos estándar
Python incluye una biblioteca estándar con muchos módulos listados en la Referencia de la Biblioteca.

Algunos módulos están integrados directamente en el intérprete para mayor eficiencia o para permitir acceso a funciones del sistema operativo. Estos pueden variar según la plataforma (por ejemplo, winreg solo está disponible en Windows).

Un módulo importante es sys, que está presente en todos los intérpretes de Python. Entre otras cosas, contiene variables como sys.ps1 y sys.ps2, que definen los símbolos del prompt principal y secundario en la consola interactiva.

```py
import sys
sys.ps1
'>>> '
sys.ps2
'... '
sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
Las variables sys.ps1 y sys.ps2 solo existen cuando Python está en modo interactivo.

Por otro lado, sys.path es una lista de rutas que indica dónde el intérprete busca los módulos. Se inicializa usando la variable de entorno PYTHONPATH o con un valor predeterminado si esta no está definida.

Además, sys.path puede modificarse fácilmente utilizando las operaciones normales de listas en Python.

### 6.3. La función dir()
La función integrada dir() se usa para encontrar qué nombres define un módulo. Retorna una lista ordenada de cadenas:
```py
import fibo, sys
dir(fibo)
['__name__', 'fib', 'fib2']
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

Sin argumentos, dir() lista los nombres que tienes actualmente definidos:
```py
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
Nótese que lista todos los tipos de nombres: variables, módulos, funciones, etc.

dir() no lista los nombres de las funciones y variables integradas. Si quieres una lista de esos, están definidos en el módulo estándar builtins:

```py
import builtins
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
 ```

 ### 6.4. Paquetes
 Los paquetes permiten organizar módulos en Python usando nombres con puntos (por ejemplo, A.B, donde B es un submódulo dentro del paquete A).

Esto ayuda a evitar conflictos de nombres, especialmente en proyectos grandes o bibliotecas como NumPy o Pillow, donde existen muchos módulos relacionados.

Por ejemplo, si se quiere crear un paquete para manejar archivos de sonido, se pueden organizar distintos módulos según su función: algunos para trabajar con formatos (.wav, .aiff, .au) y otros para aplicar efectos (mezclar, añadir eco, ecualizar, etc.).

Así, los paquetes permiten estructurar y organizar mejor grandes colecciones de módulos mediante una jerarquía de archivos.

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Al importar un paquete, Python lo busca en los directorios indicados en sys.path.

El archivo __init__.py es necesario para que Python reconozca un directorio como paquete (excepto en paquetes de espacio de nombres). Puede estar vacío o incluir código de inicialización y definir la variable __all__.

Existen varias formas de importar desde un paquete:

import sound.effects.echo → se usa el nombre completo (sound.effects.echo.función).

from sound.effects import echo → permite usar echo.función() sin el prefijo completo.

from sound.effects.echo import echofilter → importa directamente la función y se puede usar como echofilter().

Con from paquete import item, el elemento puede ser un submódulo o un nombre definido en el paquete (función, clase o variable). Si no se encuentra, se produce un ImportError.

En cambio, con import item.subitem.subsubitem, todos los elementos excepto el último deben ser paquetes; el último puede ser un módulo o paquete, pero no una función o variable.

### 6.4.1. Importar * desde un paquete
Cuando el usuario escribe from sound.effects import *, Python no busca automáticamente todos los submódulos en el sistema de archivos, ya que eso podría ser lento y provocar efectos secundarios no deseados.

En su lugar, si el archivo __init__.py del paquete define una lista llamada __all__, esa lista indica qué módulos o nombres se importarán al usar import *.

Es responsabilidad del autor del paquete mantener actualizada la lista __all__. Si no se define, entonces import * solo importará los nombres definidos directamente en __init__.py, y no necesariamente todos los submódulos.
```
__all__ = ["echo", "surround", "reverse"]
```
Esto significaría que from sound.effects import * importaría esos tres submódulos del paquete sound.effects.

Ten en cuenta que los submódulos pueden quedar ocultos por nombres definidos localmente. Por ejemplo, si agregaste una función llamada reverse al archivo sound/effects/__init__.py, from sound.effects import * solo importaría los dos submódulos echo y surround, pero no el submódulo reverse porque queda oculto por la función reverse definida localmente:

```py
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```

Si no se define __all__, la declaración from sound.effects import * no importa todos los submódulos del paquete sound.effects al espacio de nombres actual; sólo se asegura que se haya importado el paquete sound.effects (posiblemente ejecutando algún código de inicialización que haya en __init__.py) y luego importa aquellos nombres que estén definidos en el paquete. Esto incluye cualquier nombre definido (y submódulos explícitamente cargados) por __init__.py. También incluye cualquier submódulo del paquete que pudiera haber sido explícitamente cargado por declaraciones import previas. Considere este código:

```py
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
En este caso, los módulos echo y surround se importan al espacio de nombres actual porque están definidos en el paquete cuando se ejecuta from ... import. Esto también funciona si se ha definido la lista __all__.

Aunque algunos módulos están diseñados para controlar qué se exporta con import *, su uso se considera mala práctica en código profesional.

Lo recomendable es usar from package import specific_submodule, ya que es más claro y seguro, salvo en casos especiales donde haya conflictos de nombres entre submódulos de distintos paquetes.

### 6.4.2. Referencias internas en paquetes
Cuando un paquete tiene subpaquetes, se pueden usar imports absolutos para acceder a módulos de otros subpaquetes.
Por ejemplo, si sound.filters.vocoder necesita usar echo de sound.effects, puede escribir:
from sound.effects import echo.

También se pueden usar imports relativos, que emplean puntos (.) para indicar el paquete actual o los paquetes superiores.
Un punto (.) se refiere al paquete actual, dos puntos (..) al paquete padre, y así sucesivamente.

Esto permite organizar mejor el código dentro de paquetes grandes y mantener referencias más claras entre módulos relacionados.

```py
from . import echo
from .. import formats
from ..filters import equalizer
```

### 6.4.3. Paquetes en múltiples directorios
Los paquetes tienen un atributo especial llamado __path__.

Este se inicializa como una lista de rutas que contiene el directorio donde está el archivo __init__.py, antes de que se ejecute su código.

La variable __path__ puede modificarse, y al hacerlo se cambia la forma en que Python busca futuros módulos o subpaquetes dentro del paquete.

Aunque no se usa con frecuencia, esta característica permite extender o ampliar los módulos que pueden formar parte de un paquete.