# 🕷️ KAY CORP - Sistema de Bounty Hunting Automatizado

## 📋 Resumen del Sistema

KAY CORP es un sistema completo de automatización para bounty hunting que incluye:

- **Dashboard en tiempo real** con conexión a datos JSON
- **Wallet madre** para centralización de fondos
- **Auto-split automático** para distribución de ganancias
- **Sistema de logging** y monitoreo
- **Scripts de bounty hunting** para múltiples plataformas

---

## 🏗️ Arquitectura del Sistema

### 📊 Frontend (Dashboard)
- **Archivo**: `templates/dashboard.html`
- **Funcionalidad**: SPA con 8 páginas completas
- **Actualización**: Cada 30 segundos automáticamente
- **Conexión**: Datos JSON en tiempo real

### 💰 Wallet Madre
- **Archivo**: `wallet_madre.json`
- **Dirección**: `0x925853Cf0A0a509737C10C624eEF18D529164269`
- **Red**: BSC (Binance Smart Chain)
- **Propósito**: Centralizar fondos del enjambre

### 🔄 Auto-Split System
- **Archivo**: `KAY_AutoSplitTransfer.ps1`
- **Distribución**: 70% Binance, 30% Freqtrade
- **Trigger**: Balance > 0.01 BNB
- **Logging**: Completo con hashes de transacciones

---

## 📁 Estructura de Archivos

```
KAY_CORP_SERVER/
├── 📊 templates/
│   └── dashboard.html          # Dashboard principal
├── 📈 data/
│   ├── wallets.json           # Datos de wallets
│   ├── earnings.json          # Datos de ganancias
│   ├── campaigns.json         # Datos de campañas
│   └── system_status.json     # Estado del sistema
├── 💰 wallet_madre.json       # Wallet madre (CRÍTICO)
├── ⚙️ .env_wallet_madre       # Configuración de wallet
├── 🔄 KAY_AutoSplitTransfer.ps1  # Auto-split system
├── 🕷️ KAY_GalxeHunter.py      # Cazador de Galxe
├── 🎯 KAY_EliteTargeter.ps1   # Targeter de campañas
├── 🕸️ KAY_BountyAraña.ps1     # Araña de búsqueda
├── 📊 KAY_DataConsolidator.ps1 # Consolidador de datos
└── 📋 logs/                   # Logs del sistema
```

---

## 🚀 Instalación y Configuración

### 1. Dependencias Python
```bash
pip install web3 eth_account
```

### 2. Wallet Madre
```bash
python generate_wallet_madre.py
```

### 3. Configurar Destinos
```bash
powershell -ExecutionPolicy Bypass -File "KAY_ConfigureDestinations.ps1"
```

### 4. Iniciar Dashboard
```bash
python -m http.server 8080
# Abrir: http://localhost:8080/templates/dashboard.html
```

---

## 🎯 Uso del Sistema

### Dashboard
- **Navegación**: 8 páginas completas (Wallets, Campaigns, Automation, etc.)
- **Datos en vivo**: Actualización automática cada 30 segundos
- **Logs de errores**: Página Security → View Error Logs
- **Test de conexiones**: Página Security → Test Connections

### Auto-Split
```bash
# Modo test (sin transferencias reales)
powershell -ExecutionPolicy Bypass -File "KAY_AutoSplitTransfer.ps1" -TestMode

# Transferencias reales
powershell -ExecutionPolicy Bypass -File "KAY_AutoSplitTransfer.ps1"

# Forzar transferencia (balance bajo)
powershell -ExecutionPolicy Bypass -File "KAY_AutoSplitTransfer.ps1" -ForceTransfer
```

### Scripts de Bounty Hunting
```bash
# Cazador de Galxe
python KAY_GalxeHunter.py

# Targeter de campañas
powershell -ExecutionPolicy Bypass -File "KAY_EliteTargeter.ps1"

# Araña de búsqueda
powershell -ExecutionPolicy Bypass -File "KAY_BountyAraña.ps1"
```

---

## 🔐 Seguridad

### Wallet Madre
- **NUNCA** compartir la clave privada
- **Backup** en USB offline
- **Usar solo** para recibir fondos
- **Separar** de wallets de trading

### Archivos Críticos
- `wallet_madre.json` - Contiene clave privada
- `.env_wallet_madre` - Configuración de wallet
- `kay_destinations.env` - Direcciones de destino

### Logs de Seguridad
- `logs/split_log.txt` - Logs de transferencias
- `logs/split_summary.json` - Resúmenes de splits
- `logs/security_manager.log` - Logs de seguridad

---

## 📊 Monitoreo

### Dashboard Features
- ✅ **Conexión en vivo** con JSON files
- ✅ **Actualización automática** cada 30 segundos
- ✅ **Logging de errores** con contexto
- ✅ **Indicadores de estado** visuales
- ✅ **Test de conexiones** manual

### Logs Disponibles
- **Error Logs**: Errores de carga de datos
- **Split Logs**: Transferencias automáticas
- **Security Logs**: Eventos de seguridad
- **System Logs**: Estado del sistema

---

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Wallet Madre
KAY_WALLET_ADDRESS=0x...
KAY_WALLET_PRIVATE_KEY=0x...
KAY_NETWORK=BSC

# Destinos
BINANCE_WALLET=0x...
FREQTRADE_WALLET=0x...
```

### Parámetros de Auto-Split
```powershell
$MIN_BALANCE_BNB = 0.01        # Balance mínimo para split
$BINANCE_PERCENTAGE = 70       # Porcentaje a Binance
$FREQTRADE_PERCENTAGE = 30     # Porcentaje a Freqtrade
$GAS_LIMIT = 21000             # Límite de gas
$GAS_PRICE_GWEI = 5            # Precio de gas en Gwei
```

---

## 🚨 Troubleshooting

### Problemas Comunes

1. **Error de conexión BSC**
   - Verificar conexión a internet
   - Probar RPC alternativo

2. **Balance no se actualiza**
   - Verificar archivos JSON
   - Revisar logs de errores

3. **Transferencias fallan**
   - Verificar balance suficiente
   - Revisar gas fees
   - Confirmar direcciones correctas

### Logs de Debug
```bash
# Ver logs de errores
cat logs/split_log.txt

# Ver resúmenes de splits
cat logs/split_summary.json

# Test de conexión BSC
python test_bsc_balance.py <address>
```

---

## 🎉 Estado Actual

### ✅ Completado
- [x] Dashboard en tiempo real
- [x] Wallet madre generada
- [x] Auto-split system funcional
- [x] Logging completo
- [x] Conexión BSC operativa
- [x] Sistema de monitoreo

### 🔄 En Desarrollo
- [ ] Integración con scripts de bounty hunting
- [ ] Optimización de gas fees
- [ ] Alertas automáticas
- [ ] Backup automático

### 📋 Próximos Pasos
1. **Configurar direcciones reales** de Binance y Freqtrade
2. **Probar con pequeñas cantidades** primero
3. **Ejecutar scripts de bounty hunting** para generar datos reales
4. **Monitorear** el sistema en producción

---

## 🕷️ KAY CORP - Bounty Hunter's™

**Sistema autónomo de consolidación y distribución de recompensas cripto**

*Desarrollado con estilo de ingeniero Web3* 😎 