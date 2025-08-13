# KAY_BountyAraña.ps1 🕷️
Write-Host "`n🕸️ Enlace de referido automático listo para spam controlado`n" -ForegroundColor DarkYellow

$config = Get-Content ".\config\config_kay.json" | ConvertFrom-Json
$targets = $config.preferred_targets
$logPath = "logs/log_spider_$(Get-Date -Format yyyyMMdd_HHmmss).txt"

foreach ($target in $targets) {
    Write-Host "🔍 Escaneando objetivo: $target"

    Start-Sleep -Seconds 2

    $resultado = "----- ESCANEO DE: $target -----`n" +
                 "🟢 Resultado: Simulación exitosa`n" +
                 "🕓 Hora: $(Get-Date)`n" +
                 "Ganancia: $12.50`n" +
                 "------------------------------`n"

    Add-Content -Path $logPath -Value $resultado
}

Write-Host "`n✅ Escaneo finalizó. Log guardado en: $logPath" -ForegroundColor Green
