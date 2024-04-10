def freqAlphabets(s: str) -> str:
    ptr = 0
    word = ""

    while ptr < len(s):
        if ptr + 2 < len(s) and s[ptr + 2] == '#':
            # print(s[ptr:ptr+2])
            word += chr(96 + int(s[ptr:ptr+2]))
            ptr += 3
        else:
            # print(s[ptr])
            word += chr(96 + int(s[ptr]))
            ptr += 1

    return word


print(freqAlphabets("1326#"))
