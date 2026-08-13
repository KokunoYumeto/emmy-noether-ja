$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$script = Join-Path $root 'tools\make_reader.py'
$reader = Join-Path $root 'reader\00_EMMY_NOETHER_JA_COMPLETE_LINKED_READER.pdf'
$bundledPython = 'C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$python = if (Test-Path -LiteralPath $bundledPython) { $bundledPython } else { 'python' }

& $python $script
if ($LASTEXITCODE -ne 0) { throw "First reader build failed with exit code $LASTEXITCODE" }
$first = (Get-FileHash -Algorithm SHA256 -LiteralPath $reader).Hash
$bytes = (Get-Item -LiteralPath $reader).Length

& $python $script
if ($LASTEXITCODE -ne 0) { throw "Second reader build failed with exit code $LASTEXITCODE" }
$second = (Get-FileHash -Algorithm SHA256 -LiteralPath $reader).Hash

if ($first -ne $second) { throw "Publication reader is not byte-reproducible: $first != $second" }
Write-Output "PASS reader bytes=$bytes sha256=$second"
