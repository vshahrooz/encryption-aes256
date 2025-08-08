# FileEncryptor

FileEncryptor is a simple yet secure Python tool for encrypting and decrypting files using AES-GCM and password-based key derivation. It is designed for local file protection and easy usage from the command line.

## Features

- Encrypt files using AES in GCM mode (256-bit)
- Random salt and IV generation for each encryption
- Password-based key derivation using PBKDF2-HMAC-SHA256
- Hexadecimal salt output to be saved for decryption
- Integrity verification using GCM authentication tag

## Usage

### 1. Install dependencies

```bash
pip install pycryptodome
```

### 2. Run the program

```bash
python file_encryptor.py
```

### 3. To encrypt a file:

1. Choose option 1 (Encrypt)
2. Enter the file path
3. Enter and confirm your password
4. The encrypted file will be saved as `filename.crypt`
5. A unique salt (Hex) will be displayed — **save it securely**

### 4. To decrypt a file:

1. Choose option 2 (Decrypt)
2. Enter the path of the `.crypt` file
3. Enter your password
4. Enter the previously saved salt (Hex)
5. The original file will be restored if password and salt match

## Security Notes

- Your password is never stored.
- A new random salt and IV are used each time.
- Integrity is checked using AES-GCM tag verification.

## Warning

- Losing the salt makes decryption impossible.
- Incorrect passwords will cause decryption to fail.

##  Author

- Email: v.shahrooz@gmail.com

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
