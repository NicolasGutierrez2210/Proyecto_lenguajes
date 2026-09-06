# Especificacion del Lenguaje DaZe (.dz) - Sports Analytics DSL

## 1. Delimitacion del Dominio y Casos de Uso

DaZe es un lenguaje de dominio especifico (DSL) disenado para modelar flujos de trabajo reproducibles en analitica deportiva, preparacion de plantillas y generacion de pizarras tacticas[cite: 2, 3]. El lenguaje combina una sintaxis funcional/declarativa basada en pipelines (`|>`) con una estructura en espanol adaptada al ambito tecnico del deporte, facilitando el diseno de transformaciones sin requerir codigo complejo de proposito general[cite: 2, 3].

### Perfil de Usuarios
- Analistas de rendimiento, directores tecnicos y cuerpos tecnicos deportivos.
- Desarrolladores e investigadores que requieran procesar telemetria, estadisticas de jugadores y metricas de partidos de forma compacta y legible.

### Entradas y Salidas
- **Entradas**: Archivos tabulares en formato CSV con metricas de rendimiento deportivo (con soporte de delimitadores y encabezados), literales escalares y expresiones evaluadas[cite: 2].
- **Salidas**: Tablas transformadas y consolidadas exportables a CSV, declaraciones estructuradas de pizarras visuales (barras, lineas, histogramas, dispersion, caja) y proyecciones en consola[cite: 2].

### Restricciones
- El lenguaje no busca ser un sustituto de proposito general para Python, sino un DSL declarativo enfocado en analisis y rendimiento deportivo[cite: 2].
- Toda operacion en un pipeline recibe una plantilla/conjunto de datos y genera una nueva transformacion sin mutacion destructiva de estados anteriores[cite: 2].

---

## 2. Tipos de Datos y Literales

| Tipo | Descripcion | Sintaxis / Ejemplos |
|---|---|---|
| Entero | Valores numericos enteros | `10`, `0`, `-5` |
| Decimal | Valores numericos en punto flotante | `3.1416`, `0.05`, `99.9` |
| Cadena | Texto delimitado por comillas simples o dobles | `"plantilla.csv"`, `'Delantero'` |
| Booleano | Valores logicos | `verdadero`, `falso`, `true`, `false` |
| Nulo | Ausencia de registro o valor faltante | `nulo`, `null` |
| Lista | Coleccion de elementos o columnas | `[dorsal, goles]`, `["A", "B"]` |
| Tabla | Coleccion tabular cargada o derivada | Resultado de `fichar(...)` o `|>` |

---

## 3. Operadores y Precedencia

### Aritmeticos
- Potencia: `^` o `**` (asociatividad a derecha)[cite: 4]
- Unarios: `+`, `-`, `no` / `not` / `!`[cite: 4]
- Multiplicativos: `*`, `/`, `%`[cite: 4]
- Aditivos: `+`, `-`[cite: 4]

### Relacionales
- Comparaciones: `<`, `<=`, `>`, `>=`[cite: 2, 4]
- Igualdad: `==`, `!=`[cite: 2, 4]

### Logicos
- Conjuncion: `y`, `and`, `&&`[cite: 2, 4]
- Disyuncion: `o`, `or`, `||`[cite: 2, 4]
- Negacion: `no`, `not`, `!`[cite: 2, 4]

---

## 4. Catalogo de Instrucciones y Palabras Reservadas

### 4.1. Carga y Guardado de Datos
- **`fichar(ruta, ...)`**: Carga una plantilla desde disco. Permite configurar argumentos con nombre como `separador=","` y `encabezado=verdadero`[cite: 2].
  ```daze
  datos = fichar("datos/plantilla_temporada.csv", separador=",", encabezado=verdadero)
  ```
- **`archivar(dataset, en="ruta", ...)`**: Exporta los resultados o balances a un archivo CSV[cite: 2].
  ```daze
  archivar(resumen, en="salidas/balance_posiciones.csv", separador=";")
  ```

### 4.2. Operaciones de Pipeline (`|>`)
- **`convocar(col1, col2, ...)`**: Proyecta y selecciona un subconjunto de columnas o variables del jugador[cite: 2].
  ```daze
  datos |> convocar(nombre, posicion, minutos, goles)
  ```
- **`descartar(condicion)`**: Filtra registros que cumplan con un criterio condicional booleano[cite: 2].
  ```daze
  datos |> descartar(minutos > 0 y goles >= 0)
  ```
- **`contratar(nueva_col = expr, ...)`**: Agrega o calcula nuevas metricas deportivas sobre la plantilla.
  ```daze
  datos |> contratar(rendimiento_total = (goles * 1.5) + (minutos / 100))
  ```
- **`rebautizar(col_antigua = nueva_col, ...)`**: Renombra atributos o metricas del dataset.
  ```daze
  datos |> rebautizar(antiguo_id = "dorsal")
  ```
- **`clasificar(por=[col1], descendente=verdadero)`**: Ordena las filas en funcion del rendimiento de forma ascendente o descendente[cite: 2].
  ```daze
  datos |> clasificar(por=[rendimiento_total], descendente=verdadero)
  ```
- **`alinear(por=[col1, col2])`**: Define los grupos tacticos para calculos posteriores (ej. agrupar por posicion o club)[cite: 2].
  ```daze
  datos |> alinear(por=[posicion])
  ```
- **`balance(alias = func(col), ...)`**: Ejecuta calculos agregados y resumenes descriptivos sobre la agrupacion[cite: 2].
  - Funciones disponibles: `contar()`, `suma(col)`, `media(col)`, `mediana(col)`, `minimo(col)`, `maximo(col)`, `desv_std(col)`[cite: 2].
  ```daze
  datos |> balance(goles_totales = suma(goles), total_convocados = contar(), promedio = media(minutos))
  ```
- **`reemplazar_bajas(accion="eliminar" | "rellenar", valor=...)`**: Tratamiento de datos nulos o bajas medicas en la plantilla[cite: 2].
  ```daze
  datos |> reemplazar_bajas(accion="rellenar", valor=0.0)
  ```
- **`depurar_plantilla(...)`**: Remueve registros duplicados o redundantes de jugadores[cite: 2].
  ```daze
  datos |> depurar_plantilla(columnas=[dorsal])
  ```
- **`top(n)`**: Conserva los primeros `n` registros destacados del pipeline.
  ```daze
  datos |> top(11)
  ```

### 4.3. Declaracion de Visualizaciones
- **`pizarra tipo(dataset) { configuraciones }`**:
  Tipos admitidos: `barras`, `lineas`, `histograma`, `dispersion`, `caja`[cite: 2].
  Propiedades comunes: `eje_x`, `eje_y`, `titulo`, `color`, `guardar`, `proyectar`.
  ```daze
  pizarra barras(resumen_posiciones) {
      eje_x = posicion
      eje_y = goles_totales
      titulo = "Goles por Posicion"
      guardar = "salidas/pizarra_goles.png"
  }
  ```

### 4.4. Estructuras de Control y Modularidad
- **`tactica nombre(p1, p2) { ... resultado expr; }`**: Declaracion de subrutinas o formulas reutilizables[cite: 2].
- **`si (condicion) { ... } sino { ... }`**: Estructura de bifurcacion condicional[cite: 2].
- **`proyectar(expr)`**: Salida informativa en consola.
