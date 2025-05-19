# encryption-aes256
File Encryption and Decryption Script Using AES-GCM with Password-Derived Key

This Python script allows you to securely encrypt and decrypt files using AES encryption in Galois/Counter Mode (GCM). It derives a strong 256-bit encryption key from a user-provided password using PBKDF2 with SHA-256 and a random 16-byte salt.

Key Features:

Password-Based Key Derivation: The encryption key is generated from a password and a 16-byte salt via PBKDF2 with 100,000 iterations, ensuring resistance against brute-force attacks.

AES-GCM Encryption: Uses AES in GCM mode, which provides both confidentiality and data integrity through authentication tags.

Random IV and Salt: For each encryption, a new random 12-byte Initialization Vector (IV) and 16-byte salt are generated. The IV is stored in the encrypted file header; the salt is displayed to the user and must be provided during decryption.

Manual Salt Input on Decryption: During decryption, the user must enter the correct salt in hexadecimal form, adding an extra layer of security by not storing the salt within the encrypted file.

Chunked File Processing: Handles files in chunks (64 KB) to support large files efficiently without consuming excessive memory.

User-Friendly Prompts: Prompts users to enter and confirm passwords during encryption, ensuring the password is entered correctly. On decryption, it requests the password and the salt.

Usage Workflow:

Choose whether to encrypt or decrypt a file.

Provide the file path.

Enter and confirm the password (for encryption).

The script derives the key and encrypts or decrypts the file accordingly.

For encryption, the salt is shown in hex format — save it securely as it is required for decryption.

For decryption, input the password and the salt exactly as saved to successfully recover the original file.

Security Notes:

The script relies on the secrecy of both the password and the salt. If either is lost or compromised, the data cannot be decrypted.

Using a random salt for each encryption strengthens the security by preventing attackers from using precomputed hash tables.

The salt is not stored inside the encrypted file, which means the user must manage it securely outside the file system.

