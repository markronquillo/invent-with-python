# Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():
    # Function that asks the user if it wants to decrypt or encrypt a message
    while True:
        print ('Do you wish to encrypt or decrypt a message?')
        mode = raw_input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    # Asks the message to be encrypted
    print('Enter your message:')
    return raw_input()

def getKey():
    # Asks the key for encryption
    key = 0
    while True:
        print('Enter the key (1-%s)' % (MAX_KEY_SIZE))
        key = int(raw_input())
        if (key >=1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            # this part of the restricts the encoding to alphabet only
            # e.g. if the letter to encrypt is Z and the key is 2
            # it must be converted to B rather than just adding two
            # to its ordinal value (since this will return non alphabet char)
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print ('Your translated text is:')
print (getTranslatedMessage(mode, message, key))


