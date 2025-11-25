#Coconut's exercise first try, trying with just a letter
#First trying to understand how to convert from a string to binary
def bit_translator(string,char = "a"):
    b = " ".join(format(ord(char), "08b") for char in string)
    output = []
    for bit in b:
        if bit =="1":
            output.append(char.upper())
        else:
            output.append(char.lower())
    return "".join(output)

str1 = "Hi"
print(bit_translator(str1,char = "c"))


