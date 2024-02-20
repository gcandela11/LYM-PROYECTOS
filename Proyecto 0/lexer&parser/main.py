"""
    Universidad de los Andes, Bogotá - Colombia.
    Lenguajes y Máquinas 2023-2.

    Este modulo es el punto de entrada del programa.
    Se utiliza para ejecutar el programa.

    Autores:
        - David Jimenez Mora Cod. 202213799.
        - Gustavo Candela Rico Cod. 202223857.
"""

import config as cf
from app.view import console as view

if __name__ == "__main__":
    """
    Si se ejecuta este archivo directamente, se ejecuta la función init() del módulo view para ejecutar el programa.
    """

    view.init(cf)