#!/usr/bin/env python3
"""
KAY CORP - Send BSC Transfer
Script para enviar transferencias en BSC
"""

import json
import sys
import time

try:
    from web3 import Web3
    from eth_account import Account
except ImportError as e:
    print(json.dumps({"error": f"Librería no encontrada: {e}"}))
    sys.exit(1)

def send_bsc_transfer(from_address, private_key, to_address, amount_bnb, gas_limit=21000, gas_price_gwei=5):
    """Enviar transferencia en BSC"""
    try:
        # Conectar a BSC
        bsc_rpc = "https://bsc-dataseed1.binance.org/"
        w3 = Web3(Web3.HTTPProvider(bsc_rpc))
        
        if not w3.is_connected():
            return {"error": "No se pudo conectar a BSC"}
        
        # Configurar cuenta
        account = Account.from_key(private_key)
        
        # Convertir a Wei
        amount_wei = w3.to_wei(amount_bnb, 'ether')
        
        # Obtener nonce
        nonce = w3.eth.get_transaction_count(from_address)
        
        # Crear transacción
        transaction = {
            'nonce': nonce,
            'to': to_address,
            'value': amount_wei,
            'gas': gas_limit,
            'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'),
            'chainId': 56  # BSC Mainnet
        }
        
        # Firmar transacción
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        
        # Enviar transacción
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        # Esperar confirmación
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        
        return {
            "success": True,
            "tx_hash": tx_hash.hex(),
            "block_number": tx_receipt.blockNumber,
            "gas_used": tx_receipt.gasUsed,
            "status": tx_receipt.status
        }
        
    except Exception as e:
        return {"error": f"Error en transferencia: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(json.dumps({"error": "Uso: python send_bsc_transfer.py <from_address> <private_key> <to_address> <amount_bnb>"}))
        sys.exit(1)
    
    from_address = sys.argv[1]
    private_key = sys.argv[2]
    to_address = sys.argv[3]
    amount_bnb = float(sys.argv[4])
    
    result = send_bsc_transfer(from_address, private_key, to_address, amount_bnb)
    print(json.dumps(result)) 