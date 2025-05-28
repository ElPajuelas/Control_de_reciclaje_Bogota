
residuos = {
    "Papel": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendación": "Debe estar limpio y seco."},
    "Cartón": {"Precio por kilo $": 500 , "Puntos por kilo": 50, "Recomendación": "Debe estar limpio y seco."},
    "Plástico PET": {"Precio por kilo $": 1400 , "Puntos por kilo": 140, "Recomendación": "Debe estar limpio y seco."},
    "Plástico HDPE": {"Precio por kilo $": 1150 , "Puntos por kilo": 115, "Recomendación": "Debe estar limpio y seco."},
    "Vidrio": {"Precio por kilo $": 300 , "Puntos por kilo": 30, "Recomendación": "Debe estar limpio y seco."},
    "Metal Aluminio": {"Precio por kilo $": 3500 , "Puntos por kilo": 350, "Recomendación": "Debe estar limpio y seco."},
    "Metal Cobre": {"Precio por kilo $": 17500 , "Puntos por kilo": 1750, "Recomendación": "Debe estar limpio y seco."},
    "Tetra Pack": {"Precio por kilo $": 400 , "Puntos por kilo": 40, "Recomendación": "Debe estar limpio y seco."}
}

def mostrar_informacion_residuos():
    print("\n" + "="*60)
    print("      TIPOS DE RESIDUOS Y SUS DATOS".center(60))
    print("="*60)
    print(f"{'Tipo':<18} {'Puntos/kg':<12} {'Precio/kg ($)':<15} {'Recomendación'}")
    print("-"*60)
    for tipo, datos in residuos.items():
        puntos = datos["Puntos por kilo"]
        precio = datos["Precio por kilo $"]
        recomendacion = datos["Recomendación"]
        print(f"{tipo:<18} {puntos:<12} {precio:<15} {recomendacion}")
    print("="*60 + "\n")
