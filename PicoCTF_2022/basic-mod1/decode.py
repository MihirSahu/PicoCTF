import string


message = input("Message: ")
message = message.split()
alphabet = list(string.ascii_lowercase)
numbers = list(range(0, 11))

for idx, code in enumerate(message):
    message[idx] = int(message[idx]) % 37

    if ((message[idx] >= 0) and (message[idx] <= 25)):
        message[idx] = alphabet[message[idx]]
    elif ((message[idx] >= 26) and (message[idx] <=35)):
        message[idx] = numbers[message[idx] - 26]
    elif (message[idx == 36]):
        message[idx] = '_'

    message[idx] = str(message[idx])

print("".join(message))
