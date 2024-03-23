# ASCII PART
# A - Z

''' Caesar Hacker '''
def main():
    #Collect data
    
    print("Please write the message:")
    message = input('> ').upper()

    # Decode for every key
    for key in range(1,26):
        transformedMessage = ''
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

''' Start the program '''
if __name__ == '__main__':
    main()
