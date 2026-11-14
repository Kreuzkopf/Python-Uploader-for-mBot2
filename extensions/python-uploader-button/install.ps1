$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

python pack_vsix.py
$vsix = Get-ChildItem -Filter "*.vsix" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (-not $vsix) {
    Write-Error "VSIX не собран."
}

function Install-Vsix([string]$command) {
    $exe = Get-Command $command -ErrorAction SilentlyContinue
    if (-not $exe) {
        return $false
    }
    & $exe.Source --install-extension $vsix.FullName --force
    return $true
}

$installed = $false
foreach ($cmd in @("cursor", "code")) {
    if (Install-Vsix $cmd) {
        Write-Output "Установлено через $cmd : $($vsix.Name)"
        $installed = $true
    }
}
if (-not $installed) {
    Write-Error "Не найдены cursor или code в PATH. Установите VSIX вручную: $($vsix.FullName)"
}
