#Reverse word exercise.
sir1 = input("Write a sentence: ")
#we separate the string in words
cuv = sir1.split()
#we create an empty array for the words 
rev_sir1 = []

for i in cuv: 
    #slicing is done using the syntax [start:stop:step]
    #[::-1] creates a new, reversed copy of the original sequence. It does not modify the original sequence in place.
    rev_sir1.append(i[::-1]) 

sir2 = " ".join(rev_sir1)

print("Reversed sentence: ", sir2) 
