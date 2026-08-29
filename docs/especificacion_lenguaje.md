# Especificacion del Lenguaje DaZe (.dz)

## 1. Delimitacion del Dominio y Casos de Uso

DaZe es un lenguaje de dominio especifico (DSL) disenado para modelar flujos de trabajo reproducibles en ciencia de datos, preparacion tabular y visualizacion descriptiva. El lenguaje combina una sintaxis funcional/declarativa basada en pipelines (`|>`) con una estructura en espanol que facilita la lectura y el diseno de pipelines de transformacion.

### Perfil de Usuarios
- Estudiantes e investigadores en analitica y ciencia de datos.
- Desarrolladores que requieran describir pipelines de ETL y resumenes estadisticos de forma compacta y legible.

### Entradas y Salidas
- **Entradas**: Archivos tabulares en formato CSV (con soporte de delimitadores personalizados y encabezados), literales escalares y expresiones calculadas.
- **Salidas**: Tablas transformadas exportables a archivos CSV, declaraciones estructuradas de visualizacion (barras, lineas, histogramas, dispersion, caja) y mensajes en consola.

### Restricciones
- El lenguaje no busca ser un sustituto de proposito general para Python, sino un DSL declarativo enfocado en transformacion de datos tabulares.
- Toda operacion en un pipeline recibe un conjunto de datos y genera una nueva transformacion sin mutacion silenciosa de estados anteriores.

---

## 2. Tipos de Datos y Literales

| Tipo | Descripcion | Sintaxis / Ejemplos |
|---|---|---|
| Entero | Valores numericos enteros | `10`, `0`, `-5` |
| Decimal | Valores numericos en punto flotante | `3.1416`, `0.05`, `99.9` |
| Cadena | Texto delimitado por comillas simples o dobles | `"ventas.csv"`, `'Alta'` |
| Booleano | Valores logicos | `verdadero`, `falso`, `true`, `false` |
| Nulo | Ausencia de valor o valor faltante | `nulo`, `null` |
| Lista | Coleccion de elementos o columnas | `[col1, col2]`, `["A", "B"]` |
| Tabla | Coleccion tabular cargada o derivada | Resultado de `cargar(...)` o `|>` |

---

## 3. Operadores y Precedencia

### Aritmeticos
- Potencia: `^` o `**` (asociatividad a derecha)
- Unarios: `+`, `-`, `no` / `not` / `!`
- Multiplicativos: `*`, `/`, `%`
- Aditivos: `+`, `-`

### Relacionales
- Comparaciones: `<`, `<=`, `>`, `>=`
- Igualdad: `==`, `!=`

### Logicos
- Conjuncion: `y`, `and`, `&&`
- Disyuncion: `o`, `or`, `||`
- Negacion: `no`, `not`, `!`

---

## 4. Catalogo de Instrucciones y Palabras Reservadas

### 4.1. Carga y Guardado de Datos
- **`cargar(ruta, ...)`**: Carga un dataset desde disco. Permite configurar argumentos con nombre como `separador=","` y `encabezado=verdadero`.
  ```daze
  datos = cargar("datos/ventas.csv", separador=",", encabezado=verdadero)
  ```
- **`guardar(dataset, en="ruta", ...)`**: Exporta un dataset a un archivo CSV.
  ```daze
  guardar(resumen, en="salidas/reporte.csv", separador=";")
  ```

### 4.2. Operaciones de Pipeline (`|>`)
- **`seleccionar(col1, col2, ...)`**: Filtra y proyecta un subconjunto de columnas.
  ```daze
  datos |> seleccionar(fecha, ciudad, total)
  ```
- **`filtrar(condicion)`**: Filtra registros que cumplan la condicion booleana.
  ```daze
  datos |> filtrar(total > 100 y estado == "activo")
  ```
- **`crear(nueva_col = expr, ...)`**: Agrega o actualiza columnas calculadas.
  ```daze
  datos |> crear(total_iva = subtotal * 1.19, margen = utilidad / total)
  ```
- **`renombrar(col_antigua = nueva_col, ...)`**: Renombra variables del dataset.
  ```daze
  datos |> renombrar(antiguo_id = "codigo_estudiante")
  ```
- **`ordenar(por=[col1], descendente=verdadero)`**: Ordena el dataset de manera ascendente o descendente.
  ```daze
  datos |> ordenar(por=[total_iva], descendente=verdadero)
  ```
- **`agrupar(por=[col1, col2])`**: Define las claves de agrupamiento para calculos agregados posteriores.
  ```daze
  datos |> agrupar(por=[categoria, ciudad])
  ```
- **`resumir(alias = func(col), ...)`**: Ejecuta calculos agregados sobre las columnas agrupadas.
  - Funciones disponibles: `contar()`, `suma(col)`, `media(col)`, `mediana(col)`, `minimo(col)`, `maximo(col)`, `desv_std(col)`.
  ```daze
  datos |> resumir(ingreso = suma(total), cantidad = contar(), promedio = media(precio))
  ```
- **`tratar_nulos(accion="eliminar" | "rellenar", valor=...)`**: Tratamiento de valores faltantes.
  ```daze
  datos |> tratar_nulos(accion="rellenar", valor=0.0)
  ```
- **`eliminar_duplicados(...)`**: Remueve filas redundantes.
  ```daze
  datos |> eliminar_duplicados(columnas=[id_usuario])
  ```
- **`limitar(n)`**: Conserva las primeras `n` filas.
  ```daze
  datos |> limitar(10)
  ```

### 4.3. Declaracion de Visualizaciones
- **`graficar tipo(dataset) { configuraciones }`**:
  Tipos admitidos: `barras`, `lineas`, `histograma`, `dispersion`, `caja`.
  Propiedades comunes: `eje_x`, `eje_y`, `titulo`, `color`, `guardar`, `mostrar`.
  ```daze
  graficar barras(resumen_ventas) {
      eje_x = ciudad
      eje_y = ingreso
      titulo = "Ventas por Ciudad"
      guardar = "salidas/grafico_ventas.png"
  }
  ```

### 4.4. Estructuras de Control y Modularidad
- **`funcion nombre(p1, p2) { ... retornar expr; }`**: Declaracion de subrutinas y calculos reutilizables.
- **`si (condicion) { ... } sino { ... }`**: Bifurcacion condicional.
- **`mostrar(expr)`**: Impresion informativa en la consola de salida.
