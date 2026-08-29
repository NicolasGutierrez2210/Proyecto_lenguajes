import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import tokenize_code, DaZeLexer


class TestDaZeLexer(unittest.TestCase):

    def test_palabras_reservadas(self):
        codigo = "cargar guardar seleccionar filtrar crear renombrar ordenar agrupar resumir graficar si sino funcion retornar"
        tokens = [t for t in tokenize_code(codigo) if t.text != "<EOF>"]
        
        expected_types = [
            DaZeLexer.CARGAR,
            DaZeLexer.GUARDAR,
            DaZeLexer.SELECCIONAR,
            DaZeLexer.FILTRAR,
            DaZeLexer.CREAR,
            DaZeLexer.RENOMBRAR,
            DaZeLexer.ORDENAR,
            DaZeLexer.AGRUPAR,
            DaZeLexer.RESUMIR,
            DaZeLexer.GRAFICAR,
            DaZeLexer.SI,
            DaZeLexer.SINO,
            DaZeLexer.FUNCION,
            DaZeLexer.RETORNAR,
        ]
        
        token_types = [t.type for t in tokens]
        self.assertEqual(token_types, expected_types)

    def test_literales(self):
        codigo = '123 45.67 "texto doble" \'texto simple\' verdadero falso true false nulo null'
        tokens = [t for t in tokenize_code(codigo) if t.text != "<EOF>"]
        
        self.assertEqual(tokens[0].type, DaZeLexer.ENTERO)
        self.assertEqual(tokens[1].type, DaZeLexer.DECIMAL)
        self.assertEqual(tokens[2].type, DaZeLexer.CADENA)
        self.assertEqual(tokens[3].type, DaZeLexer.CADENA)
        self.assertEqual(tokens[4].type, DaZeLexer.VERDADERO)
        self.assertEqual(tokens[5].type, DaZeLexer.FALSO)
        self.assertEqual(tokens[6].type, DaZeLexer.VERDADERO)
        self.assertEqual(tokens[7].type, DaZeLexer.FALSO)
        self.assertEqual(tokens[8].type, DaZeLexer.NULO)
        self.assertEqual(tokens[9].type, DaZeLexer.NULO)

    def test_operadores_y_simbolos(self):
        codigo = "|> = == != < <= > >= + - * / % ^ ** ( ) [ ] { } , ; :"
        tokens = [t for t in tokenize_code(codigo) if t.text != "<EOF>"]
        
        expected_types = [
            DaZeLexer.PIPE,
            DaZeLexer.ASIGNAR,
            DaZeLexer.IGUAL_IGUAL,
            DaZeLexer.DIFERENTE,
            DaZeLexer.MENOR,
            DaZeLexer.MENOR_IGUAL,
            DaZeLexer.MAYOR,
            DaZeLexer.MAYOR_IGUAL,
            DaZeLexer.MAS,
            DaZeLexer.MENOS,
            DaZeLexer.MULT,
            DaZeLexer.DIV,
            DaZeLexer.MOD,
            DaZeLexer.POT,
            DaZeLexer.POT,
            DaZeLexer.LPAREN,
            DaZeLexer.RPAREN,
            DaZeLexer.LBRACK,
            DaZeLexer.RBRACK,
            DaZeLexer.LBRACE,
            DaZeLexer.RBRACE,
            DaZeLexer.COMA,
            DaZeLexer.PUNTO_Y_COMA,
            DaZeLexer.DOS_PUNTOS,
        ]
        
        token_types = [t.type for t in tokens]
        self.assertEqual(token_types, expected_types)

    def test_operadores_logicos(self):
        codigo = "y and && o or || no not !"
        tokens = [t for t in tokenize_code(codigo) if t.text != "<EOF>"]
        
        self.assertEqual(tokens[0].type, DaZeLexer.Y)
        self.assertEqual(tokens[1].type, DaZeLexer.Y)
        self.assertEqual(tokens[2].type, DaZeLexer.Y)
        self.assertEqual(tokens[3].type, DaZeLexer.O)
        self.assertEqual(tokens[4].type, DaZeLexer.O)
        self.assertEqual(tokens[5].type, DaZeLexer.O)
        self.assertEqual(tokens[6].type, DaZeLexer.NO)
        self.assertEqual(tokens[7].type, DaZeLexer.NO)
        self.assertEqual(tokens[8].type, DaZeLexer.NO)

    def test_comentarios_y_espacios(self):
        codigo = """
        # Comentario de linea tipo numeral
        // Comentario de linea tipo doble barra
        /* Comentario de bloque
           multilinea */
        x = 10;
        """
        tokens = [t for t in tokenize_code(codigo) if t.text != "<EOF>"]
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].text, "x")
        self.assertEqual(tokens[1].text, "=")
        self.assertEqual(tokens[2].text, "10")
        self.assertEqual(tokens[3].text, ";")


if __name__ == "__main__":
    unittest.main()
