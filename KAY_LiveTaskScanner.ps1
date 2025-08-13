# 🛰️ KAY_LiveTaskScanner.ps1 - Escaneo en tiempo real de tareas nuevas desde plataformas de bounty

Import-Module BitsTransfer
Add-Type -AssemblyName System.Web

Write-Host "`n🛰️ Iniciando escaneo de nuevas tareas en plataformas bounty..." -ForegroundColor Cyan

$urls = @(
    "https://api.github.com/repos/Immunefi-team/bounties/issues",
    "https://raw.githubusercontent.com/ZealyHQ/tasks/main/tasks.json",
    "https://galxe.com/api/tasks/feed"
)

$logFile = "logs/livetaskscan_$(Get-Date -Format yyyyMMdd_HHmmss).txt"

foreach ($url in $urls) {
    Write-Host "🌐 Consultando: $url" -ForegroundColor Yellow

    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing -ErrorAction Stop
        $data = $response.Content

        $decoded = try { 
            $json = $data | ConvertFrom-Json
            "✅ JSON válido"
        } catch {
            "⚠️ No es JSON válido: $_"
        }

        $summary = @"
🔗 URL: $url
🕓 Fecha: $(Get-Date)
📦 Resumen: $decoded
-------------------------------------
"@

        Add-Content -Path $logFile -Value $summary
    } catch {
        Write-Host "❌ Error al escanear $url: $_" -ForegroundColor Red
        Add-Content -Path $logFile -Value "❌ Error al escanear $url: $_"
    }
}

Write-Host "`n✅ Escaneo completado. Resultado guardado en: $logFile" -ForegroundColor Green
