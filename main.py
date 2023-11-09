import re #Imported to read regular expressions

#defined different KEYWORDS, OPERATORS, and SEPARATORS
KEYWORDS = ["if", "else", "return", "int", "float", "char", "void"]
OPERATORS = [
    "+", "-", "*", "/", "=", "<", ">", "&", "|", "^", "!", "~", "?", ":", "==", "!=", ">="
]
SEPARATORS = ["(", ")", "{", "}", "[", "]", ";", ","]

#Tokenizes our .txt file
def tokenize(code):
    tokens = []
    lines = code.split('\n')
    for line in lines:
        # Removes comment in each line. Needed to implement to handle phrases after "//"
        line = line.split('//')[0]
        for match in re.finditer(r"(\b\w+\b)|(\W)", line):
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