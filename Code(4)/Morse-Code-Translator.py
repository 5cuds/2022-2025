
dictlist = {'A': '.-',     'B': '-...',   'C': '-.-.', 
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..', " ": "/" ,

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.' }

CODE_REVERSed = {value:key for key,value in dictlist.items()}


def Basic_Translator():
    user_input = input("====================)\nPut Your Horse Code Here: ").upper()
    converter_list = user_input.split()
    
    print("\nTranslated:", "".join(CODE_REVERSed[i] for i in converter_list).capitalize())

def convert_to_morse():
    texts = input("====================)\nPut Your Text Here: ").upper()
    print("\nConverted:", " ".join(dictlist[i] for i in texts))


def main():

    while True:
        try:
            print("====================)\nMorse Code Translator\n====================)\n1)Translate\n2)Convert\n3)Exit\n====================)")
            user_input = int(input("> "))

            if user_input == 1:
                Basic_Translator()
            elif user_input == 2:
                convert_to_morse()
            else:
                print("Thank You For Using Python Morse Code Translstor!\nGoodbye!")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()