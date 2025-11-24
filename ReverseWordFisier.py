#Reverse word exercise from a file named given.txt
#We use the given.txt file and the result is in expected.txt
input_file = "given.txt"
output_file = "expected.txt"

def reverse_file(input_file, output_file):
  #We read the given.txt file
  with open(input_file, "r") as infile:
      content = infile.read()
  #Split the content of the file in words
  words = content.split()

  #Reverse the words in the file
  reversed_words = [word[::-1] for word in words] #to iterate through the list of words and reverse the characters of each one individually.
  reversed_content =" ".join(reversed_words)

  #We write the content in expected.txt
  with open(output_file, "w") as outfile:
      outfile.write(reversed_content)

  print(f"The file '{output_file}' was edited!")

reverse_file(input_file, output_file)


