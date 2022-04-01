# obj_encrypt

obj-encrypt 是基于 AES-256-CBC 算法的加密库，它以 Python 对象为基本单元，可以将对象转为二进制密文，并支持解密。经 obj-encrypt 加密的对象支持 TCP 通信、数据库存储等。


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
    # 初始化 secret 实例，key 为 AES-256 密钥，最大不能超过 32 个字符串
    secret = Secret(key='0123456789')
    # 构建 data 字典
    data = {
        'author': 'Cyberbolt',
        'personal_website': 'https://www.cyberlight.xyz/',
        'time': '2022-02-10'
    }
    ciphertext = secret.encrypt(data) # 将对象转为二进制密文，获取密文
    print(ciphertext, ' ', type(ciphertext))
    plaintext = secret.decrypt(ciphertext) # 解密密文为对象
    print(plaintext)


if __name__ == '__main__':
    main()
```

输出内容

```
b'U2FsdGVkX18IANYgINODlF8BjkxI3AaKJ/+10Iexgh65qyEKFY21HK5LSjiTuy37arjYAuIQQls+amqCdEdVdy0V1E6xECJXOFBb0kfIzQuxOimOaFFVvtq4IntjJNdCHLiTwuExVfwAW7CjqaD554B71IoT0o9xqrFch3N0vtq+UP0uXyMmMCsvu8zY7vrCuw9qM+kOW2VWsC2c2ePDnofvakchgDW9bGF8fTC3prE+TPksoJ4l6ERCjjRid54gP6+HmzB+TwOVSGaj+4VIdm1g7qv591tBU1U6Lxm83Hk='   <class 'bytes'>
{'author': 'Cyberbolt', 'personal_website': 'https://www.cyberlight.xyz/', 'time': '2022-02-10'}
```

除了字典，你可以加密自己的对象，加密后的二进制可以存入数据库，也可以用于 TCP 通信。

如果该模块对你有帮助，希望收到你的 GitHub Star！非常感谢！

[GitHub 地址](https://github.com/Cyberbolt/obj_encrypt)

[电光笔记官网](https://www.cyberlight.xyz/)