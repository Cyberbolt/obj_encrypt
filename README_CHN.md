# obj_encrypt

obj-encrypt 是基于 AES-256 算法的加密库，它以 Python 对象为基本单元，可以将对象转为二进制密文，并支持解密。经 obj-encrypt 加密的对象支持 TCP 通信、数据库存储等。


### 安装方法

推荐环境: Python 3+ 

1.进入命令窗口，创建虚拟环境，依次输入以下命令

Linux 和 macOS:


```python
python3 -m venv venv # 创建虚拟环境
. venv/bin/activate # 激活虚拟环境
```

Windows:


```python
python -m venv venv # 创建虚拟环境
venv\Scripts\activate # 激活虚拟环境
```

2.安装 obj-encrypt，依次输入


```python
pip install --upgrade pip
pip install obj-encrypt
```

### 使用方法

```
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
```

输出内容

```
b'U2FsdGVkX1/WxuK0iagq5jEbJsiIGvuNZieWehVYj7i+M66y06I1WcD7gBpPKniDhIkmSuVepFdMEisT8/+HqrWHHNwoY+waDERTes+7dGHvMBc4FcuTFjMzVoQZUE0SqFMi/ORhKcpCGgSUZo/gdNBPh0nNsRZ5ZQrKbt47aw6tSOEEXHwXEr20uHjqT7wx1uvsXnGbx1l91BNhEYrAIxhaJX0YTfGOgqVgCMc9k4xxSNEoB9v19873rryT5TnTXijNeA+FRtZKN5Mt9WUFMuBYCK5xWhXKv0BJOn8iGmw='   <class 'bytes'>
{'author': 'Cyberbolt', 'personal_website': 'https://www.cyberlight.xyz/', 'time': '2021-02-10'}
```

除了字典，你可以加密自己的对象，加密后的二进制可以存入数据库，也可以用于 TCP 通信。

[电光笔记官网](https://www.cyberlight.xyz/)