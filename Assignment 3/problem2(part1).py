def encrypt(plaintext, pad):
    ciphertext = ''
    c_prev = 0
    for i in range(len(plaintext)):
        m = ord(plaintext[i])
        c = m ^ ((pad[i] + c_prev) % 256)
        ciphertext += chr(c)
        c_prev = c
    return ciphertext

def decrypt(ciphertext, pad):
    plaintext = ''
    c_prev = 0
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        m = c ^ ((pad[i] + c_prev) % 256)
        plaintext += chr(m)
        c_prev = c
    return plaintext

plaintext = "HelloWorld"
pad = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A]
ciphertext = encrypt(plaintext, pad)
print(ciphertext)
deciphertext = decrypt(ciphertext, pad)
print(deciphertext)