# encrypt / decrypt tool for aes password encrypted files

import pyAesCrypt

bufferSize = 64 * 1024          # Change buffer size here
password = 'decryptPassword'   # put your password to decrypt file in here
filePath = 'file path'        

# pyAesCrypt.encryptFile(filePath, (filePath+'.aes'), password, bufferSize)   # one line to encrypt
# pyAesCrypt.decryptFile(filePath, "decrypted.txt", password, bufferSize)    # one line to decrypt




def encrypt(password, filePath):
    global bufferSize
    pyAesCrypt.encryptFile(filePath, (filePath+'.aes'), password, bufferSize)


def decrypt(password,filePath):
    global bufferSize
    pyAesCrypt.decryptFile(filePath, "decrypted.txt", password, bufferSize)


def main():
    password = input("Insert decryptPassword: ")
    filePath = input("Enter file path: ")
    mode = input("Type 'e' for encrypt \nType 'd' for decrypt: ")
    if mode == 'e':
    	encrypt(password, filePath)
    	print("File encrypted")
    elif mode == 'd':
        decrypt(password, filePath)
        print("File decrypted")
    else:
    	print("Wrong user input")
    	main()

main() 