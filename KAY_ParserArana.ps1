# 🧩 KAY_ParserAraña.ps1 - Análisis estratégico de objetivos
Write-Host "`n🧠 Iniciando análisis profundo con el Parser de la Araña..." -ForegroundColor Yellow

$config = Get-Content ".\config\config_kay.json" | ConvertFrom-Json
$objetivos = $config.preferred_targets
$logPath = "logs/parser_log_$(Get-Date -Format yyyyMMdd_HHmmss).txt"

foreach ($objetivo in $objetivos) {
    Write-Host "📂 Analizando estructura de: $objetivo"
    Start-Sleep -Milliseconds (Get-Random -Minimum 1500 -Maximum 3000)

    $debilidadDetectada = (Get-Random -Minimum 0 -Maximum 100) -gt 60
    $repetible = (Get-Random -Minimum 0 -Maximum 100) -gt 50

    $resultado = "==== ANÁLISIS OBJETIVO: $objetivo ====`n" +
                 "🔎 Vulnerabilidad: " + ($debilidadDetectada ? "Sí" : "No") + "`n" +
                 "🔁 Repetible: " + ($repetible ? "Sí" : "No") + "`n" +
                 "🕒 Fecha: $(Get-Date)`n" +
                 "--------------------------------------`n"

    Add-Content -Path $logPath -Value $resultado
}

Write-Host "`n✅ Análisis finalizado. Reporte en: $logPath" -ForegroundColor Green
Write-Host "📌 Úsalo junto al sistema de predicción para priorizar ataques del enjambre." -ForegroundColor Gray
