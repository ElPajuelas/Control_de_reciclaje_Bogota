from abc import ABC, abstractmethod

# Definicion de la clase Residuo como abstracta
# Esta clase sirve como base para los diferentes tipos de residuos
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

#Metodo abstracto para calcular puntos
#Cada subclase tendra que implementar este metodo

@abstractmethod
def calcular_puntos(self):
    pass
#Definicion de las subclases de residuos
#Cada clase tiene distintos puntos por kilo dependiendo del valor por kilo en el mercado de Bogotá
class Papel(Residuo):
    def __init__ (self, peso):
        super.__init__("Papel", peso)

    def calcular_puntos(self):
        return self.peso * 50
    
class carton(Residuo):
    def __init__ (self, peso):
        super.__init__("Carton", peso)

    def calcular_puntos(self):
        return self.peso * 50

class PlasticoPET(Residuo):
    def __init__ (self, peso):
        super.__init__("Plastico PET", peso)
    def calcular_puntos(self):
        return self.peso * 140
    
class PlasticoHDPE(Residuo):
    def __init__ (self, peso):
        super.__init__("Plastico HDPE", peso)
    def calcular_puntos(self):
        return self.peso * 115
    
class Vidrio(Residuo):
    def __init__(self, peso):
        super.__init__("Vidrio", peso)
    def calcular_puntos(self):
        return self.peso * 30
class MetalAluminio(Residuo):
    def __init__ (self, peso):
        super.__init__("Metal Aluminio", peso)
    def calcular_puntos(self):
        return self.peso * 350

class MetalCobre(Residuo):
    def __init__ (self, peso):
        super.__init__("Metal Cobre", peso)
    def calcular_puntos(self):
        return self.peso * 1750
    
class TetraPack(Residuo):
    def __init__ (self, peso):
        super.__init__("Tetra Pack", peso)
    def calcular_puntos(self):
        return self.peso * 40

#8 subclases de residuos
#Clase usuario usada para almacenar los datos de los usuarios
class Usuario:
    def __init__(self, nombre, cedula, puntos=0):
        self.nombre = nombre
        self.cedula = cedula
        self.puntos = puntos
        self.historial_residuos = []

    def get_nombre(self):
        return self.nombre
    def get_cedula(self):   
        return self.cedula
    def get_puntos(self):
        return self.puntos
    
    def sumar_puntos(self, puntos):
        self.puntos += puntos
    
    def agregar_residuo(self, residuo):
        self.historial_residuos.append(residuo)
#Diccionario para alamacenar los residuos y sus datos
residuos= {
    "Papel": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendacion": "El papel debe estar limpio y seco. No se aceptan papeles plastificados o encerados."},
    "Carton": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendacion": "El carton debe estar limpio y seco. No se aceptan cajas de pizza o carton plastificado."},
    "Plastico PET": {"Precio por kilo $": 1400 , "Puntos por kilo": 140, "Recomendacion": "El plastico PET debe estar limpio y seco. No se aceptan botellas con residuos de productos quimicos."},
    "Plastico HDPE": {"Precio por kilo $": 1150 , "Puntos por kilo": 115, "Recomendacion": "El plastico HDPE debe estar limpio y seco. No se aceptan botellas con residuos de productos quimicos."},
    "Vidrio": {"Precio por kilo $": 300 , "Puntos por kilo": 30, "Recomendacion": "El vidrio debe estar limpio y seco. No se aceptan botellas con residuos de productos quimicos."},
    "Metal Aluminio": {"Precio por kilo $": 3500 , "Puntos por kilo": 350, "Recomendacion": "El metal aluminio debe estar limpio y seco. No se aceptan latas con residuos de productos quimicos."},
    "Metal Cobre": {"Precio por kilo $": 17500 , "Puntos por kilo": 1750, "Recomendacion": "El metal cobre debe estar limpio y seco. No se aceptan latas con residuos de productos quimicos."},
    "Tetra Pack": {"Precio por kilo $": 400 , "Puntos por kilo": 40, "Recomendacion": "El tetra pack debe estar limpio y seco. No se aceptan tetrabriks con residuos de productos quimicos."}
}
#Se crea una funcion para mostrar los residuos y sus datos
def mostrar_informacion_residuos():
    print("\n" + "="*60)
    print("      TIPOS DE RESIDUOS Y SUS DATOS".center(60))
    print("="*60)
    print(f"{'Tipo':<18} {'Puntos/kg':<12} {'Precio/kg ($)':<15} {'Recomendación'}")
    print("-"*60)
    for tipo, datos in residuos.items():
        puntos = datos["Puntos por kilo"]
        precio = datos["Precio por kilo $"]
        recomendacion = datos["Recomendacion"]
        print(f"{tipo:<18} {puntos:<12} {precio:<15} {recomendacion}")
    print("="*60 + "\n")



#Se inicializa las listas de usarios para crear una base de datos de cada usuario y su registro de reciclaje
usuarios = []

while True:
    print("Bienvenido al sistema de control de reciclaje")
    print("1. Agregar usuario")
    print("2. Agregar residuo")
    print("3. Mostrar usuarios")
    print("4. Mostrar residuos")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        cedula = input("Ingrese la cedula del usuario: ")
        nuevo_usuario = Usuario(nombre, cedula)
        usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} agregado con exito.")
    elif opcion == "2":
        mostrar_informacion_residuos()
        tipo_residuo = input("Ingrese el tipo de residuo: ").lower()
        peso_residuo = float(input("Ingrese el peso del residuo (kg). Recuerde que el peso puede ser decimal: "))

