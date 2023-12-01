from dataclasses import dataclass
from enum import Enum

#Math Interpreter explained
#https://www.youtube.com/watch?v=88lmIMHhYNs

class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MULTIPLY = 2
    LPAREN = 3
    RPAREN = 4


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f':{self.value}' if not self.value is None else "")


WHITESPACE = ' '
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        self.current_char = None

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"illegal exception {self.current_char}")

    def generate_number(self):
        number_str = self.current_char
        self.advance()
        while not self.current_char is None and self.current_char in DIGITS:
            number_str += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(number_str))


@dataclass
class NumberNode:
    value: int

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"


class Parser:
    def __init__(self, tokens1):
        self.tokens = iter(tokens1)
        self.advance()
        self.current_token = None

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None
        result = self.expr()
        if self.current_token is not None:
            self.raise_error()

        return result

    def raise_error(self):
        raise Exception("Invalid syntax")

    def expr(self):
        result = self.term()
        while not self.current_token is None and self.current_token.type in (TokenType.MULTIPLY, TokenType.PLUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.term())

        return result

    def term(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            self.advance()
            return result
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)


@dataclass
class Number:
    value: int

    def __repr__(self):
        return f"{self.value}"


class Intepreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)


text = "5  +  6"
text = "1 + 2 * 3 + 4 * 5 + 6"
text = "2 * 3 + (4 * 5)"
text = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
text = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
text = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

summe = 0
f = open("input1", 'r')
for text in f:
    text = text[0:-1]
    print(text)
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    value = Intepreter().visit(tree)
    print(tree)
    print(value)
    summe += value.value

print(summe)
