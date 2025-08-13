# encrypt_env.py
from cryptography.fernet import Fernet
import base64
import hashlib

# Clave segura proporcionada
password = "@Killer0575"

# Función para derivar clave de 32 bytes desde contraseña
def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# Leer .env original
with open(".env_wallet_madre", "rb") as file:
    data = file.read()

# Cifrar
fernet = Fernet(generate_key(password))
encrypted = fernet.encrypt(data)

# Guardar como archivo cifrado
with open(".env_wallet_madre.enc", "wb") as file:
    file.write(encrypted)

print("🔐 .env_wallet_madre ha sido cifrado correctamente como .env_wallet_madre.enc")
