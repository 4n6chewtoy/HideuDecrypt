####
# A python script designed to decrypt the database 'HideU.db' for the Android application com.calculator.hideu
# 'HideU: Calculator Lock. 
###


# Import required modules
import hashlib
from pbkdf2 import PBKDF2
import sys

# Hardcoded passphrase as hex (needed for key derivation)
hex_passphrase = "92e418a05804d6fcaa5e0a0f3729b4ee"

# Convert the hex passphrase to raw bytes
passphrase_bytes = bytes.fromhex(hex_passphrase)

# salt - first 16 bytes of encrypted DB
salt = bytes.fromhex(sys.argv[1])

# Params for Sql 4
iterations = 256000
key_length = 64  # 64 bytes for PBKDF2-HMAC-SHA512 output

# Derive the key using PBKDF2-HMAC-SHA512
derived_key = hashlib.pbkdf2_hmac('sha512', passphrase_bytes, salt, iterations, dklen=key_length)

# Use the first 32 bytes (AES-256 key) for encryption
encryption_key = derived_key[:32]

# Output the derived key for debugging purposes
print(f"Derived Key (AES-256): {encryption_key.hex()}")
