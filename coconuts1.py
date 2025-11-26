#Coconuts Exercise 

def coconut_translator(text, word="coconuts"):
    result = []

#we go through every character in the text
    for char in text:
        binary_bits = format(ord(char), "08b") #transforms the text in 8-bit format, ord converts the character in ASCII value
        mapped_word = ""
        
#we construct the coconut word with uppercase and lowercase if 1 and 0        
        for bit, letter in zip(binary_bits, word): # we use zip function to join binary_bits with every letter from coconut 
            if bit == "1": 
                mapped_word += letter.upper()
            else:
                mapped_word += letter.lower()

        result.append(mapped_word) 

    return " ".join(result) 

#testing part
print("Hi")
print(coconut_translator("Hi"))

print("\nImi este somn")
print(coconut_translator("Imi este somn"))
