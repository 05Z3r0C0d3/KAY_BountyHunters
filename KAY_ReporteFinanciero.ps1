
# KAY_ReporteFinanciero.ps1 ✅
Write-Host "`n📊 Generando reporte financiero del Enjambre..."

$fecha = Get-Date -Format "yyyyMMdd_HHmmss"
$reporte = @"
----- REPORTE FINANCIERO -----
📅 Fecha de reporte: $fecha
------------------------------

"@

$reporte += "`n💰 Fondos disponibles por billetera:`n"

# Simulación de lectura de fondos (reemplazar con la lógica real)
$wallets = @(
    @{ name = "Wallet_Alpha"; balance = "0.5 ETH" },
    @{ name = "Wallet_Beta"; balance = "0.23 ETH" },
    @{ name = "Wallet_Gamma"; balance = "1.02 ETH" }
)

foreach ($wallet in $wallets) {
    $reporte += "• $($wallet.name): $($wallet.balance)`n"
}

$reporte += "`n📦 Puedes abrir el archivo para visualizar el resumen completo del día."

$logPath = "logs/reporte_financiero_$($fecha).txt"
$logPath = $logPath -replace '[\\/:*?"<>|]', '_'

Set-Content -Path $logPath -Value $reporte
Write-Host "`n✅ Reporte financiero guardado en: $logPath" -ForegroundColor Green
