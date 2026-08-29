# Gramatica EBNF de DaZe

A continuacion se presenta la especificacion sintactica formal de DaZe en formato EBNF (Extended Backus-Naur Form).

```ebnf
programa            ::= { sentencia } EOF ;

sentencia           ::= asignacion
                      | pipeline_stmt
                      | llamada_stmt
                      | graficar_stmt
                      | guardar_stmt
                      | mostrar_stmt
                      | si_stmt
                      | funcion_stmt
                      | retornar_stmt ;

asignacion          ::= identificador '=' expr [ ';' ] ;

pipeline_stmt       ::= [ identificador '=' ] expr { '|>' operacion_pipeline }+ [ ';' ] ;

llamada_stmt        ::= identificador '(' [ lista_argumentos ] ')' [ ';' ] ;

graficar_stmt       ::= 'graficar' tipo_grafico '(' expr ')' '{' { configuracion_grafico } '}' [ ';' ]
                      | 'graficar' tipo_grafico '(' expr ')' [ ';' ] ;

tipo_grafico        ::= 'barras' | 'lineas' | 'histograma' | 'dispersion' | 'caja' ;

configuracion_grafico ::= identificador '=' expr [ ';' ] ;

guardar_stmt        ::= 'guardar' '(' expr ',' 'en' '=' CADENA [ ',' argumentos_con_nombre ] ')' [ ';' ]
                      | 'guardar' '(' expr ',' CADENA [ ',' argumentos_con_nombre ] ')' [ ';' ]
                      | 'guardar' expr 'en' CADENA [ 'como' identificador ] [ ';' ] ;

mostrar_stmt        ::= 'mostrar' '(' expr ')' [ ';' ] ;

si_stmt             ::= 'si' '(' expr ')' '{' { sentencia } '}' [ 'sino' '{' { sentencia } '}' ] [ ';' ] ;

funcion_stmt        ::= 'funcion' identificador '(' [ lista_parametros ] ')' '{' { sentencia } '}' [ ';' ] ;

retornar_stmt       ::= 'retornar' [ expr ] [ ';' ] ;

lista_parametros    ::= identificador { ',' identificador } ;

operacion_pipeline  ::= op_seleccionar
                      | op_filtrar
                      | op_crear
                      | op_renombrar
                      | op_ordenar
                      | op_agrupar
                      | op_resumir
                      | op_tratar_nulos
                      | op_eliminar_duplicados
                      | op_limitar
                      | op_personalizada ;

op_seleccionar      ::= 'seleccionar' '(' lista_columnas ')' ;
op_filtrar          ::= 'filtrar' '(' expr ')' | 'filtrar' 'donde' expr ;
op_crear            ::= 'crear' '(' lista_asignaciones ')' ;
op_renombrar        ::= 'renombrar' '(' lista_asignaciones ')' ;
op_ordenar          ::= 'ordenar' '(' argumentos_ordenar ')' ;
op_agrupar          ::= 'agrupar' '(' argumentos_agrupar ')' | 'agrupar' 'por' [ '[' ] lista_columnas [ ']' ] ;
op_resumir          ::= 'resumir' '(' lista_resumen ')' ;
op_tratar_nulos     ::= 'tratar_nulos' '(' argumentos_con_nombre ')' ;
op_eliminar_duplicados ::= 'eliminar_duplicados' '(' [ argumentos_con_nombre | lista_columnas ] ')' ;
op_limitar          ::= 'limitar' '(' ENTERO ')' ;
op_personalizada    ::= identificador '(' [ lista_argumentos ] ')' ;

argumentos_ordenar  ::= lista_argumentos ;
argumentos_agrupar  ::= lista_argumentos ;

lista_columnas      ::= '[' [ lista_nombres_columna ] ']' | lista_nombres_columna ;
lista_nombres_columna ::= nombre_columna { ',' nombre_columna } ;
nombre_columna      ::= identificador | CADENA ;

lista_asignaciones  ::= asignacion_par { ',' asignacion_par } ;
asignacion_par      ::= identificador '=' expr ;

lista_resumen       ::= resumen_par { ',' resumen_par } ;
resumen_par         ::= identificador '=' ( funcion_agregacion | expr ) ;

funcion_agregacion  ::= ( 'contar' | 'conteo' ) '(' ')'
                      | ( 'suma' | 'media' | 'promedio' | 'mediana' | 'minimo' | 'min' | 'maximo' | 'max' | 'desv_std' | 'desviacion' ) '(' ( identificador | CADENA ) ')' ;

argumentos_con_nombre ::= argumento_con_nombre { ',' argumento_con_nombre } ;
argumento_con_nombre  ::= identificador '=' expr ;

lista_argumentos    ::= argumento { ',' argumento } ;
argumento           ::= identificador '=' expr | expr ;

expr                ::= expr ( '^' | '**' ) expr
                      | ( '+' | '-' | 'no' | 'not' | '!' ) expr
                      | expr ( '*' | '/' | '%' ) expr
                      | expr ( '+' | '-' ) expr
                      | expr ( '>' | '<' | '>=' | '<=' ) expr
                      | expr ( '==' | '!=' ) expr
                      | expr ( 'y' | 'and' | '&&' ) expr
                      | expr ( 'o' | 'or' | '||' ) expr
                      | 'cargar' '(' CADENA [ ',' argumentos_con_nombre ] ')'
                      | identificador '(' [ lista_argumentos ] ')'
                      | '[' [ lista_expr ] ']'
                      | '(' expr ')'
                      | identificador
                      | ENTERO
                      | DECIMAL
                      | CADENA
                      | ( 'verdadero' | 'true' )
                      | ( 'falso' | 'false' )
                      | ( 'nulo' | 'null' ) ;

lista_expr          ::= expr { ',' expr } ;

identificador       ::= ID | PALABRA_CLAVE_PERMITIDA ;
```
