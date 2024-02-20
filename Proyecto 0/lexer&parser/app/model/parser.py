"""

"""

from app.model import reserved_language as rl

def parse(tokens :list) -> bool:
    """
    """
    global_vars = {}
    pos = 0

    while pos < len(tokens):
        token = tokens[pos][0]

        if token == "DEFVAR":
            pos, result = parse_var(pos, tokens, global_vars)

        elif token == "DEFPROC":
            parse_proc(pos, tokens, global_vars)

        elif token == "LLAVE_A":
            parse_code_block(pos, tokens)


def parse_var(pos: int, tokens: list, global_vars: dict) -> bool:
    """
    Checks whether the variable is well defined or not and adds it to the global_vars dict.

    Args:
        pos (int): The position of the token in the tokens list.
        tokens (list): The list of tokens.
        global_vars (dict): The dictionary of global variables.

    Returns:
        bool: True if the variable is well defined, False otherwise.

    Changes:
        global_vars (dict): Adds the variable to the dictionary if it is well defined.
    """

    is_def_ok = False; is_name_ok = False; is_value_ok = False

    token_info = tokens[pos]; token = token_info[0]
    if token == "DEFVAR":
        is_def_ok = True
    pos += 1

    token_info = tokens[pos]; token = token_info[0]; var_name = token_info[1]
    if token == "ID" and var_name.isalpha() and var_name.isnumeric() == False:
        is_name_ok = True
    pos += 1

    token_info = tokens[pos]; token = token_info[0]; var_value = token_info[1]
    if token == "VALOR" and var_value.isalnum():
        is_value_ok = True
    pos += 1

    if is_def_ok and is_name_ok and is_value_ok:
        global_vars[var_name] = var_value
        return pos, True

    else:
        if not is_def_ok:
            print(SyntaxError("Error: The correct syntax is 'defVar <name> <value>'"))

        if not is_name_ok:
            print(SyntaxError("Error: The name of the variable must be a alphanumeric string."))

        if not is_value_ok:
            print("Error: The value of the variable must be a number or a alphanumeric string.")

        exit()


def parse_proc(pos: int, tokens: list, global_vars: dict) -> bool:
    """
    Checks whether the procedure is well defined or not and adds it to the global_vars dict.

    The correct definition for a procedure is: 'defProc <name> (<param1>, <param2>, ..., <paramN>) { <code> }'
    Args:
        pos (int): The position of the token in the tokens list.
        tokens (list): The list of tokens.
        global_vars (dict): The dictionary of global variables.

    Returns:
        bool: True if the procedure is well defined, False otherwise.
    """

    is_def_ok = False; is_name_ok = False; is_parentesis_A_ok = False
    is_parentesis_B_ok = False; is_params_ok = False; is_llave_A_ok = False
    is_code_block_ok = False; is_llave_B_ok = False
    proc_params = []

    token_info = tokens[pos]; token = token_info[0]
    if token == "DEFPROC":
        is_def_ok = True
    pos += 1

    token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
    if token == "ID" and text.isalpha() and text.isnumeric() == False:
        is_name_ok = True
    pos += 1

    if token == "PARENTESIS_A":
        is_parentesis_A_ok = True
    pos += 1

    while True:
        token_info = tokens[pos]; token = token_info[0]; text = token_info[1]

        if token == "ID" and text.isalpha() and text.isnumeric() == False:
            proc_params.append(text)
            pos += 1

            token_info = tokens[pos]; token = token_info[0]

            if token == "COMA" or token == "PARENTESIS_B":
                if token == "PARENTESIS_B":
                    pos += 1
                    is_params_ok = True
                    is_parentesis_B_ok = True
                    break

                elif token == "COMA":
                    pos += 1
                    continue

            else:
                print(SyntaxError("Error: Expected ',' or ') after parameter."))
                exit()


    token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
    if token == "LLAVE_A" and text == "{":
        is_llave_A_ok = True
        pos += 1
        is_code_block_ok = parse_code_block(pos, tokens, global_vars, proc_params)

        if is_code_block_ok: is_llave_B_ok = True


def parse_code_block(pos: int, tokens: list, global_vars: dict, proc_params: list, used_vars_in_code_block = []) -> bool:
    """

    """

    local_vars = {}
    is_code_block_ok = False; is_llave_B_ok = False

    while True:
        token_info = tokens[pos]; token = token_info[0]; text = token_info[1]

        if token in rl.RESERVED_PROCEDURES: # If the token is a reserved procedure.
            is_parentesis_A_ok = False; is_parentesis_B_ok = False; is_params_ok = False

            pos += 1
            token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
            if token == "PARENTESIS_A" and text == "(":
                is_parentesis_A_ok = True
                pos += 1

                while True:
                    token_info = tokens[pos]; token = token_info[0]; text = token_info[1]

                    if token == "ID" and text.isalpha() and text.isnumeric() == False:
                        used_vars_in_code_block.append(text)
                        pos += 1

                        token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
                        if token == "COMA" and text == "," or token == "PARENTESIS_B" and text == ")":
                            if token == "PARENTESIS_B" and text == ")":
                                is_params_ok = True
                                is_parentesis_B_ok = True
                                break

                            elif token == "COMA" and text == ",":
                                pos += 1
                                continue

                        else:
                            print(SyntaxError("Error: Expected ',' or ')' after parameter."))
                            exit()

            else:
                print(SyntaxError("Error: Expected '(' after procedure declaration."))
                exit()

        if token in rl.RESERVED_CONDITIONS: # If the token is a reserved condition.
            print(TypeError("Error: Cannot use reserved condition if it is not inside a conditional statement."))
            exit()

        elif token == "DEFVAR" and text == "defVar":
            parse_var(pos, tokens, local_vars)

        elif token == "IF" and text == "if":
            pos += 1
            token_info = tokens[pos]; token = token_info[0]; text = token_info[1]

            if token in rl.RESERVED_CONDITIONS:
                pos += 1
                parse_if(pos, tokens, global_vars, proc_params, local_vars, used_vars_in_code_block)

            else:
                print(SyntaxError("Error: Expected a valid condition after 'if' statement declaration."))
                exit()

        elif token == "WHILE" and text == "while":
            parse_while()

        elif token == "REPEAT" and text == "repeat":
            parse_repeat()

        elif token == "LLAVE_B" and text == "}":
            is_llave_B_ok = True
            break

        else:
            print(SyntaxError("Error: Expected '}'"))
    pass

def parse_if(pos: int, tokens: list, global_vars: dict, proc_params: list, local_vars: dict, used_vars_in_code_block: list) -> bool:
    """
    """

    is_llave_A_ok = False; is_code_block_ok = False; is_llave_B_ok = False; has_else = False; is_else_ok = False

    token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
    if token == "LLAVE_A" and text == "{":
        is_llave_A_ok = True
        pos += 1
        is_code_block_ok = parse_code_block(pos, tokens, global_vars, proc_params, local_vars, used_vars_in_code_block)

        if is_code_block_ok:
            is_llave_B_ok = True
            pos += 1

            token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
            if token == "ELSE" and text == "else":
                has_else = True
                pos += 1
                is_else_ok = parse_else(pos, tokens, global_vars, proc_params, local_vars, used_vars_in_code_block)

            if is_llave_A_ok and is_code_block_ok and is_llave_B_ok:
                if not has_else:
                    return True

                elif has_else and is_else_ok:
                    return True

                else:
                    print(SyntaxError("Error: Expected a valid 'else' statement after 'if' statement and condition declaration."))
                    exit()

            else:
                if not is_llave_A_ok:
                    print(SyntaxError("Error: Expected '{' after 'if' statement and condition declaration."))

                if not is_code_block_ok:
                    print(SyntaxError("Error: Expected a valid code block after 'if' statement and condition declaration."))

                if not is_llave_B_ok:
                    print(SyntaxError("Error: Expected '}' after 'if' statement and condition declaration."))

                exit()

    else:
        print(SyntaxError("Error: Expected '{' after 'if' statement and condition declaration."))
        exit()
    pass

def parse_else(pos: int, tokens: list, global_vars: dict, proc_params: list, local_vars: dict, used_vars_in_code_block: list) -> bool:
    """

    """

    is_llave_A_ok = False; is_code_block_ok = False; is_llave_B_ok = False

    token_info = tokens[pos]; token = token_info[0]; text = token_info[1]
    if token == "LLAVE_A" and text == "{":
        is_llave_A_ok = True
        pos += 1
        is_code_block_ok = parse_code_block(pos, tokens, global_vars, proc_params, local_vars, used_vars_in_code_block)

        if is_code_block_ok:
            is_llave_B_ok = True
            pos += 1

        if is_llave_A_ok and is_code_block_ok and is_llave_B_ok:
            return True

        else:
            if not is_llave_A_ok:
                print(SyntaxError("Error: Expected '{' after 'else' statement declaration."))

            if not is_code_block_ok:
                print(SyntaxError("Error: Expected a valid code block after 'else' statement declaration."))

            if not is_llave_B_ok:
                print(SyntaxError("Error: Expected '}' after 'else' statement declaration."))

            exit()

    else:
        print(SyntaxError("Error: Expected '{' after 'else' statement declaration."))
        exit()
    pass
def parse_while():
    pass

def parse_repeat():
    pass

def parse_facing():
    pass

def parse_can():
    pass

def parse_not():
    pass


if __name__ == "__main__":
    print("Este modulo no se puede ejecutar directamente.")
    print("Para ejecutar el programa, ejecuta el archivo main.py en la carpeta madre del proyecto.")