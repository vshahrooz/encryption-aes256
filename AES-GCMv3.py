import os
import getpass
import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHUNK_SIZE = 64 * 1024
ITERATIONS = 100000

def resolve_path(path):
    return path if os.path.isabs(path) else os.path.join(BASE_DIR, path)

def derive_key_from_password(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS, 32)

def get_password_key(encrypting=True):
    if encrypting:
        password = getpass.getpass("Enter password: ")
        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            exit()
        salt = get_random_bytes(16)
    else:
        password = getpass.getpass("Enter password: ")
        salt_hex = input("Enter salt (Hex): ").strip()
        try:
            salt = binascii.unhexlify(salt_hex)
            if len(salt) != 16:
                raise ValueError
        except:
            print("❌ Invalid salt format.")
            exit()
    key = derive_key_from_password(password, salt)
    return key, salt

def encrypt_file(file_path, key, salt):
    output_path = file_path + ".crypt"
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

    with open(file_path, "rb") as fin, open(output_path, "wb") as fout:
        fout.write(iv)  
        while chunk := fin.read(CHUNK_SIZE):
            ciphertext = cipher.encrypt(chunk)
            fout.write(ciphertext)
        fout.write(cipher.digest())  

    print(f"\n✅ File encrypted successfully: {output_path}")
    print(f"🔐 Salt (Hex) — Save this safely: {binascii.hexlify(salt).decode()}")

def decrypt_file(file_path, key):
    if not file_path.endswith(".crypt"):
        print("Invalid encrypted file (must end with .crypt)")
        exit()

    output_path = file_path[:-6]

    with open(file_path, "rb") as fin:
        iv = fin.read(12)
        file_size = os.path.getsize(file_path)
        tag_size = 16
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv)

        with open(output_path, "wb") as fout:
            while fin.tell() < file_size - tag_size:
                chunk_size = min(CHUNK_SIZE, file_size - tag_size - fin.tell())
                chunk = fin.read(chunk_size)
                fout.write(cipher.decrypt(chunk))
            tag = fin.read(tag_size)
            try:
                cipher.verify(tag)
            except ValueError:
                print("❌ Incorrect password or corrupted file.")
                os.remove(output_path)
                exit()

    print(f"\n✅ File decrypted successfully: {output_path}")

# --- Main ---
print("Do you want to:")
print("1. Encrypt a file")
print("2. Decrypt a file")

mode = input("Choice (1/2): ").strip()
encrypting = mode == "1"

file_path_input = input("Enter file name or full path: ").strip()
file_path = resolve_path(file_path_input)

if not os.path.isfile(file_path):
    print("❌ File not found:", file_path)
    exit()

key, salt = get_password_key(encrypting)

if encrypting:
    encrypt_file(file_path, key, salt)
else:
    decrypt_file(file_path, key)
