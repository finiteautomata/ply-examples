"""Archivo principal."""
from parser import parser

if __name__ == '__main__':
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue

        result = parser.parse(s)
        print(result)
