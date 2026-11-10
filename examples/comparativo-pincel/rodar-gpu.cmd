@echo off
cd /d "%~dp0"
set "CHROME_PATH=C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME_PATH%" set "CHROME_PATH=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
if not exist out mkdir out
set LOG=out\resultado-gpu.txt
echo === %DATE% %TIME% > %LOG%
node -v >> %LOG% 2>&1
ffmpeg -version 2>&1 | findstr /b "ffmpeg version" >> %LOG%
echo CHROME_PATH=%CHROME_PATH% >> %LOG%
set ANGLE=d3d11
node gpu.mjs >> %LOG% 2>&1
node still.mjs p5brush.html out\p5-gpu 2.5 4.6 >> %LOG% 2>&1
echo --- render d3d11 >> %LOG%
powershell -NoProfile -Command "$s=Get-Date; node render.mjs p5brush.html out\p5brush-gpu.mp4; 'tempo_total_s=' + [math]::Round(((Get-Date)-$s).TotalSeconds,1)" >> %LOG% 2>&1
powershell -NoProfile -Command "$s=Get-Date; node render.mjs lemo.html out\lemo-gpu.mp4; 'tempo_total_s=' + [math]::Round(((Get-Date)-$s).TotalSeconds,1)" >> %LOG% 2>&1
echo --- render swiftshader (mesma maquina, sem GPU) >> %LOG%
set ANGLE=swiftshader
node gpu.mjs >> %LOG% 2>&1
powershell -NoProfile -Command "$s=Get-Date; node render.mjs p5brush.html out\p5brush-cpu.mp4; 'tempo_total_s=' + [math]::Round(((Get-Date)-$s).TotalSeconds,1)" >> %LOG% 2>&1
echo === FIM >> %LOG%
type %LOG%
echo.
echo Pronto. Pode fechar esta janela.
pause
