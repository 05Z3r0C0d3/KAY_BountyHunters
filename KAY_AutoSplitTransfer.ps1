# =============================================================================
# KAY CORP - Auto Split Transfer System
# =============================================================================
# Sistema autónomo de consolidación y distribución de recompensas cripto
# Distribuye automáticamente fondos de la wallet madre: 70% Binance, 30% Freqtrade
# =============================================================================

param(
    [switch]$TestMode,
    [switch]$ForceTransfer,
    [string]$LogLevel = "INFO"
)

# Configuración del sistema
$SCRIPT_VERSION = "1.0.0"
$MIN_BALANCE_BNB = 0.01
$BINANCE_PERCENTAGE = 70
$FREQTRADE_PERCENTAGE = 30
$GAS_LIMIT = 21000
$GAS_PRICE_GWEI = 5

# Direcciones de destino (REEMPLAZAR CON DIRECCIONES REALES)
$BINANCE_WALLET = "0xBinanceWalletRealAqui1234567890abcdef1234567890abcdef"
$FREQTRADE_WALLET = "0xFreqtradeBotWalletAqui4567890abcdef1234567890abcdef"

# Función de logging
function Write-KayLog {
    param(
        [string]$Message,
        [string]$Level = "INFO"
    )
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] [$Level] $Message"
    
    # Console output
    switch ($Level) {
        "ERROR" { Write-Host $logEntry -ForegroundColor Red }
        "WARNING" { Write-Host $logEntry -ForegroundColor Yellow }
        "SUCCESS" { Write-Host $logEntry -ForegroundColor Green }
        "INFO" { Write-Host $logEntry -ForegroundColor Cyan }
        default { Write-Host $logEntry }
    }
    
    # File logging
    $logDir = "logs"
    if (!(Test-Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    
    $logFile = "$logDir\split_log.txt"
    Add-Content -Path $logFile -Value $logEntry
}

# Función para cargar configuración de wallet madre
function Get-KayWalletConfig {
    try {
        if (!(Test-Path ".env_wallet_madre")) {
            throw "Archivo .env_wallet_madre no encontrado"
        }
        
        $config = @{}
        Get-Content ".env_wallet_madre" | ForEach-Object {
            if ($_ -match "^([^#][^=]+)=(.*)$") {
                $config[$matches[1]] = $matches[2].Trim()
            }
        }
        
        if (!$config.ContainsKey("KAY_WALLET_ADDRESS") -or !$config.ContainsKey("KAY_WALLET_PRIVATE_KEY")) {
            throw "Configuración incompleta en .env_wallet_madre"
        }
        
        return $config
    }
    catch {
        Write-KayLog "Error cargando configuración: $($_.Exception.Message)" "ERROR"
        exit 1
    }
}

# Función para obtener balance real de BSC
function Get-BSCBalance {
    param(
        [string]$Address
    )
    
    try {
        Write-KayLog "Obteniendo balance de BSC para: $($Address.Substring(0,10))..."
        
        # Usar script Python externo para obtener balance
        $result = python test_bsc_balance.py $Address 2>$null
        if ($LASTEXITCODE -ne 0) {
            throw "Error ejecutando Python script"
        }
        
        $balanceData = $result | ConvertFrom-Json
        Write-KayLog "Balance obtenido: $($balanceData.balance_bnb) BNB" "SUCCESS"
        
        return $balanceData
    }
    catch {
        Write-KayLog "Error obteniendo balance: $($_.Exception.Message)" "ERROR"
        return $null
    }
}

# Función para calcular split
function Calculate-Split {
    param(
        [double]$TotalBalance
    )
    
    $binanceAmount = [math]::Round($TotalBalance * ($BINANCE_PERCENTAGE / 100), 8)
    $freqtradeAmount = [math]::Round($TotalBalance * ($FREQTRADE_PERCENTAGE / 100), 8)
    
    # Ajustar para gas fees
    $gasFeeBNB = [math]::Round(($GAS_LIMIT * $GAS_PRICE_GWEI) / 1e9, 8)
    $totalGasFees = $gasFeeBNB * 2  # Dos transacciones
    
    if (($binanceAmount + $freqtradeAmount + $totalGasFees) -gt $TotalBalance) {
        # Ajustar montos para incluir gas fees
        $availableForTransfer = $TotalBalance - $totalGasFees
        $binanceAmount = [math]::Round($availableForTransfer * ($BINANCE_PERCENTAGE / 100), 8)
        $freqtradeAmount = [math]::Round($availableForTransfer * ($FREQTRADE_PERCENTAGE / 100), 8)
    }
    
    return @{
        BinanceAmount = $binanceAmount
        FreqtradeAmount = $freqtradeAmount
        GasFees = $totalGasFees
        TotalTransfer = $binanceAmount + $freqtradeAmount
    }
}

# Función para ejecutar transferencia
function Send-BSCTransfer {
    param(
        [string]$FromAddress,
        [string]$PrivateKey,
        [string]$ToAddress,
        [double]$Amount,
        [string]$Description
    )
    
    try {
        Write-KayLog "Enviando $Amount BNB a $Description..."
        
        # Usar script Python externo para transferencia
        $result = python send_bsc_transfer.py $FromAddress $PrivateKey $ToAddress $Amount 2>$null
        if ($LASTEXITCODE -ne 0) {
            throw "Error en transferencia"
        }
        
        $txData = $result | ConvertFrom-Json
        if ($txData.success) {
            Write-KayLog "Transferencia exitosa: $($txData.tx_hash)" "SUCCESS"
            return $txData
        } else {
            throw "Transacción falló"
        }
    }
    catch {
        Write-KayLog "Error en transferencia: $($_.Exception.Message)" "ERROR"
        return $null
    }
}

# Función principal
function Start-KayAutoSplit {
    Write-KayLog "=== KAY CORP Auto Split Transfer System v$SCRIPT_VERSION ===" "INFO"
    Write-KayLog "Iniciando proceso de distribución automática..." "INFO"
    
    # Cargar configuración
    $config = Get-KayWalletConfig
    $walletAddress = $config.KAY_WALLET_ADDRESS
    $privateKey = $config.KAY_WALLET_PRIVATE_KEY
    
    Write-KayLog "Wallet madre: $($walletAddress.Substring(0,10))..." "INFO"
    
    # Obtener balance
    $balanceData = Get-BSCBalance -Address $walletAddress
    if (!$balanceData) {
        Write-KayLog "No se pudo obtener balance. Saliendo." "ERROR"
        exit 1
    }
    
    $balanceBNB = $balanceData.balance_bnb
    Write-KayLog "Balance total: $balanceBNB BNB" "INFO"
    
    # Verificar balance mínimo
    if ($balanceBNB -lt $MIN_BALANCE_BNB -and !$ForceTransfer) {
        Write-KayLog "Balance muy bajo ($balanceBNB BNB). Split pospuesto." "WARNING"
        exit 0
    }
    
    # Calcular split
    $splitData = Calculate-Split -TotalBalance $balanceBNB
    Write-KayLog "Calculando distribución:" "INFO"
    Write-KayLog "  - Binance ($BINANCE_PERCENTAGE%): $($splitData.BinanceAmount) BNB" "INFO"
    Write-KayLog "  - Freqtrade ($FREQTRADE_PERCENTAGE%): $($splitData.FreqtradeAmount) BNB" "INFO"
    Write-KayLog "  - Gas fees estimados: $($splitData.GasFees) BNB" "INFO"
    
    if ($TestMode) {
        Write-KayLog "MODO TEST: No se ejecutarán transferencias reales" "WARNING"
        return
    }
    
    # Ejecutar transferencias
    $transactions = @()
    
    # Transferencia a Binance
    Write-KayLog "Ejecutando transferencia a Binance..." "INFO"
    $binanceTx = Send-BSCTransfer -FromAddress $walletAddress -PrivateKey $privateKey -ToAddress $BINANCE_WALLET -Amount $splitData.BinanceAmount -Description "Binance"
    if ($binanceTx) {
        $transactions += @{
            Type = "Binance"
            Amount = $splitData.BinanceAmount
            TxHash = $binanceTx.tx_hash
            Status = "Success"
        }
    }
    
    # Transferencia a Freqtrade
    Write-KayLog "Ejecutando transferencia a Freqtrade..." "INFO"
    $freqtradeTx = Send-BSCTransfer -FromAddress $walletAddress -PrivateKey $privateKey -ToAddress $FREQTRADE_WALLET -Amount $splitData.FreqtradeAmount -Description "Freqtrade"
    if ($freqtradeTx) {
        $transactions += @{
            Type = "Freqtrade"
            Amount = $splitData.FreqtradeAmount
            TxHash = $freqtradeTx.tx_hash
            Status = "Success"
        }
    }
    
    # Log final
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $summary = @{
        Timestamp = $timestamp
        WalletAddress = $walletAddress
        InitialBalance = $balanceBNB
        BinanceTransfer = $splitData.BinanceAmount
        FreqtradeTransfer = $splitData.FreqtradeAmount
        TotalGasFees = $splitData.GasFees
        Transactions = $transactions
    }
    
    $summaryJson = $summary | ConvertTo-Json -Depth 3
    Add-Content -Path "logs\split_summary.json" -Value $summaryJson
    
    Write-KayLog "=== Proceso completado ===" "SUCCESS"
    Write-KayLog "Resumen guardado en logs\split_summary.json" "INFO"
}

# Ejecutar script
try {
    Start-KayAutoSplit
}
catch {
    Write-KayLog "Error crítico: $($_.Exception.Message)" "ERROR"
    exit 1
} 