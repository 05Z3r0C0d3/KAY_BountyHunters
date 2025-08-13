# =============================================================================
# KAY CORP - Configure Destinations
# =============================================================================
# Script para configurar las direcciones de destino del auto-split
# =============================================================================

Write-Host "=== KAY CORP - Configure Destinations ===" -ForegroundColor Cyan
Write-Host "Configurando direcciones de destino para auto-split..." -ForegroundColor Yellow

# Solicitar direcciones al usuario
Write-Host "`n📋 INSTRUCCIONES:" -ForegroundColor Green
Write-Host "1. Dirección de Binance: Copia la dirección de depósito de BNB desde tu cuenta de Binance"
Write-Host "2. Dirección de Freqtrade: Copia la dirección de la wallet del bot Freqtrade"
Write-Host "3. Verifica que ambas direcciones sean válidas antes de continuar"
Write-Host ""

$binanceWallet = Read-Host "🔗 Dirección de Binance (0x...)"
$freqtradeWallet = Read-Host "🤖 Dirección de Freqtrade (0x...)"

# Validar formato de direcciones
if ($binanceWallet -notmatch "^0x[a-fA-F0-9]{40}$") {
    Write-Host "❌ Dirección de Binance inválida" -ForegroundColor Red
    exit 1
}

if ($freqtradeWallet -notmatch "^0x[a-fA-F0-9]{40}$") {
    Write-Host "❌ Dirección de Freqtrade inválida" -ForegroundColor Red
    exit 1
}

# Crear archivo de configuración
$configContent = @"
# KAY CORP - Destination Wallets Configuration
# Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
# ⚠️  CRITICAL - VERIFY THESE ADDRESSES

# Binance Wallet (70% of funds)
BINANCE_WALLET=$binanceWallet

# Freqtrade Bot Wallet (30% of funds)
FREQTRADE_WALLET=$freqtradeWallet

# Network Configuration
NETWORK=BSC
CHAIN_ID=56
"@

$configContent | Out-File -FilePath "kay_destinations.env" -Encoding UTF8

# Actualizar el script principal
$scriptContent = Get-Content "KAY_AutoSplitTransfer.ps1" -Raw
$scriptContent = $scriptContent -replace '0xBinanceWalletRealAqui1234567890abcdef1234567890abcdef', $binanceWallet
$scriptContent = $scriptContent -replace '0xFreqtradeBotWalletAqui4567890abcdef1234567890abcdef', $freqtradeWallet
$scriptContent | Out-File -FilePath "KAY_AutoSplitTransfer.ps1" -Encoding UTF8

Write-Host "`n✅ Configuración completada!" -ForegroundColor Green
Write-Host "📁 Archivos creados:" -ForegroundColor Cyan
Write-Host "  • kay_destinations.env - Configuración de direcciones"
Write-Host "  • KAY_AutoSplitTransfer.ps1 - Script actualizado"
Write-Host ""

Write-Host "🔍 RESUMEN DE CONFIGURACIÓN:" -ForegroundColor Yellow
Write-Host "  Binance: $($binanceWallet.Substring(0,10))..." -ForegroundColor White
Write-Host "  Freqtrade: $($freqtradeWallet.Substring(0,10))..." -ForegroundColor White
Write-Host ""

Write-Host "⚠️  PRÓXIMOS PASOS:" -ForegroundColor Yellow
Write-Host "1. Verifica las direcciones en kay_destinations.env"
Write-Host "2. Prueba el script con: .\KAY_AutoSplitTransfer.ps1 -TestMode"
Write-Host "3. Ejecuta transferencias reales: .\KAY_AutoSplitTransfer.ps1"
Write-Host ""

Write-Host "🎯 ¡Sistema KAY listo para distribución automática!" -ForegroundColor Green 