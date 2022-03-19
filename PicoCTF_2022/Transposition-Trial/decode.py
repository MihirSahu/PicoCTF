message = list(input("Enter the message: "))
i = 0

while (i < len(message)):
    temp1 = message[i]
    temp2 = message[i + 1]
    temp3 = message[i + 2]

    message[i] = temp3
    message[i + 1] = temp1
    message[i + 2] = temp2

    i = i + 3

print("".join(message))
