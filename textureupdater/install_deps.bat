@echo off
REM ----------------------------------------
REM install_latest_deps.bat
REM Installs the latest versions of required Python packages
REM ----------------------------------------

echo Checking for pip...
where pip >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip not found. Please install Python/pip and add to your PATH.
    exit /b 1
)

echo.
echo Installing latest dependencies...
pip install ^
    psutil ^
    aiohttp ^
    tenacity ^
    requests ^
    tzlocal ^
    pytz

if errorlevel 1 (
    echo.
    echo [ERROR] One or more packages failed to install.
    echo Please check the error messages above and re‑run this script.
    exit /b 1
)

echo.
echo All dependencies installed successfully!
pause
