#!/usr/bin/env python3
"""
KAY CORP - Test BSC Balance
Script simple para probar la conexión a BSC y obtener balance
"""

import json
import sys

try:
    from web3 import Web3
    from eth_account import Account
except ImportError as e:
    print(json.dumps({"error": f"Librería no encontrada: {e}"}))
    sys.exit(1)

def get_bsc_balance(address):
    """Obtener balance de BSC"""
    try:
        # Conectar a BSC
        bsc_rpc = "https://bsc-dataseed1.binance.org/"
        w3 = Web3(Web3.HTTPProvider(bsc_rpc))
        
        if not w3.is_connected():
            return {"error": "No se pudo conectar a BSC"}
        
        # Obtener balance
        balance_wei = w3.eth.get_balance(address)
        balance_bnb = w3.from_wei(balance_wei, 'ether')
        
        return {
            "success": True,
            "balance_wei": str(balance_wei),
            "balance_bnb": float(balance_bnb),
            "address": address
        }
        
    except Exception as e:
        return {"error": f"Error obteniendo balance: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Uso: python test_bsc_balance.py <address>"}))
        sys.exit(1)
    
    address = sys.argv[1]
    result = get_bsc_balance(address)
    print(json.dumps(result)) 