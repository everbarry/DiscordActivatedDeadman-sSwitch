# Password hashing tool
import hashlib


def hashTool():
    pwd = input("Enter pwd: ")
# Available algorithms: 'sha224', 'sha3_512', 'sha512', 'shake_256', 'sha3_224', 'blake2s', 'blake2b', 'sha3_384', 'sha512_224', 'sha1', 'md5-sha1', 'md5', 'whirlpool', 'md4', 'sha256', 'sm3', 'sha3_256', 'ripemd160', 'sha384', 'sha512_256', 'shake_128'
    crypt = hashlib.sha512()                                                             # Change hashing algorithm here
    crypt.update(pwd.encode("utf-8"))
    return crypt.hexdigest()


while True:
    print("Your password hashed is: ", hashTool())
