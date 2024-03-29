class RC4:
    def __init__(self):
        self.init_S = list(range(256))

    def keystream(self, key):
        self.S = self.init_S.copy()
        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % len(key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            k = self.S[(self.S[i] + self.S[j]) % 256]
            yield k

    def encrypt(self, key, plaintext):
        key = [ord(c) for c in key]
        plaintext = [ord(c) for c in plaintext]
        keystream_generator = self.keystream(key)
        return bytes([byte ^ next(keystream_generator) for byte in plaintext])

    def decrypt(self, key, ciphertext):
        key = [ord(c) for c in key]
        ciphertext = list(ciphertext)
        keystream_generator = self.keystream(key)
        return bytes([byte ^ next(keystream_generator) for byte in ciphertext]).decode('UTF-8')


if __name__ == '__main__':
    key = "KeyOfRC4"
    plaintext = "ILoveCrypto"
    rc4 = RC4()
    ciphertext = rc4.encrypt(key, plaintext)
    print("Encrypted:", ciphertext)
    decrypted_text = rc4.decrypt(key, ciphertext)
    print("Decrypted:", decrypted_text)