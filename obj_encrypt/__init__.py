import sys
import base64
import pickle

from Crypto.Cipher import AES
from Crypto import Random
from AesEverywhere import aes256


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
        self._salt = salt
        self._iterations = iterations

    def encrypt(self, content: bytes):
        '''
            SHA-256 encryption
        '''
        if type(content) != type(b'1'):
            raise RuntimeError('Content must be bytes.')
        dk = hashlib.pbkdf2_hmac('sha256', content, self._salt, self._iterations)
        return dk.hex()


class Secret:

    def __init__(self, key: str=''):
        # A 256 bit (32 byte) key
        if type(key) != type(''):
            raise RuntimeError('The key must be a string.')
        if len(key) > KEY_LEN:
            raise RuntimeError('The key cannot contain more than 32 characters.')
        
        self.__key = key
        # Less than 32 characters complement 0.
        for i in range(KEY_LEN - len(key)):
            self.__key += '0'
        
        # Used for SHA 256 signatures.
        key_bin = self.__key.encode()
        self.signature = Signature(salt=key_bin)
        self.__iv = self.signature.encrypt(key_bin)[:IV_LEN]

    def encrypt_old(self, obj) -> bytes:
        '''
            Encrypt Python objects using AES.
                obj -- Most Python objects.
        '''
        obj_bin = pickle.dumps(obj) # Convert Python objects to binary.
        obj_bin_str = str(obj_bin)
        ciphertext = aes256.encrypt(obj_bin_str, self.__key)
        return ciphertext

    def decrypt_old(self, ciphertext: bytes):
        '''
            AES decryption.
                ciphertext -- The ciphertext is encrypted by encrypt method.
            Return: Python object
        '''
        decrypted = aes256.decrypt(ciphertext, self.__key)
        # Concatenate the binary of a Python object.
        obj_bin_str_part = decrypted.decode()[2:-1]
        loc = locals()
        exec("obj_bin = b'''{}''' ".format(obj_bin_str_part))
        obj_bin = loc['obj_bin']
        # Convert the binary to a Python object.
        obj = pickle.loads(obj_bin)
        return obj

    def encrypt(self, obj) -> bytes:
        aes = AES.new(self.__key, AES.MODE_CBC, self.__iv)
        
        # Convert Python objects to binary.
        obj_bin = pickle.dumps(obj)
        # Get binary string.
        obj_str = obj_bin.hex()
        
        # The padding string size is a multiple of 16B.
        for i in range(16 - len(obj_str) % BLOCK_SIZE):
            obj_str += ' '

        ciphertext = aes.encrypt(obj_str)
        return ciphertext
    
    def decrypt(self, ciphertext: bytes):
        aes = AES.new(self.__key, AES.MODE_CBC, self.__iv)
        
        obj_str = aes.decrypt(ciphertext).decode()
        
        # Unpack the string padding.
        obj_str = obj_str.rstrip(' ')
        
        # Convert the string to its original binary.
        obj_bin = bytes.fromhex(obj_str)
        # Convert binary to Python object.
        obj = pickle.loads(obj_bin) 
        return obj
    

def pkcs7_padding(s):
    """
    Padding to blocksize according to PKCS #7
    calculates the number of missing chars to BLOCK_SIZE and pads with
    ord(number of missing chars)
    @see: http://www.di-mgt.com.au/cryptopad.html
    @param s: string Text to pad
    @type s: string
    @rtype: string
    """
    s_len = s.encode('utf-8')
    s = s + (BLOCK_SIZE - s_len % BLOCK_SIZE) * chr(BLOCK_SIZE - s_len % BLOCK_SIZE)
    return bytes(s, 'utf-8')

def pkcs7_trimming(s):
    """
    Trimming according to PKCS #7
    @param s: string Text to unpad
    @type s: string
    @rtype: string
    """
    return s[0:-s[-1]]