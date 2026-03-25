class Persona:
    especie = "Humano"  

    def __init__(self, nombre, edad):
        self.nombre = nombre      
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  
        self.matricula = matricula
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0


class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        return f"Estoy enseñando {self.materia}"


class Escuela:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__estudiantes = []  

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for e in self.__estudiantes:
            print(e.nombre)


e1 = Estudiante("Diego", 16, "A123")
e2 = Estudiante("Cesar", 17, "B456")

p1 = Profesor("Carlos", 40, "Matemáticas")

e1.agregar_calificacion(10)
e1.agregar_calificacion(9)

print(e1.saludar())        
print(e1.promedio())      
print(p1.enseñar())


escuela = Escuela("Mi Escuela")
escuela.agregar_estudiante(e1)
escuela.agregar_estudiante(e2)

escuela.mostrar_estudiantes()