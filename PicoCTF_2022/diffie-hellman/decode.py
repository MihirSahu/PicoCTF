import string


alphanumeric = list(string.ascii_uppercase + str(string.digits))
key = int(input("Enter the key: "))
message = list(input("Enter the message: "))

for idx, character in enumerate(message):
    if (character == "_"):
        continue
    else:
        message[idx] = alphanumeric[(alphanumeric.index(character) - key) % len(alphanumeric)]

print("".join(message))
