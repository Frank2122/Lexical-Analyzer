import re
#Imported re to handle regular expressions

def tokenize_code(input_file):
    # Defined regular expressions for different types of tokens
    keyword = r'\b(if|else|return|while|for|int|float|char|void)\b'
    separator = r'([{}();])'
    operator = r'([=+\-*/<>]=?)'
    identifier = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    integer = r'\b\d+\b'
    comment = r'\/\/.*'

    # Created a dictionary to map regular expressions to their corresponding token names
    token_patterns = {
        keyword: "keyword",
        separator: "separator",
        operator: "operator",
        identifier: "identifier",
        integer: "integer",
        comment: "comment",
    }

    lexemes_and_tokens = []

    with open(input_file, 'r') as file:
        for line in file:
            # Removes comments, hopefully
            line = re.sub(comment, '', line)
            line = line.strip()

            if not line:
                continue  # Skip empty lines

            while line:
                matched = False
                for pattern, token_name in token_patterns.items():
                    match = re.match(pattern, line)
                    if match:
                        lexeme = match.group(0)
                        lexemes_and_tokens.append((lexeme, token_name))
                        line = line[len(lexeme):]
                        matched = True
                        break

                if not matched:
                    print(f"Error: Unrecognized token at the beginning of the line: {line}")
                    break

    return lexemes_and_tokens

if __name__ == "__main__":
    input_file = "input.txt"
    lexemes_and_tokens = tokenize_code(input_file)

    # Prints the result, hopefully
    for lexeme, token in lexemes_and_tokens:
        print(f'"{lexeme}" = {token}')
