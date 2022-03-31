import pickle

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


import hashlib


BLOCK_SIZE = 16
KEY_LEN = 32
IV_LEN = 16


class Signature:
    '''
        This class is based on the SHA-256 algorithm for signing and checking data integrity.
    '''

    def __init__(self, salt: bytes, iterations: int=1):
        '''
            salt -- SHA-256 salt\n
            iterations -- The number of iterations of the SHA-256 algorithm.
        '''
        if type(salt) != type(b'1'):
            raise RuntimeError('Salt must be bytes.')
        self.salt = salt
        self.iterations = iterations

    def encrypt(self, content: bytes):
        '''
            SHA-256 encryption
        '''
        if type(content) != type(b'1'):
            raise RuntimeError('Content must be bytes.')
        dk = hashlib.pbkdf2_hmac('sha256', content, self.salt, self.iterations)
        return dk.hex()


class Secret:

    def __init__(self, key: str=''):
        # A 256 bit (32 byte) key
        if type(key) != type(''):
            raise RuntimeError('The key must be a string.')
        if len(key) > KEY_LEN:
            raise RuntimeError('The key cannot contain more than 32 characters.')
        
        self.key = key
        # Less than 32 characters complement 0.
        for i in range(KEY_LEN - len(key)):
            self.key += '0'
        
        # Used for SHA 256 signatures.
        self.key_bin = self.key.encode()
        self.signature = Signature(salt=self.key_bin)
        self.__iv = self.signature.encrypt(self.key_bin)[:IV_LEN]

    def encrypt(self, obj) -> bytes:
        aes = AES.new(self.key_bin, AES.MODE_CBC, self.__iv.encode())
        
        # Convert Python objects to binary.
        obj_bin = pickle.dumps(obj)
        obj_bin = pad(obj_bin, BLOCK_SIZE)

        ciphertext = aes.encrypt(obj_bin)
        return ciphertext
    
    def decrypt(self, ciphertext: bytes):
        try:
            aes = AES.new(self.key_bin, AES.MODE_CBC, self.__iv.encode())
            obj_bin = aes.decrypt(ciphertext)
            obj_bin = unpad(obj_bin, BLOCK_SIZE)
        except (ValueError, KeyError):
            raise KeyError('Incorrect key.')
        
        # Convert binary to Python object.
        obj = pickle.loads(obj_bin) 
        return obj
