"""


"""

from app.model import lexer
from app.model import parser
from app.model import verify_parenthesis
from app.model import file_management

def open_file(file_path: str) -> str:
    """
    Opens a text file and reads it as a string.

    Args:
        file_path (str): The path of the text file (Must be a .txt file).

    Returns:
        str: The content of the text file.
    """

    return file_management.openFile(file_path)


def verify_parens(code: str) -> bool:
    """
    Verifies if the number of opening and closing parenthesis is the same in the source code.

    Args:
        code (str): The source code to analyze.

    Returns:
        bool: True if the number of opening and closing parenthesis is the same, False otherwise.
    """

    return verify_parenthesis.check_parens_balance(code)


def lex_code(code: str) -> list:
    """
    Creates a list of tokens from the source code.

    Args:
        code (str): The source code to analyze.

    Returns:
        list: A list of tokens.
    """

    return lexer.get_tokens(code)

def parse_code(tokens: list) -> list:
    """
    Parses a list of tokens and checks if the syntax is correct.

    Args:
        tokens (list): The list of tokens.

    Returns:
        list: A tree of tokens.
    """

    return parser.parse(tokens)

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")