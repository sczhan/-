import os


def encrypt(src: str, dest: str, key: int):
    if not os.access(src, os.F_OK) or os.access(dest, os.F_OK):
        return False
    fr = open(src, "rb")
    fw = open(dest, "wb")
    while True:
        new_bts = fr.read(4096)
        if len(new_bts) == 0:
            break
        bts = [b ^ key for b in new_bts]
        fw.write(bytes(bts))
    fr.close(), fw.close()
    return True


if __name__ == '__main__':
    a = encrypt("18.txt", "13.txt", 15)
    print(a)
