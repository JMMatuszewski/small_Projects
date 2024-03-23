import pyperclip

MODES = 'ED'
# ASCII PART
# A - Z

''' Caesar Code '''
def main():
    #Collect data
    while True:
        print("Select mode - (E)ncode, (D)ecode")
        mode = input('> ')
        mode = mode.upper()
        if mode in MODES:
            print("Please write the message:")
            message = input('> ').upper()
            break
        else:
            continue

    while True:
        print("Select the key: 0 to 25")
        key = input('> ')
        if key.isdecimal:
            key = int(key)
            if 0 <= key <= 25:
                break

    #Transform the message
    transformedMessage = ''
    if mode == 'E':
        for symbol in message:
            # Check if A-Z symbol
            symbolASCII = ord(symbol)
            if 65 <= symbolASCII <= 90:
                symbolASCII += key
                if symbolASCII > 90:
                    symbolASCII -= 26
                transformedMessage += chr(symbolASCII)
            else:
                transformedMessage += symbol

    else:
        for symbol in message:
            # Check of A-Z symbol
            symbolASCII = ord(symbol)
            if 65 <= symbolASCII <= 90:
                symbolASCII -= key
                if symbolASCII < 65:
                    symbolASCII += 26
                transformedMessage += chr(symbolASCII)
            else:
                transformedMessage += symbol

    # Display transformed message
    print(transformedMessage)

    # Copy to clipboard for easier use in next run
    try:
        pyperclip.copy(transformedMessage)
        print('Transformed message has been copied to clipboard')
    except:
        # Library has not been installed
        pass  



''' Start the program '''
if __name__ == '__main__':
    main()
