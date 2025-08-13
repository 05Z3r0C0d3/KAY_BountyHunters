# KAY_GeneraWallets.ps1 - Generador de Wallets 🪙
param (
    [int]$cantidad = 10
)

Write-Host "`n🔐 Generando $cantidad billeteras aleatorias..." -ForegroundColor Cyan

$carpeta = "wallets"
if (-not (Test-Path $carpeta)) {
    New-Item -ItemType Directory -Path $carpeta | Out-Null
}

for ($i = 1; $i -le $cantidad; $i++) {
    $privateKey = -join ((48..57) + (97..102) | Get-Random -Count 64 | ForEach-Object { [char]$_ })
    $walletFile = "$carpeta/wallet_$i.txt"
    $contenido = "Wallet #$i`nPrivate Key: 0x$privateKey`n"
    Set-Content -Path $walletFile -Value $contenido
    Write-Host "✅ Wallet $i generada y guardada en $walletFile" -ForegroundColor DarkGreen
}

Write-Host "`n🎉 Proceso completado. Billeteras generadas: $cantidad" -ForegroundColor Green
