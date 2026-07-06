from enum import Enum

class TokenType(Enum):
    # Single-character tokens.
    NUMBER = "THENUMBER"
    IDENTIFIER="IDENTIFIER"
    PLUS='+'
    MINUS='-'
    SLASH='/'
    STAR='*'
    EQUAL='='
    LEFT_PAREN='('
    RIGHT_PAREN=')'
    EOF='EOF'

class Token:
    def __init__(self,type_,value=None):
        self.type=type_
        self.value=value
    def __repr__(self):
        if self.value is None:
            return self.type.name
        return f"{self.type.name}({self.value})"
# token = Token(TokenType.NUMBER, 42)

# print(token)

