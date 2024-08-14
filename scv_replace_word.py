input_file = "data.txt"
output_file = "censored_data.txt"


with open(input_file, "r") as file:
   contents = file.read()
words = contents.split()


with open(output_file, "w") as file:
   
   for word in words:
       # Check if the word has exactly four letters
        if len(word) == 4:
                # Replace the four-letter word with ""
                censored_word = "****"
                file.write(censored_word)
        else:
            # Write the original word to the output file
            file.write(word)
        file.write(' ')