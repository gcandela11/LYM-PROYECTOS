"""
    Universidad de los Andes, Bogotá - Colombia.
    Lenguajes y Máquinas 2023-2.

    Este modulo contiene las palabras reservadas del lenguaje definido para
    el robot, así como los formatos de las funciones, procedimientos entre otros.

    Autores:
        - David Jimenez Mora Cod. 202213799.
        - Catalina Álvarez Latorre Cod. 202220307.

"""

TOKEN_SPECIFICATION = [
    ('MOVE_DIR', r'move-dir'), ('RUN_DIRS', r'run-dirs'), ('MOVE_FACE', r'move-face'),
    ('MBALL', r'myBalloons'), ('BALLH', r'baloonsHere'), ('CHIPH', r'chipsHere'),
    ('REPEAT_TIMES', r'RepeatTimes'), ('CAN_PUT', r'can-put\?'), ('CAN_PICK', r'can-pick\?'),
    ('CAN_MOVE', r'can-move\?'), ('IS_ZERO', r'isZero\?'),
    ('MXPOS', r'myXPos'), ('MYPOS', r'myYPos'), ('MCHIPS', r'myChips'),
    ('FACING', r'facing?'), ('BLOCKED', r'blocked?'),
    ('AROUND', r':around'), ('BALLONS', r':ballons'), ('CHIPS', r':chips'),
    ('SPACES', r'spaces'), ('NORTH', r':north'), ('SOUTH', r':south'), ('EAST', r':east'),
    ('WEST', r':west'), ('FRONT', r':front'), ('BACK', r':back'), ('LEFT', r':left'),
    ('RIGHT', r':right'), ('DEFUN', r'defun'), ('DEFVAR', r'defvar'), ('INTERROGATION', r'\?'),
    ('SEMICOLON', r';'), ('ASSIGN', r'='), ('REPEAT', r'Repeat'), ('MOVE', r'move'),
    ('SKIP', r'skip'), ('TURN', r'turn'), ('FACE', r'face'), ('PUT', r'put'),
    ('PICK', r'pick'), ('NULL', r'null'), ('NOT', r'not'), ('IF', r'if'),
    ('DIM', r'Dim'),

    ('NUMBER', r'\d+'), ('VARIABLE', r'[a-zA-Z_][a-zA-Z_0-9]*'),

    ('MF', r'(\bM\b|(?<=\()M(?=\))|M(?=;))'),
    ('TR', r'(\bR\b|(?<=\()R(?=\))|R(?=;))'),
    ('DC', r'(\bC\b|(?<=\()C(?=\))|C(?=;))'),
    ('PB', r'(\bB\b|(?<=\()B(?=\))|B(?=;))'),
    ('PC', r'(\bc\b|(?<=\()c(?=\))|c(?=;))'),
    ('GB', r'(\bb\b|(?<=\()b(?=\))|b(?=;))'),
    ('POB', r'(\bP\b|(?<=\()P(?=\))|P(?=;))'),

    ('J', r'J'), ('G', r'G'), ('LPAREN', r'\('), ('RPAREN', r'\)'),
    #('SPACE', r'\s+')
]

