#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as template:
    letter = template.read()

with open("./Input/Names/invited_names.txt") as names:
    all_names = names.read().split("\n")

for name in all_names:
    letter = letter.replace("[name]", f"{name}")
    name_file = f"letter_for_{name}.txt"
    with open(f"./Output/ReadyToSend/{name_file}", mode="w") as new_letter:
        new_letter.write(letter)
    letter = letter.replace(f"{name}", "[name]")

print("Done")

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
