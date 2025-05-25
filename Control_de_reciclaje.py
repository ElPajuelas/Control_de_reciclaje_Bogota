from abc import ABC, abstractmethod

# Clase base abstracta
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

# Subclases
class Papel(Residuo):
    def __init__(self, peso):
        super().__init__("Papel", peso)
    def calcular_puntos(self):
        return self.peso * 50

class Carton(Residuo):
    def __init__(self, peso):
        super().__init__("Carton", peso)
    def calcular_puntos(self):
        return self.peso * 50

class PlasticoPET(Residuo):
    def __init__(self, peso):
        super().__init__("Plastico PET", peso)
    def calcular_puntos(self):
        return self.peso * 140

class PlasticoHDPE(Residuo):
    def __init__(self, peso):
        super().__init__("Plastico HDPE", peso)
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

# Clase Usuario
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

# Diccionario de residuos
residuos = {
    "Papel": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendacion": "Debe estar limpio y seco."},
    "Carton": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendacion": "Debe estar limpio y seco."},
    "Plastico PET": {"Precio por kilo $": 1400 , "Puntos por kilo": 140, "Recomendacion": "Debe estar limpio y seco."},
    "Plastico HDPE": {"Precio por kilo $": 1150 , "Puntos por kilo": 115, "Recomendacion": "Debe estar limpio y seco."},
    "Vidrio": {"Precio por kilo $": 300 , "Puntos por kilo": 30, "Recomendacion": "Debe estar limpio y seco."},
    "Metal Aluminio": {"Precio por kilo $": 3500 , "Puntos por kilo": 350, "Recomendacion": "Debe estar limpio y seco."},
    "Metal Cobre": {"Precio por kilo $": 17500 , "Puntos por kilo": 1750, "Recomendacion": "Debe estar limpio y seco."},
    "Tetra Pack": {"Precio por kilo $": 400 , "Puntos por kilo": 40, "Recomendacion": "Debe estar limpio y seco."}
}

# Mostrar tabla de residuos
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

# Lógica principal
usuarios = []

while True:
    print("\nBienvenido al sistema de control de reciclaje")
    if len(usuarios) == 0:
        print("1. Agregar usuario")
    print("2. Mostrar información del usuario")
    print("3. Añadir material reciclable")
    print("4. Mostrar materiales ingresados por usuario")
    print("5. Salir")
    opcion = input("Por favor, selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario representante: ")
        try:
            n_integrantes = int(input("Ingrese el número adicional de integrantes de su familia: "))
            direccion = input("Ingrese la dirección de su grupo familiar: ")
            nuevo_usuario = Usuario(nombre, n_integrantes, direccion) 
            usuarios.append(nuevo_usuario)
            print(f"El usuario {nombre} fue agregado con éxito.")
        except ValueError:
            print("Error: El número de integrantes de tu familia debe ser lógico")

    elif opcion == "2":
        if not usuarios:
            print("Primero debe registrar un usuario (opción 1).")
            continue

        usuario = usuarios[0]
        print("\nInformación del titular registrada:")
        print(f"Nombre del titular: {usuario.get_nombre()}")
        print(f"Número de integrantes de la familia: {usuario.get_n_integrantes()}")
        print(f"Dirección: {usuario.get_direccion()}")

        if not usuario.nombres_integrantes:
            respuesta = input("¿Desea ingresar nombres de los integrantes? (si/no): ").lower()
            if respuesta == "si":
                for i in range(1, usuario.get_n_integrantes() + 1):
                    nombre = input(f"Nombre del integrante {i}: ")
                    usuario.nombres_integrantes.append(nombre)

        if not usuario.id_titular:
            respuesta = input("¿Desea ingresar el documento del titular? (si/no): ").lower()
            if respuesta == "si":
                usuario.id_titular = input("Ingrese el número de documento del titular: ")

        print("\nResumen:")
        print(f"Titular: {usuario.get_nombre()}")
        print(f"Número de integrantes: {usuario.get_n_integrantes()}")
        print(f"Dirección: {usuario.get_direccion()}")
        if usuario.nombres_integrantes:
            for i, nombre in enumerate(usuario.nombres_integrantes, 1):
                print(f" - Integrante {i}: {nombre}")
        if usuario.id_titular:
            print(f"Número de documento del titular: {usuario.id_titular}")

    elif opcion == "3":
        if not usuarios:
            print("Primero debe registrar un usuario (opción 1).")
            continue

        usuario = usuarios[0]
        mostrar_informacion_residuos()
        tipo_residuo = input("Ingrese el tipo de residuo: ").strip()

        if tipo_residuo not in residuos:
            print("Tipo de residuo no válido.")
            continue

        try:
            peso = float(input("Ingrese el peso (kg): "))
            if peso < 0:
                print("El peso no puede ser negativo.")
                continue
        except ValueError:
            print("Peso inválido.")
            continue

        puntos_kilo = residuos[tipo_residuo]["Puntos por kilo"]
        puntos_totales = peso * puntos_kilo

        clases = {
            "Papel": Papel, "Carton": Carton, "Plastico PET": PlasticoPET,
            "Plastico HDPE": PlasticoHDPE, "Vidrio": Vidrio,
            "Metal Aluminio": MetalAluminio, "Metal Cobre": MetalCobre,
            "Tetra Pack": TetraPack
        }
        residuo = clases[tipo_residuo](peso)
        usuario.agregar_residuo(residuo)
        usuario.sumar_puntos(residuo.calcular_puntos())

        print("\n✅ Registro exitoso:")
        print(f"Titular: {usuario.get_nombre()}")
        print(f"Material: {tipo_residuo}")
        print(f"Peso: {peso} kg")
        print(f"Puntos obtenidos: {int(puntos_totales)}")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
