
# KAY_GalxeHunter.ps1 🕷️
# Sistema de caza automatizada en Galxe usando Cookie real
# Estado: Producción ✅

Write-Host "`n🕷️ Iniciando caza automatizada en GALXE...`n"

# Cargar configuración
$configPath = "config/config_kay.json"
if (-Not (Test-Path $configPath)) {
    Write-Host "❌ Configuración no encontrada en $configPath"
    exit
}
$config = Get-Content $configPath | ConvertFrom-Json
$cookie = $config.cookie_galxe
$targets = @("https://app.galxe.com/campaign/quest", "https://app.galxe.com/leaderboard", "https://app.galxe.com/user")

# Crear carpeta de logs si no existe
$logDir = "logs"
if (-Not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir }

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = "$logDir/log_galxe_$timestamp.txt"

# Headers
$headers = @{
    "cookie" = $cookie
    "user-agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Lógica de caza
foreach ($url in $targets) {
    Write-Host "`n🎯 Cazando en: $url"

    try {
        $response = Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing
        if ($response.StatusCode -eq 200) {
            $log = "✅ [$timestamp] Caza exitosa en $url`n"
        } else {
            $log = "⚠️ [$timestamp] Código $($response.StatusCode) en $url`n"
        }
    } catch {
        $log = "❌ [$timestamp] Error en $url - $($_.Exception.Message)`n"
    }

    Add-Content -Path $logPath -Value $log
    Start-Sleep -Seconds 2
}

Write-Host "`n✅ Cacería en Galxe finalizada. Log: $logPath" -ForegroundColor Green
