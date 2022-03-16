import string


message = input("Message: ")
message = message.split()
alphabet = list(string.ascii_lowercase)
numbers = list(range(0, 10))


def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

for idx, code in enumerate(message):
    message[idx] = modInverse(int(message[idx]), 41)

    if ((message[idx] >= 1) and (message[idx] <= 26)):
        message[idx] = alphabet[message[idx] - 1]
    elif ((message[idx] >= 27) and (message[idx] <=36)):
        message[idx] = numbers[message[idx] - 27]
    elif (message[idx == 37]):
        message[idx] = '_'

    message[idx] = str(message[idx])

print("".join(message))
