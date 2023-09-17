import re

class Token:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

def analizar(entrada):
    tokens = []
    palabras_reservadas = ["SELECT", "FROM", "WHERE", "JOIN", "GROUP BY", "ORDER BY"]
    columnas = ["id", "nombre", "apellido", "edad"]
    tablas = ["usuarios", "productos", "pedidos"]
    elementos = entrada.split() 

    for elemento in elementos:
        tipo = obtener_tipo(elemento, palabras_reservadas, columnas, tablas)
        tokens.append(Token(elemento, tipo))
    return tokens   

def obtener_tipo(elemento, palabras_reservadas, columnas, tablas):
    if elemento.upper() in palabras_reservadas:
        return "Palabra reservada"
    elif elemento.lower() in columnas:
        return "Columna"
    elif elemento.lower() in tablas:
        return "Tabla"
    elif re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', elemento):
        return "Correo electrónico" 
    elif re.match(r'\d{1,2}\.\d{1,2}\.\d{4}', elemento):
        return "Fecha" 
    else:
        return "Dato desconocido"
    
def main():
    print("Escribe los datos separados por espacios:")
    input_data = input()
    tokens = analizar(input_data)

    print("\nTokens-Etiquetas:")
    for token in tokens:
        print(f"{token.valor} ({token.tipo})")

if __name__ == "__main__":
    main()  