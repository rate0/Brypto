import base64
import pyfiglet

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt_caesar(ciphertext):
    decrypted_texts = []

    for key in range(len(alphabet)):
        plaintext = ''

        for symbol in ciphertext:
            if symbol in alphabet:
                num = alphabet.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alphabet)

                plaintext = plaintext + alphabet[num]
            else:
                plaintext = plaintext + symbol
        decrypted_texts.append(plaintext)
    return decrypted_texts


def decrypt_atbash(ciphertext):
    reversed_alphabet = alphabet[::-1]
    plaintext = ''

    for symbol in ciphertext:
        if symbol in alphabet:
            index = alphabet.find(symbol)
            plaintext = plaintext + reversed_alphabet[index]

        else:
            plaintext = plaintext + symbol

    return plaintext

def decrypt_base64(ciphertext):
    decoded_bytes = base64.b64decode(ciphertext)
    plaintext = decoded_bytes.decode("utf-8")
    return plaintext

def decrypt_rot13(ciphertext):
    rot13 = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    plaintext = str.translate(ciphertext, rot13)
    return plaintext


def decrypt_cipher(ciphertext):
    caesar_decryptions = decrypt_caesar(ciphertext)
    atbash_decryption = decrypt_atbash(ciphertext)
    base64_decryption = decrypt_base64(ciphertext)
    rot13_decryption = decrypt_rot13(ciphertext)

    print("Caesar Cipher Decryptions:")
    for i, text in enumerate(caesar_decryptions):
        print(f"Key #{i}: {text}")

    print("\nAtbash Cipher Decryption:")
    print(atbash_decryption)

    print("\nBase64 Decryption:")
    print(base64_decryption)

    print("\nROT13 Decryption:")
    print(rot13_decryption)

text = "Brypto"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
print("Let's solve crypto with bruteforce!")
ciphertext = input("Enter your ciphertext: ")
decrypt_cipher(ciphertext)