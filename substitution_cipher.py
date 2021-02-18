# caesar cipher, shift 13
plaintext = 'thequickbrownfoxjumpsoverthelazydog'
plaintext_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = []
ciphertext = ""
ciphertext_list = []

for character in plaintext:
    plaintext_list.append(character)

for character in alphabet:
    alphabet_list.append(character)

for character in plaintext_list:
    index = alphabet_list.index(character)
    if index <= 12:
        newindex = index + 13
    if index >= 13:
        newindex = index - 13
    newcharacter = alphabet_list[newindex]
    ciphertext_list.append(newcharacter)
ciphertext = "".join(ciphertext_list)

# break caesar cipher
ciphertext = 'dzeevjfkrlezkvuwffksrcctcls'
ciphertext_list = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = []

for character in ciphertext:
    ciphertext_list.append(character)

for character in alphabet:
    alphabet_list.append(character)

for attempt in range(25):
    plaintext = ''
    plaintext_list = []
    for character in ciphertext_list:
        index = alphabet_list.index(character)
        newindex = (index + attempt) % 26
        newcharacter = alphabet_list[newindex]
        plaintext_list.append(newcharacter)
    plaintext = "".join(plaintext_list)
    print(plaintext)

# encrypt message
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'
ciphertext = ""

ciphertext_list = []
alphabet_list = []
plaintext_list = []
key_list = []

for character in plaintext:
    plaintext_list.append(character)

for character in alphabet:
    alphabet_list.append(character)

for character in key:
    key_list.append(character)

for attempt in range(25):
    ciphertext = ''
    ciphertext_list = []
    for character in plaintext_list:
        index = alphabet_list.index(character)
        newindex = (index + attempt) % 27
        newcharacter = key[newindex]
        ciphertext_list.append(newcharacter)
    ciphertext = "".join(ciphertext_list)
    print(ciphertext)

# decrypt message
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'
plaintext = ''

ciphertext_list = []
alphabet_list = []
plaintext_list = []
key_list = []

for character in ciphertext:
    ciphertext_list.append(character)

for character in alphabet:
    alphabet_list.append(character)

for character in key:
    key_list.append(character)

for attempt in range(25):
    plaintext = ''
    plaintext_list = []
    for character in ciphertext_list:
        index = key_list.index(character)
        newindex = (index + attempt) % 27
        newcharacter = alphabet[newindex]
        plaintext_list.append(newcharacter)
    plaintext = "".join(plaintext_list)
    print(plaintext)
# ask user to enter key and message to encrypt
# your code here
alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = input('Please enter your key to encrypt your message.')
plaintext = input('Please enter the message you would like to encrypt.')
ciphertext = ""

ciphertext_list = []
alphabet_list = []
plaintext_list = []
key_list = []

for character in plaintext:
    plaintext_list.append(character)

for character in alphabet:
    alphabet_list.append(character)

for character in key:
    key_list.append(character)

for attempt in range(25):
    ciphertext = ''
    ciphertext_list = []
    for character in plaintext_list:
        index = alphabet_list.index(character)
        newindex = (index + attempt) % 27
        newcharacter = key[newindex]
        ciphertext_list.append(newcharacter)
    ciphertext = "".join(ciphertext_list)
    print(ciphertext)
