import pickle

from AesEverywhere import aes256


class Secret:

    def __init__(self, key: str=''):
        # A 256 bit (32 byte) key
        if type(key) != type(''):
            raise RuntimeError('The key must be a string.')
        if len(key) > 32:
            raise RuntimeError('The key cannot contain more than 32 characters.')
        self.__key = key
        # Less than 32 characters complement 0.
        for i in range(32 - len(key)):
            self.__key += '0'

    def encrypt(self, obj) -> bytes:
        '''
            Encrypt Python objects using AES.
                obj -- Most Python objects.
        '''
        obj_bin = pickle.dumps(obj) # Convert Python objects to binary.
        obj_bin_str = str(obj_bin)
        ciphertext = aes256.encrypt(obj_bin_str, self.__key)
        return ciphertext

    def decrypt(self, ciphertext: bytes):
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