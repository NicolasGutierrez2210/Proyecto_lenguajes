import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import parse_code, parse_file

class TestDaZeErrors(unittest.TestCase):

    def test_error_sintactico_parentesis_incompleto(self):
        codigo = 'datos = fichar("ruta/archivo.csv"'
        tree, parser, errors = parse_code(codigo)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("Sintactico" in e.error_type for e in errors))

    def test_error_sintactico_pipeline_malformado(self):
        codigo = "resultado = |> descartar(x > 0)"
        tree, parser, errors = parse_code(codigo)
        self.assertGreater(len(errors), 0)

    def test_error_sintactico_bloque_sin_cerrar(self):
        codigo = """
        pizarra barras(datos) {
            eje_x = posicion
        """
        tree, parser, errors = parse_code(codigo)
        self.assertGreater(len(errors), 0)

    def test_error_lexico_simbolos_invalidos(self):
        codigo = "var$invalida = 100 @ 20;"
        tree, parser, errors = parse_code(codigo)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("Lexico" in e.error_type for e in errors))

    def test_archivos_incorrectos_ejemplos(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "examples"))
        
        ruta_sintaxis = os.path.join(base_dir, "incorrecto_sintaxis.dz")
        tree, parser, errors_sintaxis = parse_file(ruta_sintaxis)
        self.assertGreater(len(errors_sintaxis), 0)

        ruta_lexico = os.path.join(base_dir, "incorrecto_lexico.dz")
        tree, parser, errors_lexico = parse_file(ruta_lexico)
        self.assertGreater(len(errors_lexico), 0)

if __name__ == "__main__":
    unittest.main()
