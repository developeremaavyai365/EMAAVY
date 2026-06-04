Add-Type -AssemblyName System.Drawing
$path = Join-Path $PSScriptRoot "..\assets\emaavy-wordmark-source.png" | Resolve-Path
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
    if ($c.R -lt 248 -or $c.G -lt 248 -or $c.B -lt 248) {
      if ($x -lt $minX) { $minX = $x }
      if ($y -lt $minY) { $minY = $y }
      if ($x -gt $maxX) { $maxX = $x }
      if ($y -gt $maxY) { $maxY = $y }
    }
  }
}
$trimRight = 0
for ($x = $maxX; $x -ge $minX; $x--) {
  $dark = 0
  for ($y = $minY; $y -le $maxY; $y++) {
    $c = $bmp.GetPixel($x, $y)
    if ($c.R -lt 200 -and $c.G -lt 200 -and $c.B -lt 220) { $dark++ }
  }
  if ($dark -gt [int](($maxY - $minY + 1) * 0.55)) { $trimRight++ } else { break }
}
if ($trimRight -gt 0 -and $trimRight -lt 40) { $maxX -= $trimRight }

$pad = 10
$minX = [Math]::Max(0, $minX - $pad)
$minY = [Math]::Max(0, $minY - $pad)
$maxX = [Math]::Min($w - 1, $maxX + $pad)
$maxY = [Math]::Min($h - 1, $maxY + $pad)
$cw = $maxX - $minX + 1
$ch = $maxY - $minY + 1
$crop = New-Object System.Drawing.Bitmap $cw, $ch
$g = [System.Drawing.Graphics]::FromImage($crop)
$g.Clear([System.Drawing.Color]::White)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$src = New-Object System.Drawing.Rectangle $minX, $minY, $cw, $ch
$dst = New-Object System.Drawing.Rectangle 0, 0, $cw, $ch
$g.DrawImage($bmp, $dst, $src, [System.Drawing.GraphicsUnit]::Pixel)
$out = Join-Path (Split-Path $path) "emaavy-wordmark.png"
$crop.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$crop.Dispose()
$bmp.Dispose()
Write-Host "Wordmark ${cw}x${ch} -> $out"
