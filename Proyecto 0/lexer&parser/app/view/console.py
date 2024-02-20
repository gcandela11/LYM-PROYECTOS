"""


"""
import config as cf
import os
import time
from app.controller import controller

def clear_console():
    """
    Función que limpia la consola en Python dos veces, para Windows y para otros SO.

    Args:
        None

    Returns:
        None
    """

    try: #Para Windows
        None
        os.system("cls"); os.system("cls")

    except: #Para otros SO
        None
        os.system("clear"); os.system("clear")

    pass

def print_menu():
    """
    Prints the main menu of the application.

    Args:
        None

    Returns:
        None
    """

    print("\n1. Verificar la sintaxis de un código.")
    print("2. Salir.")


def exec_option(option: int):
    """
    Executes the option selected by the user.

    Args:
        option (int): The option selected by the user.

    Returns:
        None
    """

    if option == 1:
        exec_opt1()

    elif option == 2:
        print("Gracias por usar el programa, hasta luego.")
        exit()

def exec_opt1():
    clear_console()
    print("Perfecto, para verificar la sintaxis de el código, primero debes indicar donde está ubicado el archivo.")

    while True:
        print(f"Quieres usar el archivo por defecto ubicado en {cf.data_dir + '/program.txt'} o prefieres indicar la ruta de otro archivo? (S/N)")
        option = input(">>> ")

        if option.lower() == "s":
            print("\nPerfecto se usará el archivo por defecto.")
            file_path = cf.data_dir + "/program.txt"

            code = controller.open_file(file_path)
            break

        elif option.lower() == "n":
            print("\nPor favor, indica la ruta del archivo (recuerda que debe ser un archivo .txt):")
            file_path = input(">>> ")

            code = controller.open_file(file_path)
            break

        else:
            print("\nOpción no válida, vuelve a intentarlo.")
            time.sleep(1.5); clear_console()

    if code == InterruptedError:
        print("Ingresaste un archivo que no está en formato .txt, vuelve a intentarlo.")
        return 0

    else:
        clear_console()
        print(f"{'#' * 50} ANALIZANDO CÓDIGO {'#' * 50}")
        print(f"Archivo analizado: {file_path}")

        print(f"\n{'#' * 50} VERIFICANDO PARÉNTESIS {'#' * 50}")
        are_brackets_balanced = controller.verify_parens(code)
        print(f"{'#' * 50} PARÉNTESIS VERIFICADOS {'#' * 50}\n'")

        if are_brackets_balanced:
            print(f"{'#' * 50} CREANDO TOKENS {'#' * 50}")
            tokens = controller.lex_code(code)

            print(f"{'#' * 50} TOKENS CREADOS {'#' * 50}\n")

            print("El proyecto se realizó con éxito, hasta este punto, por lo cual lo demás está comentado y no se ejecutará.")
            print("Tokens encontrados:")
            print(tokens)

            """print(f"{'#' * 50} VERIFICANDO SINTAXIS {'#' * 50}")
            is_syntax_correct = controller.parse_code(tokens)
            print(f"{'#' * 50} SINTAXIS VERIFICADA {'#' * 50}\n")

            if is_syntax_correct:
                print("El código está escrito correctamente.")
                return 0

            else:
                print("El código tiene errores de sintaxis, vuelve a intentarlo.")
                return 0"""

        else:
            print("ERROR: PARÉNTESIS INCORRECTOS")
            print(f"{TypeError} - El número de paréntesis de apertura y cierre no es el mismo.")
            return 0

def init():
    while True:
        print_menu()
        option = int(input(">>> "))
        exec_option(option)

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")