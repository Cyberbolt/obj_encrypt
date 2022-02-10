from obj_encrypt import Secret


def main():
    secret = Secret(key='0123456789') # 初始化 secret 实例，密钥最大不能超过 32 个字符串
    # 构建 data 字典
    data = {
        'author': 'Cyberbolt',
        'personal_website': 'https://www.cyberlight.xyz/',
        'time': '2021-02-10'
    }
    ciphertext = secret.encrypt(data) # 将对象转为二进制密文，获取密文
    print(ciphertext, ' ', type(ciphertext))
    data = secret.decrypt(ciphertext) # 解密密文为对象
    print(data)


if __name__ == '__main__':
    main()