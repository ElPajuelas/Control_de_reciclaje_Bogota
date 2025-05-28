
from abc import ABC, abstractmethod

class Residuo(ABC):
    def __init__(self, tipo, peso):
        self.tipo = tipo
        self.peso = peso

    def get_tipo(self):
        return self.tipo

    def get_peso(self):
        return self.peso    

    def set_peso(self, nuevo_peso: float):
        if nuevo_peso >= 0:
            self.peso = nuevo_peso
        else:
            print("El peso no puede ser negativo")   

    @abstractmethod
    def calcular_puntos(self):
        pass

class Papel(Residuo):
    def __init__(self, peso):
        super().__init__("Papel", peso)
    def calcular_puntos(self):
        return self.peso * 50

class Carton(Residuo):
    def __init__(self, peso):
        super().__init__("Cartón", peso)
    def calcular_puntos(self):
        return self.peso * 50

class PlasticoPET(Residuo):
    def __init__(self, peso):
        super().__init__("Plástico PET", peso)
    def calcular_puntos(self):
        return self.peso * 140

class PlasticoHDPE(Residuo):
    def __init__(self, peso):
        super().__init__("Plástico HDPE", peso)
    def calcular_puntos(self):
        return self.peso * 115

class Vidrio(Residuo):
    def __init__(self, peso):
        super().__init__("Vidrio", peso)
    def calcular_puntos(self):
        return self.peso * 30

class MetalAluminio(Residuo):
    def __init__(self, peso):
        super().__init__("Metal Aluminio", peso)
    def calcular_puntos(self):
        return self.peso * 350

class MetalCobre(Residuo):
    def __init__(self, peso):
        super().__init__("Metal Cobre", peso)
    def calcular_puntos(self):
        return self.peso * 1750

class TetraPack(Residuo):
    def __init__(self, peso):
        super().__init__("Tetra Pack", peso)
    def calcular_puntos(self):
        return self.peso * 40

class Usuario:
    def __init__(self, nombre, n_integrantes, direccion, puntos=0):
        self.nombre = nombre
        self.n_integrantes = n_integrantes
        self.direccion = direccion
        self.puntos = puntos
        self.historial_residuos = []
        self.nombres_integrantes = []  
        self.id_titular = None

    def get_nombre(self):
        return self.nombre
    def get_n_integrantes(self):   
        return self.n_integrantes
    def get_direccion(self):
        return self.direccion
    def get_puntos(self):
        return self.puntos

    def sumar_puntos(self, puntos):
        self.puntos += puntos

    def agregar_residuo(self, residuo):
        self.historial_residuos.append(residuo)

    def mostrar_informacion(self):
        print(f"Nombre del Titular: {self.nombre}")
        print(f"Número de integrantes de la familia: {self.n_integrantes}")
        print(f"Dirección: {self.direccion}")
        print(f"Puntos acumulados: {self.puntos}")  

    def mostrar_historial_residuos(self):
        if not self.historial_residuos:
            return print("No hay nada registrado.")
        else:
            print("\nHistorial de materiales ingresados:")
            for residuo in self.historial_residuos:
                print(f"Tipo: {residuo.get_tipo()}, Peso: {residuo.get_peso()} kg, Puntos: {residuo.calcular_puntos()}")
            print("="*60)
