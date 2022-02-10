# obj_encrypt

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
    secret = Secret(key='0123456789') # Initialize the secret instance, the key cannot exceed 32 strings.
    # Build the data dictionary.
    data = {
        'author': 'Cyberbolt',
        'personal_website': 'https://www.cyberlight.xyz/',
        'time': '2021-02-10'
    }
    ciphertext = secret.encrypt(data) # Convert the object to binary ciphertext and get the ciphertext.
    print(ciphertext, ' ', type(ciphertext))
    data = secret.decrypt(ciphertext) # Decrypt ciphertext as object.
    print(data)


if __name__ == '__main__':
    main()
```

Output

```
b'U2FsdGVkX1/WxuK0iagq5jEbJsiIGvuNZieWehVYj7i+M66y06I1WcD7gBpPKniDhIkmSuVepFdMEisT8/+HqrWHHNwoY+waDERTes+7dGHvMBc4FcuTFjMzVoQZUE0SqFMi/ORhKcpCGgSUZo/gdNBPh0nNsRZ5ZQrKbt47aw6tSOEEXHwXEr20uHjqT7wx1uvsXnGbx1l91BNhEYrAIxhaJX0YTfGOgqVgCMc9k4xxSNEoB9v19873rryT5TnTXijNeA+FRtZKN5Mt9WUFMuBYCK5xWhXKv0BJOn8iGmw='   <class 'bytes'>
{'author': 'Cyberbolt', 'personal_website': 'https://www.cyberlight.xyz/', 'time': '2021-02-10'}
```

In addition to Python dictionaries, you can encrypt your own objects, and the encrypted binary can be stored in a database or used for TCP communication.