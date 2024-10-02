# -*- coding: utf-8 -*-
"""Affine Chiper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_0V1Ghbdip9sIr6BcEeQzR6BqeoUYFyB
"""

# Commented out IPython magic to ensure Python compatibility.
# Implementasi Algoritma Affine Cipher

#GCD(Greatest Common Divisor)
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

#invers modulo
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# Fungsi Enkripsi Affine Cipher
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


#fungsi Deskripsi Affine Chiper
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
#                          % 26) + ord('A')) for c in cipher])


# main
def main():
    # Input teks
    text = input("Masukkan Teks: ")

    # Input kunci a dan b
    a = int(input("Masukkan Kunci Pertama (a): "))
    b = int(input("Masukkan Kunci Kedua (b): "))
    key = [a, b]

    # memanggil fungsi enskripsi
    affine_encrypted_text = affine_encrypt(text, key)

    print('Teks Enskripsi: {}'.format(affine_encrypted_text))

    # memanggil fungsi deskripsi
    affine_decrypted_text = affine_decrypt(affine_encrypted_text, key)
    print('Teks Deskripsi: {}'.format(affine_decrypted_text))


if __name__ == '__main__':
    main()