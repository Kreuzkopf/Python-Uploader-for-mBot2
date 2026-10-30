# Установка кнопки Uploader в статус-бар Cursor / VS Code.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python .\pack_vsix.py
$vsix = Get-ChildItem -Filter "*.vsix" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (-not $vsix) {
  throw "VSIX не собран"
}

$editor = $null
foreach ($name in @("cursor", "code")) {
  $cmd = Get-Command $name -ErrorAction SilentlyContinue
  if ($cmd) { $editor = $cmd.Source; break }
}
if (-not $editor) {
  Write-Host "Не найден cursor/code в PATH."
  Write-Host "Ctrl+Shift+P -> Extensions: Install from VSIX..."
  Write-Host $vsix.FullName
  exit 1
}

Write-Host "Установка $($vsix.Name) через $editor"
& $editor --install-extension $vsix.FullName
Write-Host "Готово. Reload Window, если кнопки ещё нет."
