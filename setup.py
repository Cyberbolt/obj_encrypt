import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obj-encrypt",
    version="0.1.3",
    author="Cyberbolt",
    author_email="dtconlyone@gmail.com",
    description="obj-encrypt is an encryption library based on the AES-256 algorithm. It uses Python objects as the basic unit, which can convert objects into binary ciphertext and support decryption. Objects encrypted with obj-encrypt support TCP communication, database storage, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aes-everywhere>=1.2.10',
        'pycryptodomex>=3.13.0'
    ]    
)