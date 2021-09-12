def main():
    
    secret_codes = create_code()
    
    text = open("info_security.txt", "r")

    new_file = open("encrypted_info_security.txt", "w")

    encrypted_text = ""

    for line in text:
        for character in line:
            new_file.write(secret_codes[character])            

    new_file.close()        


def create_code():
    codes = {
        'A' : '%', 'a' : '9',
        'B' : '2', 'b' : ')',
        'C' : '@', 'c' : '.',
        'D' : '8', 'd' : '+',
        'E' : '^', 'e' : ':',
        'F' : '1', 'f' : '}',
        'G' : '(', 'g' : '[',
        'H' : '7', 'h' : '?',
        'I' : '[', 'i' : '!',
        'J' : '?', 'j' : '%',
        'K' : '-', 'k' : '$',
        'L' : '0', 'l' : '*',
        'M' : '*', 'm' : '0',
        'N' : '6', 'n' : ')',
        'O' : ')', 'o' : '#',
        'P' : '4', 'p' : '&',
        'Q' : ',', 'q' : '_',
        'R' : '3', 'r' : ':',
        'S' : '$', 's' : '-',
        'T' : '/', 't' : ']',
        'U' : '=', 'u' : '}',
        'V' : '|', 'v' : '5',
        'W' : '{', 'w' : '+',
        'X' : '"', 'x' : '`',
        'Y' : '~', 'y' : ':',
        'Z' : ';', 'z' : '!',
        '.' : '.', ',' : ',',
        ' ' : ' ', ':' : ':'
    }
    return codes

main()
