"""Calculator lexer example."""
import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

Sí, es súper nigromántico pero es lo que hay.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como se
muestra aquí abajo.

"""

tokens = (
    'NUMBER',
    'PLUS',
    'TIMES',
    'MINUS',
    'LEFT_PAR',
    'RIGHT_PAR',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'

"""Esta variable especial ignora estos caracteres"""
t_ignore = " \t"


def t_NUMBER(t):
    r'\d+'
    """Regla para números.

    Esta función se crea para hacer "algo más" que sólo convertir a token.

    Observar que la primer línea (!) tiene que ser un
    """
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    """
    Regla para newlines. Sólo cuenta la cantidad de estos.
    """

    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


def apply(string):
    """Aplica el análisis léxico al string dado."""
    lexer.input(string)

    return list(lexer)
