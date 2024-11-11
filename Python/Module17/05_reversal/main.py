def perevorot(strr: str):
    hi = []
    for i in range(len(strr)):
        if strr[i] == "h":
            hi.append(i)
    hi = sorted(hi)
    print("Развёрнутая последовательность между первым и последним h:", strr[max(hi): min(hi): -1])


strok = input("Введите строку: ")
perevorot(strok)