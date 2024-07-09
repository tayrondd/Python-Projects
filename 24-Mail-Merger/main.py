# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode="r") as format_file:
    f = format_file.read()

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    name_list = names_file.readlines()
    print(name_list)

for name in name_list:
    name = name.strip("\n")

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(f.replace("[name]", name))
