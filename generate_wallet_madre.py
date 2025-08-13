from eth_account import Account
import json
import os
from datetime import datetime

def generate_kay_mother_wallet():
    """
    Genera la wallet madre de KAY para el sistema de automatización
    Esta será la wallet central que recibirá todos los fondos del enjambre
    """
    
    print("KAY CORP - Generando Wallet Madre")
    print("=" * 50)
    
    # Crear nueva wallet
    wallet = Account.create()
    
    # Datos de la wallet
    wallet_data = {
        "address": wallet.address,
        "private_key": wallet.key.hex(),
        "network": "BSC",
        "wallet_type": "KAY_MADRE",
        "created_at": datetime.now().isoformat(),
        "description": "Wallet central del enjambre KAY para recibir fondos de bounty hunting",
        "security_level": "CRITICAL",
        "backup_required": True
    }
    
    # Guardar wallet_madre.json
    with open("wallet_madre.json", "w") as f:
        json.dump(wallet_data, f, indent=4)
    
    # Guardar .env_wallet_madre
    with open(".env_wallet_madre", "w") as f:
        f.write(f"# KAY CORP - Wallet Madre Configuration\n")
        f.write(f"# Generated: {datetime.now().isoformat()}\n")
        f.write(f"# ⚠️  CRITICAL SECURITY - PROTECT THESE KEYS\n\n")
        f.write(f"KAY_WALLET_ADDRESS={wallet.address}\n")
        f.write(f"KAY_WALLET_PRIVATE_KEY={wallet.key.hex()}\n")
        f.write(f"KAY_NETWORK=BSC\n")
        f.write(f"KAY_WALLET_TYPE=KAY_MADRE\n")
        f.write(f"KAY_CREATED_AT={datetime.now().isoformat()}\n")
    
    # Crear archivo de backup seguro
    backup_data = {
        "wallet_info": {
            "address": wallet.address,
            "network": "BSC",
            "type": "KAY_MADRE",
            "created": datetime.now().isoformat()
        },
        "import_instructions": {
            "metamask": "Importar como cuenta privada usando la clave privada",
            "trust_wallet": "Importar wallet usando la clave privada",
            "hardware_wallet": "Usar solo para recibir, nunca para firmar"
        },
        "security_warnings": [
            "NUNCA compartir la clave privada",
            "Hacer backup en USB offline",
            "Usar solo para recibir fondos del enjambre",
            "Mantener separada de wallets de trading"
        ]
    }
    
    with open("wallet_madre_backup.json", "w") as f:
        json.dump(backup_data, f, indent=4)
    
    print("✅ Wallet madre creada exitosamente!")
    print("=" * 50)
    print(f"Dirección: {wallet.address}")
    print(f"Red: BSC (Binance Smart Chain)")
    print(f"Tipo: KAY_MADRE (Wallet Central)")
    print(f"Creada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    print("\nArchivos generados:")
    print("• wallet_madre.json → Para importar en Metamask/Trust Wallet")
    print("• .env_wallet_madre → Para uso en scripts de KAY")
    print("• wallet_madre_backup.json → Backup seguro (sin clave privada)")
    
    print("\nINSTRUCCIONES DE SEGURIDAD:")
    print("1. Protege estos archivos con cifrado")
    print("2. Haz backup en USB offline")
    print("3. NUNCA compartas la clave privada")
    print("4. Usa esta wallet solo para RECIBIR fondos")
    print("5. Marca como wallet central del enjambre KAY")
    
    print("\nPRÓXIMOS PASOS:")
    print("1. Importar wallet_madre.json en Metamask/Trust Wallet")
    print("2. Configurar .env_wallet_madre en los scripts de KAY")
    print("3. Probar con pequeñas cantidades primero")
    print("4. Configurar el enjambre para enviar fondos aquí")
    
    return wallet_data

if __name__ == "__main__":
    try:
        wallet_data = generate_kay_mother_wallet()
        print("\n¡Wallet madre KAY lista para recibir cash real!")
    except Exception as e:
        print(f"❌ Error generando wallet: {e}")
        print("Verifica que eth_account esté instalado: pip install eth_account") 