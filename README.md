# DaZe: Lenguaje de Dominio Especifico para Ciencia de Datos y Visualizacion

DaZe (`.dz`) es un lenguaje de dominio especifico disenado para estructurar flujos reproducibles de analisis de datos, preparacion tabular y generacion de graficos. El objetivo del lenguaje es ofrecer una sintaxis clara, directa y en espanol, apoyada en el encadenamiento de operaciones mediante pipelines (`|>`), permitiendo expresar transformaciones de datos sin requerir codigo complejo de proposito general.

El proyecto implementa la definicion formal, el analizador lexico, el analizador sintactico y las herramientas de validacion y visualizacion del arbol de analisis sintactico, utilizando ANTLR4 y Python 3.11+.

---

## Estructura del Proyecto

La organizacion modular del repositorio se divide de la siguiente manera:

```text
proyecto_lenguajes/
|-- grammar/
|   |-- DaZeLexer.g4          # Definicion lexica: palabras reservadas, simbolos, operadores y literales
|   |-- DaZeParser.g4         # Definicion sintactica: sentencias, expresiones, pipelines y graficos
|-- src/
|   |-- __init__.py           # Funciones de alto nivel para tokenizacion y analisis
|   |-- cli.py                # Interfaz de linea de comandos para validar y mostrar arboles
|   |-- errors.py             # Manejador y listener personalizado de errores lexicos y sintacticos
|   |-- tree_viewer.py        # Visualizador en texto del arbol de derivacion sintactica (CST/AST)
|   |-- generated/            # Codigo Python generado automaticamente por ANTLR4
|       |-- DaZeLexer.py
|       |-- DaZeParser.py
|       |-- DaZeParserVisitor.py
|       |-- DaZeParserListener.py
|-- docs/
|   |-- especificacion_lenguaje.md  # Catalogo de instrucciones, operadores y reglas del lenguaje
|   |-- gramatica_ebnf.md          # Especificacion formal en notacion EBNF
|-- examples/
|   |-- correcto_ventas.dz        # Ejemplo de flujo de analisis comercial y ventas
|   |-- correcto_estudiantes.dz   # Ejemplo de procesamiento de notas academicas
|   |-- correcto_sensores.dz      # Ejemplo de monitoreo IoT y funciones
|   |-- incorrecto_sintaxis.dz    # Caso de prueba con errores sintacticos intencionales
|   |-- incorrecto_lexico.dz      # Caso de prueba con errores lexicos intencionales
|-- tests/
|   |-- test_lexer.py         # Pruebas unitarias para tokens, comentarios y literales
|   |-- test_parser.py        # Pruebas sintacticas de sentencias, pipelines y graficos
|   |-- test_errors.py        # Pruebas de captura de errores y diagnostico
|-- requirements.txt          # Dependencias necesarias para ejecutar el proyecto
|-- .gitignore                # Archivos y directorios excluidos del control de versiones
|-- README.md                 # Documentacion principal del proyecto
```

---

## Caracteristicas del Lenguaje DaZe

### 1. Carga y Exportacion de Conjuntos de Datos
Permite leer y escribir archivos CSV asociando los datos a variables y configurando delimitadores o encabezados:
```daze
datos = cargar("datos/ventas.csv", separador=",", encabezado=verdadero)
guardar(resumen, en="salidas/resumen.csv", separador=",")
```

### 2. Pipelines de Transformacion (`|>`)
Las operaciones se encadenan de forma secuencial, recibiendo un dataset y produciendo uno nuevo:
- `seleccionar(...)`: Proyeccion de columnas.
- `filtrar(...)`: Filtrado mediante expresiones booleanas.
- `crear(...)`: Creacion o modificacion de columnas calculadas.
- `renombrar(...)`: Cambio de nombres de variables.
- `ordenar(...)`: Ordenamiento ascendente o descendente.
- `agrupar(...)`: Definicion de variables de agrupacion.
- `resumir(...)`: Agregaciones descriptivas (`suma`, `media`, `mediana`, `minimo`, `maximo`, `desv_std`, `contar`).
- `tratar_nulos(...)`: Imputacion o descarte de datos faltantes.
- `eliminar_duplicados(...)`: Limpieza de registros redundantes.
- `limitar(...)`: Seleccion de un numero determinado de filas.

Ejemplo:
```daze
ventas_limpias = ventas
    |> seleccionar(fecha, ciudad, unidades, precio)
    |> filtrar(unidades > 0 y precio > 0)
    |> crear(total = unidades * precio)
    |> agrupar(por=[ciudad])
    |> resumir(ingreso_total = suma(total), transacciones = contar())
```

### 3. Expresiones y Operadores
- Aritmetica: Suma (`+`), resta (`-`), multiplicacion (`*`), division (`/`), modulo (`%`), potencia (`^` o `**`).
- Comparacion: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Logica: `y` (`and`), `o` (`or`), `no` (`not`).
- Literales: Enteros, decimales, cadenas (comillas simples o dobles), booleanos (`verdadero`/`falso`) y nulos (`nulo`).

### 4. Declaracion de Visualizaciones
Sintaxis para especificar representaciones visuales:
```daze
graficar barras(resumen) {
    eje_x = ciudad
    eje_y = ingreso_total
    titulo = "Ingresos por Ciudad"
    guardar = "salidas/grafica_ingresos.png"
}
```

### 5. Estructuras de Control y Funciones
```daze
funcion calcular_bono(salario, porcentaje) {
    retornar salario * (porcentaje / 100);
}

si (total > 5000) {
    mostrar("Meta alcanzada");
} sino {
    mostrar("Meta pendiente");
}
```

---

## Manejo de Errores y Diagnostico

El modulo `src/errors.py` implementa `DaZeErrorListener`, el cual sustituye el listener por defecto de ANTLR. Este componente intercepta los errores durante las etapas lexica y sintactica, reportando mensajes claros en espanol con la siguiente informacion:
- Tipo de error (Lexico o Sintactico).
- Numero de linea y columna exacta.
- Simbolo o token causante del problema.
- Mensaje descriptivo con el elemento esperado.

---

## Guia de Ejecucion en Linux

A continuacion se describen los pasos necesarios para preparar el entorno, compilar la gramatica y ejecutar las pruebas o el analizador desde la terminal en sistemas operativos basados en Linux (Ubuntu, Debian, Fedora, Arch, etc.).

### 1. Requisitos Previos
Asegurarse de tener instalados Python 3.11 o superior, pip y una version reciente de Java (JRE/JDK 11+ para compilar gramaticas ANTLR):

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv openjdk-17-jre -y
```

### 2. Clonar o Acceder al Directorio del Proyecto
```bash
cd proyecto_lenguajes
```

### 3. Crear y Activar un Entorno Virtual
Es una buena practica aislar las dependencias:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias
Instalar el runtime de ANTLR4 y las bibliotecas del proyecto:
```bash
pip install -r requirements.txt
```

### 5. Generacion de Archivos ANTLR4 (Opcional)
Los archivos generados ya se encuentran incluidos en `src/generated/`. No obstante, si se realizan modificaciones en `grammar/DaZeLexer.g4` o `grammar/DaZeParser.g4`, se pueden regenerar ejecutando:

```bash
# Descargar el jar de ANTLR si no se tiene localmente
wget https://www.antlr.org/download/antlr-4.13.2-complete.jar

# Generar el lexer, parser, listener y visitor en Python
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener -o src/generated grammar/DaZeLexer.g4 grammar/DaZeParser.g4
```

### 6. Ejecucion de la Bateria de Pruebas
Para correr todas las pruebas unitarias (lexicas, sintacticas y de errores):
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

### 7. Uso de la Herramienta CLI

Para validar la sintaxis de un archivo DaZe:
```bash
python3 src/cli.py examples/correcto_ventas.dz --check
```

Para inspeccionar la secuencia de tokens reconocidos por el lexer:
```bash
python3 src/cli.py examples/correcto_ventas.dz --tokens
```

Para visualizar el arbol de derivacion sintactica completo en formato jerarquico:
```bash
python3 src/cli.py examples/correcto_ventas.dz --tree
```

Para probar el reporte de errores en un archivo con errores intencionales:
```bash
python3 src/cli.py examples/incorrecto_sintaxis.dz
python3 src/cli.py examples/incorrecto_lexico.dz
```
