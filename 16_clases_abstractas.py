from abc import ABC, abstractmethod

class Persona (ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def presentarse(self):
        pass

    @abstractmethod
    def actividad_diaria(self):
        pass

    def cumplir_años(self, años):
        self.edad += años
        return (f'{self.nombre} ha cumplido {años} años')

class Alumno (Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def presentarse (self):
        return(f'Mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.curso}')

    def actividad_diaria(self):
        return('Voy todos los días a clase')

class Profesor (Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        return(f'Mi nombre es {self.nombre}, tengo {self.edad} años y doy {self.asignatura} asignatura')

    def actividad_diaria (self):
        return('Siempre llego puntual')

alumno_1 = Alumno('Lucía', 19, '2ª de Análisis de Datos y de Negocios')
profesor_1 = Profesor('Rufino', 30, 'Programación I')

print(alumno_1.presentarse())
print(alumno_1.actividad_diaria()) 
print(alumno_1.cumplir_años(20))
print(f'\n')
print(profesor_1.presentarse())
print(profesor_1.actividad_diaria())



'''Si intentamos crear directamente: Persona('Pepe', 38) nos aparece un TypeError: Can't instantiate abstract class Persona without an implementation 
for abstract methods 'actividad_diaria', 'presentarse

Esto ocurre debido a que, aunque Persona este definida como una clase abstracta, los métodos abstractos
que contiene no los implementa, ya que solo tiene el pass

El error ocurre porque todas las clases que herden de Persona están obligadas a tener las funciones abstractas,
sin embargo, Persona las tiene defniidas como funciones pero no están implementadas.'''
