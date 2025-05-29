# ♻️ Sistema de Control de Reciclaje

Este es un proyecto en Python diseñado para promover el reciclaje a través de un sistema de puntos. Los usuarios pueden registrar diferentes tipos de residuos reciclables y obtener puntos según el tipo y peso del material. El objetivo es fomentar hábitos sostenibles en hogares y comunidades mediante un sistema sencillo, educativo e interactivo.

---

## 🧠 Justificación
El sistema busca incentivar la clasificación adecuada de residuos reciclables, permitiendo a las familias llevar control de los materiales que reciclan, ganar puntos simbólicos y adquirir consciencia ecológica.

---

## 🚀 Características
- Registro de usuarios con información básica y familiares.
- Clasificación y registro de residuos por tipo: papel, cartón, plásticos, vidrio, metales, Tetra Pak.
- Asignación de puntos según el tipo de material y peso ingresado.
- Visualización de historial de materiales reciclados por usuario.
- Menú interactivo para fácil navegación en consola.

---

## 🧱 Tecnologías utilizadas
- Python 3.10+
- Programación Orientada a Objetos (OOP)
- Módulo `abc` para clases abstractas
- Módulo `unicodedata` para manejo de texto sin tildes

---

## 📂 Estructura del Proyecto
```
├── Control_de_reciclaje.py         # Código fuente principal
├── Documentacion_Tecnica_Reciclaje.docx  # Documento técnico completo
├── README.md                       # Este archivo
```

---

## 📋 Cómo ejecutar el sistema
1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga los archivos.
3. Ejecuta el archivo principal:

```bash
python Control_de_reciclaje.py
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

## 🧪 Casos de Uso
- **Registro de Usuario**: El usuario ingresa su nombre, dirección y cantidad de integrantes del hogar.
- **Registro de Residuos**: Selección del tipo de residuo y peso para calcular puntos automáticamente.
- **Consulta de Historial**: Visualización del historial de reciclaje del usuario y puntos acumulados.

---

## 🧱 Clases Implementadas
### 🔹 Residuo (abstracta)
- Métodos: `get_tipo()`, `get_peso()`, `set_peso()`, `calcular_puntos()`
- Subclases: `Papel`, `Cartón`, `Plástico PET`, `Plástico HDPE`, `Vidrio`, `Metal Aluminio`, `Metal Cobre`, `Tetra Pack`

### 🔹 Usuario
- Atributos: nombre, n_integrantes, dirección, puntos, historial_residuos
- Métodos: `sumar_puntos()`, `agregar_residuo()`, `mostrar_informacion()`, `mostrar_historial_residuos()`

---

## 🖼️ Diagrama de Clases
El diagrama conceptual se encuentra incluido en el documento `Documentacion_Tecnica_Reciclaje.docx`.

---

## ✅ Estado del proyecto
🔧 En desarrollo — se sugiere implementar persistencia de datos (JSON) y soporte para múltiples usuarios.

---

## 👨‍💻 Autor
Proyecto desarrollado por [Tu Nombre Aquí].

---

## 📄 Licencia
Este proyecto se encuentra bajo la licencia MIT.
