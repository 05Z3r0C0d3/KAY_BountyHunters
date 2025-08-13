# KAY_HormigaAutoFaucet.ps1 - v2
Write-Host "`n🐜 Solicitando fondos desde faucet..."
try {
    # Simulación de petición a faucet
    Start-Sleep -Seconds 2
    Write-Host "🟢 Fondos solicitados exitosamente."
} catch {
    Write-Host "🔴 Error con la solicitud: $($_.Exception.Message)"
}