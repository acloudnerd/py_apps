# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import csv

with open("nato_phonetic_alphabet.csv", newline="") as csv_file:
    data = csv.DictReader(csv_file)
    #TODO 1. Create a dictionary in this format:
    phonetic_dict = {row["letter"]: row["code"] for row in data}

print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters allowed.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()