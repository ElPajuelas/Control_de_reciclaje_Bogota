# Sistema de Control de Reciclaje

Este es un proyecto en Python diseñado para promover el reciclaje a través de un sistema de puntos. Los usuarios pueden registrar diferentes tipos de residuos reciclables y obtener puntos según el tipo y peso del material. El objetivo es fomentar hábitos sostenibles en hogares y comunidades mediante un sistema sencillo, educativo e interactivo.

---

## Justificación
El sistema busca incentivar la clasificación adecuada de residuos reciclables, permitiendo a las familias llevar control de los materiales que reciclan, ganar puntos simbólicos y adquirir consciencia ecológica.

---

## Características
- Registro de usuarios con información básica y familiares.
- Clasificación y registro de residuos por tipo: papel, cartón, plásticos, vidrio, metales, Tetra Pak.
- Asignación de puntos según el tipo de material y peso ingresado.
- Visualización de historial de materiales reciclados por usuario.
- Menú interactivo para fácil navegación en consola.

---

## Tecnologías utilizadas
- Python 3.10+
- Programación Orientada a Objetos (OOP)
- Módulo `abc` 
- Módulo `unicodedata` 

---

##  Estructura del Proyecto
```
├── Main.py                        # Punto de entrada del programa
├── Controlador.py                 # Lógica de control (flujo del programa)
├── Modelo.py                      # Definición de clases (Usuario, Residuo y subclases)
├── Vista.py                       # Funciones de entrada/salida (interfaz de consola)
├── Documentacion_Tecnica_Reciclaje.docx  # Documento técnico completo
├── README.md                      # Este archivo
```

---

## 📋 Cómo ejecutar el sistema
1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga los archivos del respositorio.
3. Ejecuta el archivo principal:

```bash
Main.py
```

4. Navega por el menú interactivo:
```
1. Agregar usuario
2. Mostrar información del usuario
3. Añadir material reciclable
4. Mostrar materiales ingresados por usuario
5. Salir
```

---

## Casos de Uso
- **Registro de Usuario**: El usuario ingresa su nombre, dirección y cantidad de integrantes del hogar.
- **Elección de Usuario**: Los datos almacenados de usuarios son guardados en una lista y lista para su ejecución.
- **Registro de Residuos**: Selección del tipo de residuo y peso para calcular puntos automáticamente.
- **Consulta de Historial**: Visualización del historial de reciclaje del usuario y puntos acumulados.

---

##  Clases Implementadas
### 🔹 Residuo (abstracta)
- Métodos: `get_tipo()`, `get_peso()`, `set_peso()`, `calcular_puntos()`
- Subclases: `Papel`, `Cartón`, `Plástico PET`, `Plástico HDPE`, `Vidrio`, `Metal Aluminio`, `Metal Cobre`, `Tetra Pack`

### 🔹 Usuario
- Atributos: nombre, n_integrantes, dirección, puntos, historial_residuos
- Métodos: `sumar_puntos()`, `agregar_residuo()`, `mostrar_informacion()`, `mostrar_historial_residuos()`

---

## Diagrama de Clases
El diagrama conceptual se encuentra incluido en el documento `Documentacion_Tecnica_Reciclaje.docx`.

---

##  Estado del proyecto
En desarrollo -- El proyecto esta encaminado a almacenar en la nube los datos, puntos y usuarios.

---

##  Autores
Daniel Estiven Canchon Roa
Luis Alejandro Neira Rivera.

---


