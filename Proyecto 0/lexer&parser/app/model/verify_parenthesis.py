def check_parens_balance(code: str):
    """
    Función que comprueba si el número de paréntesis de apertura y cierre es el mismo.

    Args:
        code (str): Código a analizar.

    Returns:
        bool: True si el número de paréntesis de apertura y cierre es el mismo, False en caso contrario.
    """

    open_parens = 0
    close_parens = 0

    for line in code.split("\n"):
        open_parens += line.count("(")
        close_parens += line.count(")")

    if open_parens == close_parens:
        return True

    else:
        return False

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")