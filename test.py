import time

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
    
    start1 = time.time()    
    ciphertext = secret.encrypt(data) # Convert the object to binary ciphertext and get the ciphertext.
    end1 = time.time()
    
    print(ciphertext, ' ', type(ciphertext))
    start2 = time.time()
    plaintext = secret.decrypt(ciphertext) # Decrypt ciphertext as object.
    end2 = time.time()
    print(plaintext)
    print()
    print('encrypt time: {}'.format(end1 - start1))
    print('decrypt time: {}'.format(end2 - start2))
    print('all time: {}'.format(end1 - start1 + end2 - start2))
    

if __name__ == '__main__':
    main()