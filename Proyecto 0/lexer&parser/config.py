"""
    Universidad de los Andes, Bogotá - Colombia.
    Lenguajes y Máquinas 2023-2.

    Este modulo contiene las configuraciones del proyecto.
    Se utiliza para definir las rutas de los archivos de entrada y salida.

    Autores:
        - David Jimenez Mora Cod. 202213799.
        - Catalina Álvarez Latorre Cod. 202220307.

"""

import os
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_dir = os.path.dirname(os.path.realpath('__file__'))

sys.path.insert(0, os.path.abspath(file_dir))

data_dir = file_dir + '/data'

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")
