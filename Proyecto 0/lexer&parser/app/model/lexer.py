from app.model import reserved_language as rl
import re

def get_tokens(code: str) -> list:
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in rl.TOKEN_SPECIFICATION)

    tokens = []
    for match in re.finditer(tok_regex, code, re.IGNORECASE):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))

    return tokens

if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")