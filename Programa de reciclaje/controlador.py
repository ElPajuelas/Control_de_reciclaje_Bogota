
import unicodedata
from modelo import *
from vista import mostrar_informacion_residuos, residuos

usuarios = []

def seleccionar_usuario():
    if not usuarios:
        print("No hay usuarios registrados.")
        return None

    print("\nUsuarios registrados:")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario.get_nombre()} - {usuario.get_direccion()}")
    
    try:
        seleccion = int(input("Selecciona el número del usuario: ")) - 1
        if 0 <= seleccion < len(usuarios):
            return usuarios[seleccion]
        else:
            print("Selección inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None


def quitar_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

def ejecutar_aplicacion():
    while True:
        print("\nBienvenido al sistema de control de reciclaje")
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
                direccion = input("Ingrese su domicilo correspondiente: ")
                nuevo_usuario = Usuario(nombre, n_integrantes, direccion) 
                usuarios.append(nuevo_usuario)
                print(f"El usuario {nombre} fue agregado con éxito.")
            except ValueError:
                print("Error: El número de integrantes de tu familia debe ser lógico")

        elif opcion == "2":
            usuario = seleccionar_usuario()
            if usuario is None:
                continue

            print("\n" + "="*60)
            print("      INFORMACIÓN DEL USUARIO".center(60))
            print("="*60)
            usuario.mostrar_informacion()

            if usuario.get_n_integrantes() > 0 and not usuario.nombres_integrantes:
                respuesta = input("¿Desea ingresar nombres de los integrantes de su familia? (si/no): ").lower()
                if respuesta == "si":
                    for i in range(1, usuario.get_n_integrantes() + 1):
                        nombre = input(f"Nombre del integrante {i}: ")
                        usuario.nombres_integrantes.append(nombre)

            if not usuario.id_titular:
                respuesta = input("¿Desea ingresar el documento del titular? (si/no): ").lower()
                if respuesta == "si":
                    usuario.id_titular = input("Ingrese el número de documento del titular: ")

            print("\n" + "="*60)
            print("      Resumen".center(60))
            print("="*60)
            usuario.mostrar_informacion()

            if usuario.nombres_integrantes:
                for i, nombre in enumerate(usuario.nombres_integrantes, 1):
                    print(f" - Integrante {i}: {nombre}")
            if usuario.id_titular:
                print(f"Número de documento del titular: {usuario.id_titular}")

        elif opcion == "3":
            usuario = seleccionar_usuario()
            if usuario is None:
                continue

            mostrar_informacion_residuos()
            residuos_normalizados = {quitar_tildes(k.lower()): k for k in residuos.keys()}
            tipo_residuo_input = input("Ingrese el tipo de residuo: ").strip().lower()
            tipo_residuo_normalizado = quitar_tildes(tipo_residuo_input)

            if tipo_residuo_normalizado not in residuos_normalizados:
                print("Ingrese un material que esté en la lista.")
                continue

            tipo_residuo = residuos_normalizados[tipo_residuo_normalizado]

            try:
                peso = float(input("Ingrese el peso (kg): "))
                if peso < 0:
                    print("El peso no puede ser negativo.")
                    continue
            except ValueError:
                print("El peso no es lógico.")
                continue

            puntos_kilo = residuos[tipo_residuo]["Puntos por kilo"]
            puntos_totales = peso * puntos_kilo

            clases = {
                "Papel": Papel, "Cartón": Carton, "Plástico PET": PlasticoPET,
                "Plástico HDPE": PlasticoHDPE, "Vidrio": Vidrio,
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

        elif opcion == "4":
            usuario = seleccionar_usuario()
            if usuario is None:
                continue

            print("\n" + "="*60)
            print("      MATERIALES INGRESADOS POR EL USUARIO".center(60))
            print("="*60)
            usuario.mostrar_historial_residuos()
            print(f"Puntos totales acumulados: {usuario.get_puntos()}")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
