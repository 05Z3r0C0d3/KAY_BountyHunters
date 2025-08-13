# 🪙 KAY_Centralizador.ps1 - Consolidación de Recompensas del Enjambre
Write-Host "`n💼 Iniciando consolidación de recompensas a wallet madre..." -ForegroundColor Yellow

$config = Get-Content ".\config\config_kay.json" | ConvertFrom-Json
$wallets = $config.generated_wallets
$walletMadre = $config.wallet_madre
$logPath = ".\logs\centralizador_$(Get-Date -Format yyyyMMdd_HHmmss).txt"

foreach ($wallet in $wallets) {
    Write-Host "🔁 Simulando transferencia desde wallet: $wallet"

    Start-Sleep -Milliseconds 800

    $resultado = "💸 Transferencia simulada`n" +
                 "🔐 Desde: $wallet`n" +
                 "📥 Hacia: $walletMadre`n" +
                 "💰 Monto: 100% disponible (simulado)`n" +
                 "🕓 Hora: $(Get-Date)`n" +
                 "--------------------------`n"

    Add-Content -Path $logPath -Value $resultado
}

Write-Host "`n✅ Consolidación completada. Log guardado en: $logPath" -ForegroundColor Green
