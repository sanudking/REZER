from tokens import TokenType, Token

class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos=0
    
    @property
    def current_char(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]
    def advance(self):
        self.pos += 1
    # advance , curr_char
    def number(self):
        result = ""
        while (
            self.current_char is not None
            and self.current_char.isdigit()
        ):
            result += self.current_char
            self.advance()

        return Token(
            TokenType.NUMBER,
            int(result)
        )
    def identifier(self):
        result = ""

        while (
            self.current_char is not None
            and (
                self.current_char.isalnum()
                or self.current_char == "_"
            )
        ):
            result += self.current_char
            self.advance()

        return Token(
            TokenType.IDENTIFIER,
            result
        )
    
    def get_next_token(self):
        while self.current_char :
            if self.current_char.isdigit():
                return self.number()
            if self.current_char.isalnum():
                return self.identifier()
            if self.current_char.isspace():
                self.advance()
                continue
            if self.current_char=="+":
                self.advance()
                return Token(TokenType.PLUS)
            if self.current_char=="-":
                self.advance()
                return Token(TokenType.MINUS)
            if self.current_char=="*":
                self.advance()
                return Token(TokenType.STAR)
            if self.current_char=="/":
                self.advance()
                return Token(TokenType.SLASH)
            if self.current_char=="(":
                self.advance()
                return Token(TokenType.LEFT_PAREN)
            if self.current_char=="=":
                self.advance()
                return Token(TokenType.EQUAL)
            if self.current_char==")":
                self.advance()
                return Token(TokenType.RIGHT_PAREN)
            else:
                raise Exception(
                    f"Unknown token: {self.current_char}"
                )
        return Token(TokenType.EOF)
            
            


text = input("rzr> ")

lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    print(token)

    if token.type == TokenType.EOF:
        break
