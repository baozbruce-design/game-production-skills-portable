param(
  [string]$TargetPath,
  [switch]$Force
)

$ErrorActionPreference = 'Stop'
$Source = Join-Path $PSScriptRoot 'skills'
$Target = if ($TargetPath) { $TargetPath } else { Join-Path $HOME '.codex\skills' }

if (-not (Test-Path $Source)) {
  throw "Skills source not found: $Source"
}

New-Item -ItemType Directory -Force -Path $Target | Out-Null

$installed = 0
$skipped = 0
foreach ($skill in Get-ChildItem -Path $Source -Directory) {
  $dest = Join-Path $Target $skill.Name
  if ((Test-Path $dest) -and -not $Force) {
    Write-Host "SKIP  $($skill.Name) (already exists; use -Force to replace)"
    $skipped++
    continue
  }
  if (Test-Path $dest) {
    Remove-Item -Path $dest -Recurse -Force
  }
  Copy-Item -Path $skill.FullName -Destination $dest -Recurse -Force
  Write-Host "INSTALL  $($skill.Name)"
  $installed++
}

Write-Host ""
Write-Host "Codex skills target: $Target"
Write-Host "Installed: $installed  Skipped: $skipped"
Write-Host "Restart/open a new Codex session so the skill catalog is refreshed."
