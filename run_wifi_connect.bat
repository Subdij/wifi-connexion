REM filepath: /c:/Users/ziyad/Desktop/wifi-connexion/run_wifi_connect.bat
@echo off
REM Chemin vers RBTray.exe
set RBTRAY_PATH=C:\Users\ziyad\Desktop\wifi-connexion\RBtray\64bit\RBTray.exe

REM Charger les variables d'environnement à partir du fichier .env
for /f "tokens=1,2 delims==" %%i in (C:\Users\ziyad\Desktop\wifi-connexion\.env) do set %%i=%%j

REM Charger le nom d'utilisateur à partir du fichier .env
for /f "tokens=1,2 delims==" %%i in (C:\Users\ziyad\Desktop\wifi-connexion\.env) do if "%%i"=="USERNAME" set USERNAME=%%j

REM Lancer RBTray pour permettre la minimisation dans la zone de notification
start "" "%RBTRAY_PATH%"

:loop
REM Lancer le script Python sans afficher le terminal
start /b "" "C:\Users\ziyad\AppData\Local\Programs\Python\Python310\pythonw.exe" "C:\Users\ziyad\Desktop\wifi-connexion\wifi_connect.py"

REM Attendre 3 heures et 30 minutes (12600 secondes)
timeout /t 12600 /nobreak

REM Recommencer la boucle
goto loop