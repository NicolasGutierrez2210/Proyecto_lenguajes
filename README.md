# DaZe: Sports Analytics DSL (Lenguaje de Dominio Específico)

DaZe (`.dz`) es un lenguaje de dominio específico diseñado para estructurar flujos reproducibles de análisis de datos deportivos, preparación tabular de plantillas y generación de pizarras gráficas[cite: 3]. El objetivo del lenguaje es ofrecer una sintaxis clara, directa y formal basada en el ámbito de la analítica deportiva, apoyada en el encadenamiento de operaciones mediante pipelines (`|>`), permitiendo expresar transformaciones de datos sin requerir código complejo de propósito general[cite: 3].

El proyecto implementa la definición formal, el analizador léxico, el analizador sintáctico y las herramientas de validación y visualización del árbol de análisis sintáctico, utilizando ANTLR4 y Python 3.11+[cite: 3, 4].

---

## Estructura del Proyecto

La organización modular del repositorio se divide de la siguiente manera[cite: 1]:

```text
proyecto_lenguajes/
|-- grammar/
|   |-- DaZeLexer.g4          # Definición léxica: palabras reservadas deportivas, símbolos y operadores
|   |-- DaZeParser.g4         # Definición sintáctica: sentencias, expresiones, pipelines y pizarras
|-- src/
|   |-- __init__.py           # Funciones de alto nivel para tokenización y análisis
|   |-- cli.py                # Interfaz de línea de comandos para validar y mostrar árboles
|   |-- errors.py             # Manejador y listener personalizado de errores léxicos y sintácticos
|   |-- tree_viewer.py        # Visualizador en texto del árbol de derivación sintáctica (CST/AST)
|   |-- generated/            # Código Python generado automáticamente por ANTLR4
|       |-- DaZeLexer.py
|       |-- DaZeParser.py
|       |-- DaZeParserVisitor.py
|       |-- DaZeParserListener.py
|-- docs/
|   |-- especificacion_lenguaje.md  # Catálogo de instrucciones, operadores y reglas del lenguaje
|   |-- gramatica_ebnf.md          # Especificación formal en notación EBNF
|-- examples/
|   |-- correcto_ventas.dz         # Flujo de análisis de rendimiento de jugadores y fichajes
|   |-- correcto_estudiantes.dz    # Ejemplo de procesamiento de datos
|   |-- correcto_sensores.dz       # Ejemplo de métricas de monitoreo
|   |-- incorrecto_sintaxis.dz     # Caso de prueba con errores sintácticos intencionales
|   |-- incorrecto_lexico.dz       # Caso de prueba con errores léxicos intencionales
|-- tests/
|   |-- test_lexer.py         # Pruebas unitarias para tokens, comentarios y literales
|   |-- test_parser.py        # Pruebas sintácticas de sentencias, pipelines y gráficas
|   |-- test_errors.py        # Pruebas de captura de errores y diagnóstico
|-- requirements.txt          # Dependencias necesarias para ejecutar el proyecto
|-- .gitignore                # Archivos y directorios excluidos del control de versiones
|-- README.md                 # Documentación principal del proyecto
```

---

## Características del Lenguaje DaZe

### 1. Carga y Exportación de Conjuntos de Datos
Permite leer y escribir archivos CSV asociando los datos a variables y configurando delimitadores o encabezados[cite: 3]:
```daze
datos = fichar("datos/plantilla_temporada.csv", separador=",", encabezado=verdadero)
archivar(resumen, en="salidas/resumen_posiciones.csv", separador=",")
```

### 2. Pipelines de Transformación (`|>`)
Las operaciones se encadenan de forma secuencial, recibiendo un dataset y produciendo uno nuevo[cite: 3]:
- `convocar(...)`: Proyección y selección de columnas[cite: 3].
- `descartar(...)`: Filtrado de filas mediante expresiones booleanas[cite: 3].
- `contratar(...)`: Creación o modificación de columnas calculadas[cite: 3].
- `rebautizar(...)`: Cambio de nombres de variables[cite: 3].
- `clasificar(...)`: Ordenamiento ascendente o descendente[cite: 3].
- `alinear(...)`: Definición de variables de agrupación[cite: 3].
- `balance(...)`: Agregaciones descriptivas (`suma`, `media`, `mediana`, `minimo`, `maximo`, `desv_std`, `contar`)[cite: 3].
- `reemplazar_bajas(...)`: Imputación o descarte de datos faltantes[cite: 3].
- `depurar_plantilla(...)`: Limpieza de registros redundantes[cite: 3].
- `top(...)`: Selección de un número determinado de filas[cite: 3].

Ejemplo:
```daze
jugadores_aptos = jugadores
    |> convocar(dorsal, club, posicion, minutos, goles, asistencias)
    |> descartar(minutos > 0 y goles >= 0)
    |> contratar(rendimiento_total = (goles * 1.5) + (minutos / 100))
    |> alinear(por=[posicion])
    |> balance(goles_totales = suma(goles), total_convocados = contar())
```

### 3. Expresiones y Operadores
- Aritmética: Suma (`+`), resta (`-`), multiplicación (`*`), división (`/`), módulo (`%`), potencia (`^` o `**`)[cite: 3].
- Comparación: `==`, `!=`, `<`, `<=`, `>`, `>=`[cite: 3].
- Lógica: `y` (`and`), `o` (`or`), `no` (`not`)[cite: 3].
- Literales: Enteros, decimales, cadenas (comillas simples o dobles), booleanos (`verdadero`/`falso`) y nulos (`nulo`)[cite: 3].

### 4. Declaración de Visualizaciones
Sintaxis para especificar representaciones visuales y pizarras tácticas[cite: 3]:
```daze
pizarra barras(resumen_posiciones) {
    eje_x = posicion
    eje_y = goles_totales
    titulo = "Goles Totales por Posicion"
    guardar = "salidas/goles_por_posicion.png"
}
```

### 5. Estructuras de Control y Funciones
```daze
tactica calcular_bono(salario, porcentaje) {
    resultado salario * (porcentaje / 100);
}

si (goles_totales > 50) {
    proyectar("Meta alcanzada");
} sino {
    proyectar("Meta pendiente");
}
```

---

## Manejo de Errores y Diagnóstico

El módulo `src/errors.py` implementa `DaZeErrorListener`, el cual sustituye el listener por defecto de ANTLR[cite: 1, 3, 4]. Este componente intercepta los errores durante las etapas léxica y sintáctica, reportando mensajes claros en español con la siguiente información[cite: 3]:
- Tipo de error (Léxico o Sintáctico)[cite: 3].
- Número de línea y columna exacta[cite: 3, 4].
- Símbolo o token causante del problema[cite: 3, 4].
- Mensaje descriptivo con el elemento esperado[cite: 3, 4].

---

## Guía de Ejecución en Linux

A continuación se describen los pasos necesarios para preparar el entorno, compilar la gramática y ejecutar las pruebas o el analizador desde la terminal en sistemas operativos basados en Linux (Ubuntu, Debian, Fedora, Arch, instancias EC2 de AWS, etc.)[cite: 3].

### 1. Requisitos Previos
Asegurarse de tener instalados Python 3.11 o superior, pip y una versión reciente de Java (JRE/JDK 11+ para compilar gramáticas ANTLR)[cite: 3]:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv openjdk-17-jre -y
```

### 2. Clonar o Acceder al Directorio del Proyecto
```bash
cd proyecto_lenguajes
```

### 3. Crear y Activar un Entorno Virtual
Es una buena práctica aislar las dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias
Instalar el runtime de ANTLR4 y las bibliotecas del proyecto[cite: 1, 3]:
```bash
pip install -r requirements.txt
```

### 5. Generación de Archivos ANTLR4 (Opcional)
Los archivos generados ya se encuentran incluidos en `src/generated/`[cite: 1, 3]. No obstante, si se realizan modificaciones en `grammar/DaZeLexer.g4` o `grammar/DaZeParser.g4`, se pueden regenerar ejecutando[cite: 1, 3]:

```bash
cd grammar
antlr4 -Dlanguage=Python3 DaZeLexer.g4
antlr4 -Dlanguage=Python3 -visitor DaZeParser.g4
mv DaZe* ../src/generated/
rm -f ../src/generated/*.g4
cd ..
```

### 6. Ejecución de la Batería de Pruebas
Para correr todas las pruebas unitarias (léxicas, sintácticas y de errores)[cite: 1, 3]:
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### 7. Uso de la Herramienta CLI

Para validar la sintaxis de un archivo DaZe[cite: 1, 3]:
```bash
python3 src/cli.py --check examples/correcto_ventas.dz
```

Para inspeccionar la secuencia de tokens reconocidos por el lexer[cite: 1, 3]:
```bash
python3 src/cli.py --tokens examples/correcto_ventas.dz
```

Para visualizar el árbol de derivación sintáctica completo en formato jerárquico[cite: 1, 3]:
```bash
python3 src/cli.py --tree examples/correcto_ventas.dz
```

Para probar el reporte de errores en un archivo con errores intencionales[cite: 1, 3]:
```bash
python3 src/cli.py examples/incorrecto_sintaxis.dz
python3 src/cli.py examples/incorrecto_lexico.dz
```
