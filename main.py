import re
#Imported re to handle regular expressions

def tokenize_code(input_file):
    # Define regular expressions for different types of tokens
    keyword_regex = r'\b(if|else|return|while|for|int|float|char|void)\b'
    separator_regex = r'([{}();])'
    operator_regex = r'([=+\-*/<>]=?)'
    identifier_regex = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    integer_regex = r'\b\d+\b'
    comment_regex = r'\/\/.*'

    # Create a dictionary to map regular expressions to their corresponding token names
    token_patterns = {
        keyword_regex: "keyword",
        separator_regex: "separator",
        operator_regex: "operator",
        identifier_regex: "identifier",
        integer_regex: "integer",
        comment_regex: "comment",
    }

    lexemes_and_tokens = []

    with open(input_file, 'r') as file:
        for line in file:
            # Remove comments
            line = re.sub(comment_regex, '', line)
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

    # Print the result
    for lexeme, token in lexemes_and_tokens:
        print(f'"{lexeme}" = {token}')
