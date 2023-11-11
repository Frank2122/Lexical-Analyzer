import re #Imported to read regular expressions

#Defined different KEYWORDS, OPERATORS, and SEPARATORS
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
        line = line.split('//')[0] #Splits each line that use "//", and removes the comments present on that line following "//"
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
    with open("input.txt", "r") as f: #Reads input.txt
        code = f.read()
    
    tokens = tokenize(code)

    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()

# Much of our initial problem was met with handling comments. While we figured out reading and separating keywords,
# operators, separators, integers, and identifiers, it began to label the comments as identifiers. We rectified this splitting
# the line after "//" and removing the comments after it on the same line. That way we can ensure that code written 
# after the comments can still be translated.