Add-Type -AssemblyName System.Drawing
$path = Join-Path $PSScriptRoot "..\assets\emaavy-mark.png" | Resolve-Path
$bmp = [System.Drawing.Bitmap]::FromFile($path)
$w = $bmp.Width
$h = $bmp.Height
$trim = 0
for ($x = $w - 1; $x -ge 0; $x--) {
  $dark = 0
  $total = 0
  for ($y = 0; $y -lt $h; $y++) {
    $c = $bmp.GetPixel($x, $y)
    if ($c.R -lt 250 -or $c.G -lt 250 -or $c.B -lt 250) { $total++ }
    if ($c.R -lt 120 -and $c.G -lt 120 -and $c.B -lt 140) { $dark++ }
  }
  if ($total -gt 0 -and ($dark / [Math]::Max(1, $total)) -gt 0.7 -and $total -lt ($h * 0.15)) {
    $trim++
  } else {
    break
  }
}
if ($trim -eq 0) { $trim = 14 }
$newW = $w - $trim
$crop = New-Object System.Drawing.Bitmap $newW, $h
$g = [System.Drawing.Graphics]::FromImage($crop)
$g.Clear([System.Drawing.Color]::White)
$src = New-Object System.Drawing.Rectangle 0, 0, $newW, $h
$dst = New-Object System.Drawing.Rectangle 0, 0, $newW, $h
$g.DrawImage($bmp, $dst, 0, 0, $newW, $h, [System.Drawing.GraphicsUnit]::Pixel)
$tmp = Join-Path (Split-Path $path) "emaavy-mark-trimmed.png"
$crop.Save($tmp, [System.Drawing.Imaging.ImageFormat]::Png)
Copy-Item -Force $tmp $path
Remove-Item -Force $tmp
$g.Dispose(); $crop.Dispose(); $bmp.Dispose()
Write-Host "Trimmed $trim px from right -> ${newW}x${h}"
