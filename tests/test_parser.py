import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import parse_code, parse_file

class TestDaZeParser(unittest.TestCase):

    def test_asignacion_y_expresiones(self):
        codigos = [
            "x = 42;",
            "y = 3.14159",
            "nombre = 'Jugador'",
            "apto = verdadero",
            "calculo = (10 + 5) * 2 ^ 3 - 4 / 2",
            "condicion = (a > 10) y (b <= 5) o no (c == 0)",
        ]
        for codigo in codigos:
            with self.subTest(codigo=codigo):
                tree, parser, errors = parse_code(codigo)
                self.assertEqual(len(errors), 0, f"Error al parsear: {codigo} -> {errors}")
                self.assertIsNotNone(tree)

    def test_carga_datos(self):
        codigos = [
            'datos = fichar("ruta/archivo.csv")',
            'datos = fichar("ruta/archivo.csv", separador=",", encabezado=verdadero)',
            'datos = fichar("ruta/archivo.csv", separador=";", encoding="utf-8")',
        ]
        for codigo in codigos:
            with self.subTest(codigo=codigo):
                tree, parser, errors = parse_code(codigo)
                self.assertEqual(len(errors), 0, f"Error al parsear: {codigo} -> {errors}")

    def test_pipeline_operaciones(self):
        codigo = """
        resultado = dataset
            |> convocar(col1, col2, col3)
            |> descartar(col1 > 100 y col2 != "lesionado")
            |> contratar(total = col1 * 1.19, flag = verdadero)
            |> rebautizar(col1 = "primera_columna")
            |> clasificar(por=[total], descendente=verdadero)
            |> alinear(por=[col2])
            |> balance(
                total_suma = suma(total),
                promedio = media(col1),
                mediana_val = mediana(col1),
                desviacion = desv_std(col1),
                conteo_filas = contar()
            )
            |> reemplazar_bajas(accion="rellenar", valor=0)
            |> depurar_plantilla()
            |> top(50)
        """
        tree, parser, errors = parse_code(codigo)
        self.assertEqual(len(errors), 0, f"Errores en pipeline: {errors}")

    def test_sentencias_graficar(self):
        codigos = [
            'pizarra barras(df) { eje_x = categoria; eje_y = total; titulo = "Mi Grafica"; }',
            'pizarra lineas(df) { eje_x = fecha; eje_y = valor; guardar = "salida.png"; }',
            'pizarra histograma(df) { eje_x = edad; }',
            'pizarra dispersion(df) { eje_x = x; eje_y = y; }',
            'pizarra caja(df) { eje_x = grupo; eje_y = puntaje; }',
            'pizarra barras(df)',
        ]
        for codigo in codigos:
            with self.subTest(codigo=codigo):
                tree, parser, errors = parse_code(codigo)
                self.assertEqual(len(errors), 0, f"Error al parsear grafico: {codigo} -> {errors}")

    def test_estructuras_control_y_funciones(self):
        codigo = """
        tactica normalizar(valor, maximo) {
            resultado valor / maximo;
        }

        si (total > 1000) {
            categoria = "Alto";
            proyectar("Rendimiento: Alto");
        } sino {
            categoria = "Normal";
            proyectar("Rendimiento: Normal");
        }
        """
        tree, parser, errors = parse_code(codigo)
        self.assertEqual(len(errors), 0, f"Errores en funciones/condicionales: {errors}")

    def test_ejemplos_completos(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "examples"))
        archivos_correctos = [
            "correcto_ventas.dz",
            "correcto_estudiantes.dz",
            "correcto_sensores.dz",
        ]
        for archivo in archivos_correctos:
            ruta = os.path.join(base_dir, archivo)
            with self.subTest(archivo=archivo):
                tree, parser, errors = parse_file(ruta)
                self.assertEqual(len(errors), 0, f"Errores en archivo {archivo}: {errors}")

if __name__ == "__main__":
    unittest.main()
