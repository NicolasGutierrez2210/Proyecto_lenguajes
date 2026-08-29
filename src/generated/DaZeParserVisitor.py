# Generated from grammar/DaZeParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DaZeParser import DaZeParser
else:
    from DaZeParser import DaZeParser

# This class defines a complete generic visitor for a parse tree produced by DaZeParser.

class DaZeParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DaZeParser#programa.
    def visitPrograma(self, ctx:DaZeParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#sentencia.
    def visitSentencia(self, ctx:DaZeParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#asignacion.
    def visitAsignacion(self, ctx:DaZeParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#pipeline_stmt.
    def visitPipeline_stmt(self, ctx:DaZeParser.Pipeline_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#llamada_stmt.
    def visitLlamada_stmt(self, ctx:DaZeParser.Llamada_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#graficar_stmt.
    def visitGraficar_stmt(self, ctx:DaZeParser.Graficar_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#tipo_grafico.
    def visitTipo_grafico(self, ctx:DaZeParser.Tipo_graficoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#configuracion_grafico.
    def visitConfiguracion_grafico(self, ctx:DaZeParser.Configuracion_graficoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#guardar_stmt.
    def visitGuardar_stmt(self, ctx:DaZeParser.Guardar_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#mostrar_stmt.
    def visitMostrar_stmt(self, ctx:DaZeParser.Mostrar_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#si_stmt.
    def visitSi_stmt(self, ctx:DaZeParser.Si_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#funcion_stmt.
    def visitFuncion_stmt(self, ctx:DaZeParser.Funcion_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#retornar_stmt.
    def visitRetornar_stmt(self, ctx:DaZeParser.Retornar_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_parametros.
    def visitLista_parametros(self, ctx:DaZeParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#operacion_pipeline.
    def visitOperacion_pipeline(self, ctx:DaZeParser.Operacion_pipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_seleccionar.
    def visitOp_seleccionar(self, ctx:DaZeParser.Op_seleccionarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_filtrar.
    def visitOp_filtrar(self, ctx:DaZeParser.Op_filtrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_crear.
    def visitOp_crear(self, ctx:DaZeParser.Op_crearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_renombrar.
    def visitOp_renombrar(self, ctx:DaZeParser.Op_renombrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_ordenar.
    def visitOp_ordenar(self, ctx:DaZeParser.Op_ordenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_agrupar.
    def visitOp_agrupar(self, ctx:DaZeParser.Op_agruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_resumir.
    def visitOp_resumir(self, ctx:DaZeParser.Op_resumirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_tratar_nulos.
    def visitOp_tratar_nulos(self, ctx:DaZeParser.Op_tratar_nulosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_eliminar_duplicados.
    def visitOp_eliminar_duplicados(self, ctx:DaZeParser.Op_eliminar_duplicadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_limitar.
    def visitOp_limitar(self, ctx:DaZeParser.Op_limitarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#op_personalizada.
    def visitOp_personalizada(self, ctx:DaZeParser.Op_personalizadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#argumentos_ordenar.
    def visitArgumentos_ordenar(self, ctx:DaZeParser.Argumentos_ordenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#argumentos_agrupar.
    def visitArgumentos_agrupar(self, ctx:DaZeParser.Argumentos_agruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_columnas.
    def visitLista_columnas(self, ctx:DaZeParser.Lista_columnasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_nombres_columna.
    def visitLista_nombres_columna(self, ctx:DaZeParser.Lista_nombres_columnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#nombre_columna.
    def visitNombre_columna(self, ctx:DaZeParser.Nombre_columnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_asignaciones.
    def visitLista_asignaciones(self, ctx:DaZeParser.Lista_asignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#asignacion_par.
    def visitAsignacion_par(self, ctx:DaZeParser.Asignacion_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_resumen.
    def visitLista_resumen(self, ctx:DaZeParser.Lista_resumenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#resumen_par.
    def visitResumen_par(self, ctx:DaZeParser.Resumen_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#funcion_agregacion.
    def visitFuncion_agregacion(self, ctx:DaZeParser.Funcion_agregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#argumentos_con_nombre.
    def visitArgumentos_con_nombre(self, ctx:DaZeParser.Argumentos_con_nombreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#argumento_con_nombre.
    def visitArgumento_con_nombre(self, ctx:DaZeParser.Argumento_con_nombreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_argumentos.
    def visitLista_argumentos(self, ctx:DaZeParser.Lista_argumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#argumento.
    def visitArgumento(self, ctx:DaZeParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprAgrupacion.
    def visitExprAgrupacion(self, ctx:DaZeParser.ExprAgrupacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprEntero.
    def visitExprEntero(self, ctx:DaZeParser.ExprEnteroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprMulDivMod.
    def visitExprMulDivMod(self, ctx:DaZeParser.ExprMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprRelacional.
    def visitExprRelacional(self, ctx:DaZeParser.ExprRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprIgualdad.
    def visitExprIgualdad(self, ctx:DaZeParser.ExprIgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprCadena.
    def visitExprCadena(self, ctx:DaZeParser.ExprCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprIdentificador.
    def visitExprIdentificador(self, ctx:DaZeParser.ExprIdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprPotencia.
    def visitExprPotencia(self, ctx:DaZeParser.ExprPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprUnaria.
    def visitExprUnaria(self, ctx:DaZeParser.ExprUnariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprLogicaY.
    def visitExprLogicaY(self, ctx:DaZeParser.ExprLogicaYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprLlamada.
    def visitExprLlamada(self, ctx:DaZeParser.ExprLlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprLista.
    def visitExprLista(self, ctx:DaZeParser.ExprListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprSumaResta.
    def visitExprSumaResta(self, ctx:DaZeParser.ExprSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprLogicaO.
    def visitExprLogicaO(self, ctx:DaZeParser.ExprLogicaOContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprDecimal.
    def visitExprDecimal(self, ctx:DaZeParser.ExprDecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprFalso.
    def visitExprFalso(self, ctx:DaZeParser.ExprFalsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprCargar.
    def visitExprCargar(self, ctx:DaZeParser.ExprCargarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprVerdadero.
    def visitExprVerdadero(self, ctx:DaZeParser.ExprVerdaderoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#ExprNulo.
    def visitExprNulo(self, ctx:DaZeParser.ExprNuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#lista_expr.
    def visitLista_expr(self, ctx:DaZeParser.Lista_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaZeParser#identificador.
    def visitIdentificador(self, ctx:DaZeParser.IdentificadorContext):
        return self.visitChildren(ctx)



del DaZeParser