import gmpy2

def encryptChar(xChar, a, b):
    x = ord(xChar) - ord('a') # Use 'a' as 0
    return (chr( (5*x+7)%26 + ord('a') )) # Undo shift

def encryptString(string, a, b):
    result = ""
    for i in range(len(string)):
        result+=(encryptChar(string[i], a, b))
    return (result)

def decryptChar(xChar, a, b):
    x = ord(xChar) - ord('a') # Use 'a' as 0
    return (chr( (gmpy2.invert(a, 26)*(x-b)%26)+ord('a')))

def decryptString(string, a, b):
    result = ""
    for i in range(len(string)):
        result+=(decryptChar(string[i], a, b))
    return (result)

a = 5
b = 7

cyphertext = encryptString("helloworld", a, b)
print(cyphertext)

c = gmpy2.invert(a, 26)
print("The modular multiplicative inverse of a is:" + str(c))
decryptedCyphertext = decryptString(cyphertext, a, b)
print(decryptedCyphertext)
