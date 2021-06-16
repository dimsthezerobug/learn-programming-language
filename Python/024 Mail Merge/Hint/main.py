with open("./Input/Letters/starting_letter.txt") as text:
    print(text.readlines(2))  # memasukan 2 baris text ke dalam sebuah list

with open("./Input/Letters/starting_letter.txt", mode="w") as text:
    