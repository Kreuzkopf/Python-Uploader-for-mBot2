$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $here

$vsixPath = (python pack_vsix.py | Select-Object -Last 1).Trim()
if (-not $vsixPath -or -not (Test-Path -LiteralPath $vsixPath)) {
    Write-Error "VSIX не собран."
}
$vsix = Get-Item -LiteralPath $vsixPath

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
