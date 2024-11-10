import hashlib


def check_hash(hash: str, words: list):
    for check in words:
        if hashlib.new("md5", check.encode()).hexdigest() == hash:
            print(check)



text = [x.strip() for x in open("C:/Users/pogro/Downloads/words.txt", "r")]
hash = "8bf7f3c31cb4b455397f1ca228ca5597"
check_hash(hash, text)