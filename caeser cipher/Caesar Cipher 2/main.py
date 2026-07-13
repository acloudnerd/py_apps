alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# encrypt(original_text=text, shift_amount=shift)
#
# def decrypt(original_text, shift_amount):
#     decipher_text = ""
#     for letter in original_text:
#         back_shifted_position = alphabet.index(letter) - shift_amount
#         back_shifted_position %= len(alphabet)
#         decipher_text += alphabet[back_shifted_position]
#     print(f"Here's your decoded result:  {decipher_text}")
#
# decrypt(original_text=text, shift_amount=shift)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shift_direction = 1 if encode_or_decode == "encode" else -1
            shifted_position = alphabet.index(letter) + shift_amount * shift_direction
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"The result of the {encode_or_decode}d string is {output_text}")

caesar(text, shift, direction)