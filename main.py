import re

KEYWORDS = ["if", "else", "return", "int", "float", "char", "void"]
OPERATORS = [
    "+", "-", "*", "/", "=", "<", ">", "&", "|", "^", "!", "~", "?", ":", "==", "!=", ">="
]
SEPARATORS = ["(", ")", "{", "}", "[", "]", ";", ","]

def tokenize(code):
    tokens = []
    for match in re.finditer(r"(\b\w+\b)|(\W)", code):
        match = match.group(0)
        if match in KEYWORDS:
            tokens.append((match, "KEYWORD"))
        elif match in OPERATORS:
            tokens.append((match, "OPERATOR"))
        elif match in SEPARATORS:
            tokens.append((match, "SEPARATOR"))
        elif match.isdigit():
            tokens.append((match, "INTEGER"))
        elif match.isalpha():
            tokens.append((match, "IDENTIFIER"))
    return tokens

def main():
    with open("input.txt", "r") as f:
        code = f.read()
    
    tokens = tokenize(code)

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()