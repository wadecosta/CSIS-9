# lab 15
def encode(str, key):
    result = ''
    for c in str:
        a = ord(c)-97
        a = (a + key)%26
        b = chr(a + 97)
        result = result + b
    return result
    # you need to complete the encode function
    # this function does not do anything
    #return str

def decode(str, key):
    result = ''
    for c in str:
        a = ord(c)-97
        a = (a - key)%26
        b = chr(a + 97)
        result = result + b
    return result
    # you need to complete the decode function
    # this function does not do anything
    #return str

message = input("enter a message.  Enter only lowercase letters a-z ")
key = int(input("enter a secret key 1 to 26 "))
codemsg = encode(message, key)
print("cypher text is:",codemsg)
cleartext = decode(codemsg,key)
print("clear test is:",cleartext)
        
