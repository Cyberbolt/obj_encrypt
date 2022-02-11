from obj_encrypt import Secret


def main():
    # Initialize the secret instance, the key is an AES-256 key, and the maximum size cannot exceed 32 strings.
    secret = Secret(key='0123456789')
    # build the data dictionary
    data = {
        'author': 'Cyberbolt',
        'personal_website': 'https://www.cyberlight.xyz/',
        'time': '2022-02-10'
    }
    ciphertext = secret.encrypt(data) # Convert the object to binary ciphertext and get the ciphertext.
    print(ciphertext, ' ', type(ciphertext))
    plaintext = secret.decrypt(ciphertext) # Decrypt ciphertext as object.
    print(plaintext)


if __name__ == '__main__':
    main()