# obj_encrypt

[Chinese Version](https://github.com/Cyberbolt/obj_encrypt/blob/main/README_CHN.md)

obj-encrypt is an encryption library based on the AES-256 algorithm. It uses Python objects as the basic unit, which can convert objects into binary ciphertext and support decryption. Objects encrypted with obj-encrypt support TCP communication, database storage, and more.


### Installation

Recommended Environment: Python 3+

1. Enter the command window, create a virtual environment, and enter the following commands in turn

Linux and macOS:


```python
python3 -m venv venv # Create a virtual environment.
. venv/bin/activate # Activate the virtual environment.
```

Windows:


```python
python -m venv venv # Create a virtual environment.
venv\Scripts\activate # Activate the virtual environment.
```

2. Install obj-encrypt, enter in turn


```python
pip install --upgrade pip
pip install obj-encrypt
```

### Use

```
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
```

Output

```
b'U2FsdGVkX18IANYgINODlF8BjkxI3AaKJ/+10Iexgh65qyEKFY21HK5LSjiTuy37arjYAuIQQls+amqCdEdVdy0V1E6xECJXOFBb0kfIzQuxOimOaFFVvtq4IntjJNdCHLiTwuExVfwAW7CjqaD554B71IoT0o9xqrFch3N0vtq+UP0uXyMmMCsvu8zY7vrCuw9qM+kOW2VWsC2c2ePDnofvakchgDW9bGF8fTC3prE+TPksoJ4l6ERCjjRid54gP6+HmzB+TwOVSGaj+4VIdm1g7qv591tBU1U6Lxm83Hk='   <class 'bytes'>
{'author': 'Cyberbolt', 'personal_website': 'https://www.cyberlight.xyz/', 'time': '2022-02-10'}
```

In addition to Python dictionaries, you can encrypt your own objects, and the encrypted binary can be stored in a database or used for TCP communication.

If this module was helpful to you, I hope to receive your GitHub Star! Thank you so much!

[GitHub](https://github.com/Cyberbolt/obj_encrypt)

[CyberLight](https://www.cyberlight.xyz/)