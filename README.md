# Talleres de Python
## Descripción
Este repositorio reúne talleres, ejercicios y prácticas en Python organizados por clases y temas. Contiene ejemplos de programación básica (tipos, estructuras de control, funciones), un proyecto modular de calculadora, y materiales para manipulación y visualización de datos (archivos CSV/XLSX y ejemplos con pandas y matplotlib).

## Objetivos
Agrupar ejercicios y prácticas para el aprendizaje de los fundamentos de Python.
Mostrar modularización y uso de funciones en pequeños proyectos (por ejemplo, la calculadora).
Proveer ejemplos introductorios de manipulación y visualización de datos con pandas y matplotlib.

## Tecnologías y herramientas
- Python
- Librerías encontradas en el código:
  * pandas — ejemplos y manipulación de DataFrame (Clase2, PANDAS).
  * matplotlib — visualización (Clase2/grafico.py).
  * numpy — importado en main.py (aparece en el código).
- Archivos de datos incluidos:
  * tips.csv
  * ventas_limpio.xlsx

## Estructura del repositorio
Repositorio/ ├── Clase2/ │ ├── Taller1.py │ ├── clase2.py │ └── grafico.py ├── PANDAS/ │ └── primerPandas.py ├── Taller/ │ ├── Funciones propias de python.py │ ├── Listas y duplas.py │ ├── Parte final Estudiantes.py │ ├── Variables y operaciones.py │ └── funciones creadas por usuario.py ├── calculadora.py ├── clase1.py ├── dividir.py ├── main.py ├── menu.py ├── multiplicar.py ├── potenciar.py ├── restar.py ├── sumar.py ├── tips.csv ├── ventas_limpio.xlsx └── README.md

## Talleres y ejercicios
### Calculadora
Archivos principales:
calculadora.py — menú interactivo y control de flujo para seleccionar operaciones.
menu.py — imprime las opciones del menú (menu()).
sumar.py, restar.py, multiplicar.py, dividir.py, potenciar.py — funciones para cada operación; cada función lee valores con input() y retorna el resultado.
Temas trabajados: modularización, funciones, entrada/salida por consola, manejo básico de casos (ej. división por cero).
Funcionamiento: ejecutar python calculadora.py y seguir las indicaciones por consola.
### Carpeta: Taller
Archivos y foco:
- Funciones propias de python.py — uso de funciones integradas y manipulación básica de strings y listas.
- Listas y duplas.py — operaciones con colecciones (promedio, sum).
- Parte final Estudiantes.py — (Uso de tuplas para imprimir datos de estudiante ).
- Variables y operaciones.py — variables y operaciones básicas.
- funciones creadas por usuario.py — creación y uso de funciones definidas por el usuario.
Temas: variables, listas, tuplas/sets, funciones, filtrado, enumerate.
### Carpeta: Clase2
#### Archivos:
- Taller1.py — ejemplo con pandas: creación de DataFrame de estudiantes, cálculo de promedio, filtrado y exportación a CSV (aprobados.csv).
- clase2.py — ejemplos y snippets para leer tips.csv y ventas_limpio.xlsx, selección y agregación (usa pandas).
- grafico.py — ejemplos de visualización con matplotlib (líneas, barras, torta). Contiene código comentado y ejemplos de uso con DataFrame.
#### Temas: 
pandas (DataFrame, lectura/escritura), matplotlib (gráficas). Algunos fragmentos están comentados y requieren datos (por ejemplo datosventa.xlsx) — revisar para ajustar rutas/archivos.
### Carpeta: PANDAS
#### Archivos:
- primerPandas.py — crea un DataFrame desde un diccionario y lo exporta a CSV (dataframepython.csv).
#### Temas: 
introducción a pandas: DataFrame, to_csv.

## Librerías utilizadas
- pandas — manipulación de datos tabulares (leer CSV/XLSX, DataFrame, selección, agregación, exportación).
- matplotlib — creación de gráficos (líneas, barras, pie).
- numpy — importado en main.py (se sugiere uso para operaciones numéricas; revisar main.py para su propósito real).
- Biblioteca estándar de Python — entrada/salida (input/print), funciones matemáticas y utilidades (abs, round, pow, max, min, sum, len, ord, chr).

## Instalación y configuración
1. Clonar el repositorio:
git clone https://github.com/EdwinBalles-T/Diplomado.git
2. Crear y activar un entorno virtual (recomendado):
python -m venv venv
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate
3. Instalar dependencias mínimas:
pip install pandas matplotlib numpy
Instale otras librerías según los scripts que vaya a ejecutar (ver imports en los archivos).
4. Verifique que los archivos de datos (tips.csv, ventas_limpio.xlsx) estén en la misma carpeta desde donde se ejecutan los scripts que los leen, o ajuste rutas en los scripts.
## Ejecución
- Ejecutar la calculadora:
* python calculadora.py
* El programa pedirá seleccionar una opción por número y solicitará los números necesarios (input por consola).
- Ejecutar ejemplos pandas:
* python PANDAS/primerPandas.py
* python Clase2/Taller1.py
* python Clase2/clase2.py
- Visualización (si matplotlib está instalado):
* python Clase2/grafico.py
- Carga de datos con pandas (ejemplo interactivo):
Python
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.head())

## Ejemplos de uso
- Calculadora:
Al ejecutar python calculadora.py, seleccione "1" para suma, luego ingrese dos valores cuando se le solicite; el programa mostrará el resultado y preguntará si desea continuar.
- Pandas (crear CSV desde DataFrame):
Ejecutar python PANDAS/primerPandas.py creará dataframepython.csv con los datos definidos en el script.

## Conclusiones
Este repositorio ofrece un conjunto de ejercicios y prácticas orientadas a la enseñanza de fundamentos de Python y a la introducción a la manipulación y visualización de datos con pandas y matplotlib. Contiene ejemplos didácticos y un proyecto modular (calculadora) que ilustra cómo dividir funciones en módulos.

## Autor
Repositorio propiedad de: EdwinBalles-T.
