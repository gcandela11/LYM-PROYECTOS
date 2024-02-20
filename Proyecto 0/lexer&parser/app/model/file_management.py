def openFile(file_path: str) -> str:
    """
    Función que abre un archivo de texto y lo convierte en una lista de líneas.

    Args:
        file_path (str): Ruta del archivo de texto.

    Returns:
        str: Contenido del archivo.
    """

    if file_path[-4:] == ".txt":
        file = open(file_path, "r")

        return file.read().lower().replace("\n", "").replace("\t", "")

    else:
        return InterruptedError

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")