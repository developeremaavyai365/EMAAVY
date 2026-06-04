Add-Type -AssemblyName System.Drawing
$path = Join-Path $PSScriptRoot "..\assets\emaavy-logo.png" | Resolve-Path
$bmp = [System.Drawing.Bitmap]::FromFile($path)
$w = $bmp.Width
$h = $bmp.Height
$minX = $w
$minY = $h
$maxX = 0
$maxY = 0
for ($y = 0; $y -lt $h; $y++) {
  for ($x = 0; $x -lt $w; $x++) {
    $c = $bmp.GetPixel($x, $y)
    if ($c.R -lt 245 -or $c.G -lt 245 -or $c.B -lt 245) {
      if ($x -lt $minX) { $minX = $x }
      if ($y -lt $minY) { $minY = $y }
      if ($x -gt $maxX) { $maxX = $x }
      if ($y -gt $maxY) { $maxY = $y }
    }
  }
}
# Drop thin UI stroke on far-right edge of screenshot
$trimRight = 0
for ($x = $maxX; $x -ge $minX; $x--) {
  $dark = 0
  for ($y = $minY; $y -le $maxY; $y++) {
    $c = $bmp.GetPixel($x, $y)
    if ($c.R -lt 200 -and $c.G -lt 200 -and $c.B -lt 220) { $dark++ }
  }
  $colH = $maxY - $minY + 1
  if ($dark -gt [int]($colH * 0.55)) { $trimRight++ } else { break }
}
if ($trimRight -gt 0 -and $trimRight -lt 40) { $maxX -= $trimRight }

$pad = 6
$minX = [Math]::Max(0, $minX - $pad)
$minY = [Math]::Max(0, $minY - $pad)
$maxX = [Math]::Min($w - 1, $maxX + $pad)
$maxY = [Math]::Min($h - 1, $maxY + $pad)

# Square crop around logo center
$cw0 = $maxX - $minX + 1
$ch0 = $maxY - $minY + 1
$side = [Math]::Min($cw0, $ch0)
$cx = [int](($minX + $maxX) / 2)
$cy = [int](($minY + $maxY) / 2)
$minX = [Math]::Max(0, $cx - [int]($side / 2))
$minY = [Math]::Max(0, $cy - [int]($side / 2))
$maxX = [Math]::Min($w - 1, $minX + $side - 1)
$maxY = [Math]::Min($h - 1, $minY + $side - 1)
$cw = $maxX - $minX + 1
$ch = $maxY - $minY + 1
$crop = New-Object System.Drawing.Bitmap $cw, $ch
$g = [System.Drawing.Graphics]::FromImage($crop)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$src = New-Object System.Drawing.Rectangle $minX, $minY, $cw, $ch
$dst = New-Object System.Drawing.Rectangle 0, 0, $cw, $ch
$g.DrawImage($bmp, $dst, $src, [System.Drawing.GraphicsUnit]::Pixel)
$out = Join-Path (Split-Path $path) "emaavy-mark.png"
$crop.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$crop.Dispose()
$bmp.Dispose()
Write-Host "Cropped to ${cw}x${ch} -> $out"
