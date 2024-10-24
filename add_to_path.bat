@echo off

REM Holt das Verzeichnis des aktuellen Batch-Skripts
SET "SCRIPT_DIR=%~dp0"

REM Entfernt den abschließenden Backslash, falls vorhanden
IF "%SCRIPT_DIR:~-1%"=="\" SET "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

echo Überprüfet, ob das Skript-Verzeichnis bereits im PATH ist
echo %PATH% | findstr /C:"%SCRIPT_DIR%" > nul

if errorlevel 1 (
    echo Fügt das Skript-Verzeichnis dem PATH hinzu
    SETX PATH "%PATH%;%SCRIPT_DIR%"

    REM Der geänderte PATH wird erst nach dem Neustart der Konsole wirksam.
    echo Skript-Verzeichnis wurde dem PATH hinzugefügt. Bitte starten Sie die Konsole neu, um die Änderungen zu übernehmen.
) else (
    echo Skript-Verzeichnis ist bereits im PATH.
)

echo Fertig!