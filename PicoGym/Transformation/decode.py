# Encoded text: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽
# Code used to encode: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Undo the encoding process
'''
28777 = ord(flag[0]) << 8 + ord(flag[1])
ord('p') << 8 + ord('i')
= 112 << 8 + 105
= 28672 + 105 = 288777
'''

with open("enc", "r") as file:
    input = file.read()
    encoded_message = []
    output = []

    for idx, i in enumerate(input):
        encoded_message.append(ord(i))

    for i in encoded_message:
        for j in range(0, 128):
            for k in range(0, 128):
                if i == (ord(chr((ord(chr(j)) << 8) + ord(chr(k))))):
                    #print(chr(j), chr(k))
                    output.append(chr(j))
                    output.append(chr(k))


    #print(encoded_message)
    print(''.join(output))
