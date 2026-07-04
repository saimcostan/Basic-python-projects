import random
import string

#making a string of all possible string characters using the string builtin module
chars=" "+string.punctuation+string.ascii_letters+string.digits

#creating a list of all possible string values with the help of the char string
chars=list(chars)

#duplicating the list
key=chars.copy()

#rearranging the list so that each character has a corresponding encrypted character
random.shuffle(key)

#taking user input about the text they want to encrypt and initialising the encrypted string
plain_text=input("Enter the message you want to encrypt: ")
cypher_text=""

#looping through each element of the plain text and adding the corresponding encrypted character in the cypher text
for letter in plain_text:
    index=chars.index(letter)
    cypher_text=cypher_text+key[index]

print(f"Encrypted message: {cypher_text}")

#asking user to input the text they want to decrypt and intialising a new plain text
new_cypher_text=input("Enter the message you want to decrypt: ")
new_plain_text=""

#looping through each element of the cypher text and adding the corresponding decrypted character in the new plain text
for letter in new_cypher_text:
    index=key.index(letter)
    new_plain_text=new_plain_text+chars[index]

print(f"Decrypted message: {new_plain_text}")


