def alph(strr: str):
    print("1:", strr)
    print("2:", strr[::-1])
    print("3:", strr[::2])
    print("4:", strr[1::2])
    print("5:", strr[:1:])
    print("6:", strr[-1:-2:-1])
    print("7:", strr[3:4:])
    print("8:", strr[-3::])
    print("9:", strr[3:5:])
    print("10:", strr[4:2:-1])


alphabet = "abcdefg"
alph(alphabet)