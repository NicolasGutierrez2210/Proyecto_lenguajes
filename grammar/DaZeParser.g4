parser grammar DaZeParser;

options { tokenVocab=DaZeLexer; }

programa
    : sentencia* EOF
    ;

sentencia
    : asignacion
    | pipeline_stmt
    | llamada_stmt
    | graficar_stmt
    | guardar_stmt
    | mostrar_stmt
    | si_stmt
    | funcion_stmt
    | retornar_stmt
    ;

asignacion
    : identificador ASIGNAR expr PUNTO_Y_COMA?
    ;

pipeline_stmt
    : (identificador ASIGNAR)? expr (PIPE operacion_pipeline)+ PUNTO_Y_COMA?
    ;

llamada_stmt
    : identificador LPAREN lista_argumentos? RPAREN PUNTO_Y_COMA?
    ;

graficar_stmt
    : GRAFICAR tipo_grafico LPAREN expr RPAREN LBRACE configuracion_grafico* RBRACE PUNTO_Y_COMA?
    | GRAFICAR tipo_grafico LPAREN expr RPAREN PUNTO_Y_COMA?
    ;

tipo_grafico
    : BARRAS
    | LINEAS
    | HISTOGRAMA
    | DISPERSION
    | CAJA
    ;

configuracion_grafico
    : identificador ASIGNAR expr PUNTO_Y_COMA?
    ;

guardar_stmt
    : GUARDAR LPAREN expr COMA EN ASIGNAR CADENA (COMA argumentos_con_nombre)? RPAREN PUNTO_Y_COMA?
    | GUARDAR LPAREN expr COMA CADENA (COMA argumentos_con_nombre)? RPAREN PUNTO_Y_COMA?
    | GUARDAR expr EN CADENA (COMO identificador)? PUNTO_Y_COMA?
    ;

mostrar_stmt
    : MOSTRAR LPAREN expr RPAREN PUNTO_Y_COMA?
    ;

si_stmt
    : SI LPAREN expr RPAREN LBRACE sentencia* RBRACE (SINO LBRACE sentencia* RBRACE)? PUNTO_Y_COMA?
    ;

funcion_stmt
    : FUNCION identificador LPAREN lista_parametros? RPAREN LBRACE sentencia* RBRACE PUNTO_Y_COMA?
    ;

retornar_stmt
    : RETORNAR expr? PUNTO_Y_COMA?
    ;

lista_parametros
    : identificador (COMA identificador)*
    ;

operacion_pipeline
    : op_seleccionar
    | op_filtrar
    | op_crear
    | op_renombrar
    | op_ordenar
    | op_agrupar
    | op_resumir
    | op_tratar_nulos
    | op_eliminar_duplicados
    | op_limitar
    | op_personalizada
    ;

op_seleccionar
    : SELECCIONAR LPAREN lista_columnas RPAREN
    ;

op_filtrar
    : FILTRAR LPAREN expr RPAREN
    | FILTRAR DONDE expr
    ;

op_crear
    : CREAR LPAREN lista_asignaciones RPAREN
    ;

op_renombrar
    : RENOMBRAR LPAREN lista_asignaciones RPAREN
    ;

op_ordenar
    : ORDENAR LPAREN argumentos_ordenar RPAREN
    ;

op_agrupar
    : AGRUPAR LPAREN argumentos_agrupar RPAREN
    | AGRUPAR POR LBRACK lista_columnas RBRACK
    | AGRUPAR POR lista_columnas
    ;

op_resumir
    : RESUMIR LPAREN lista_resumen RPAREN
    ;

op_tratar_nulos
    : TRATAR_NULOS LPAREN argumentos_con_nombre RPAREN
    ;

op_eliminar_duplicados
    : ELIMINAR_DUPLICADOS LPAREN (argumentos_con_nombre | lista_columnas)? RPAREN
    ;

op_limitar
    : LIMITAR LPAREN ENTERO RPAREN
    ;

op_personalizada
    : identificador LPAREN lista_argumentos? RPAREN
    ;

argumentos_ordenar
    : lista_argumentos
    ;

argumentos_agrupar
    : lista_argumentos
    ;

lista_columnas
    : LBRACK lista_nombres_columna? RBRACK
    | lista_nombres_columna
    ;

lista_nombres_columna
    : nombre_columna (COMA nombre_columna)*
    ;

nombre_columna
    : identificador
    | CADENA
    ;

lista_asignaciones
    : asignacion_par (COMA asignacion_par)*
    ;

asignacion_par
    : identificador ASIGNAR expr
    ;

lista_resumen
    : resumen_par (COMA resumen_par)*
    ;

resumen_par
    : identificador ASIGNAR (funcion_agregacion | expr)
    ;

funcion_agregacion
    : CONTAR LPAREN RPAREN
    | (SUMA | MEDIA | MEDIANA | MINIMO | MAXIMO | DESV_STD) LPAREN (identificador | CADENA) RPAREN
    ;

argumentos_con_nombre
    : argumento_con_nombre (COMA argumento_con_nombre)*
    ;

argumento_con_nombre
    : identificador ASIGNAR expr
    ;

lista_argumentos
    : argumento (COMA argumento)*
    ;

argumento
    : identificador ASIGNAR expr
    | expr
    ;

expr
    : expr POT expr                                         # ExprPotencia
    | (MAS | MENOS | NO) expr                               # ExprUnaria
    | expr (MULT | DIV | MOD) expr                          # ExprMulDivMod
    | expr (MAS | MENOS) expr                               # ExprSumaResta
    | expr (MAYOR | MENOR | MAYOR_IGUAL | MENOR_IGUAL) expr  # ExprRelacional
    | expr (IGUAL_IGUAL | DIFERENTE) expr                   # ExprIgualdad
    | expr Y expr                                           # ExprLogicaY
    | expr O expr                                           # ExprLogicaO
    | CARGAR LPAREN CADENA (COMA argumentos_con_nombre)? RPAREN # ExprCargar
    | identificador LPAREN lista_argumentos? RPAREN         # ExprLlamada
    | LBRACK lista_expr? RBRACK                             # ExprLista
    | LPAREN expr RPAREN                                    # ExprAgrupacion
    | identificador                                         # ExprIdentificador
    | ENTERO                                                # ExprEntero
    | DECIMAL                                               # ExprDecimal
    | CADENA                                                # ExprCadena
    | VERDADERO                                             # ExprVerdadero
    | FALSO                                                 # ExprFalso
    | NULO                                                  # ExprNulo
    ;

lista_expr
    : expr (COMA expr)*
    ;

identificador
    : ID
    | Y
    | O
    | NO
    | POR
    | EN
    | COMO
    | DONDE
    | ASCENDENTE
    | DESCENDENTE
    | MAXIMO
    | MINIMO
    | MEDIA
    | MEDIANA
    | SUMA
    | CONTAR
    | DESV_STD
    | BARRAS
    | LINEAS
    | HISTOGRAMA
    | DISPERSION
    | CAJA
    | GUARDAR
    | CARGAR
    | SELECCIONAR
    | FILTRAR
    | CREAR
    | RENOMBRAR
    | ORDENAR
    | AGRUPAR
    | RESUMIR
    | TRATAR_NULOS
    | ELIMINAR_DUPLICADOS
    | LIMITAR
    | GRAFICAR
    | MOSTRAR
    | RETORNAR
    | FUNCION
    ;
