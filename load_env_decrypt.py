# load_env_decrypt.py
from cryptography.fernet import Fernet
import base64
import hashlib
import os
from dotenv import load_dotenv
from io import StringIO

password = "@Killer0575"

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Leer archivo cifrado
with open(".env_wallet_madre.enc", "rb") as file:
    encrypted_data = file.read()

fernet = Fernet(generate_key(password))
decrypted_data = fernet.decrypt(encrypted_data).decode()

# Cargar variables de entorno en memoria
load_dotenv(stream=StringIO(decrypted_data))

print("✅ Variables de entorno cargadas en memoria de forma segura.")
