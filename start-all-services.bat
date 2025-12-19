@echo off
REM ============================================================================
REM PastryApp - Windows Startup Script
REM ============================================================================
REM This script starts all services for the Pastry delivery app on Windows
REM ============================================================================

echo.
echo ========================================
echo   PastryApp - Starting All Services
echo ========================================
echo.

REM Get the script directory
set SCRIPT_DIR=%~dp0
set BACKEND_DIR=%SCRIPT_DIR%backend
set FRONTEND_DIR=%SCRIPT_DIR%frontend

REM Check if virtual environment exists
if not exist "%BACKEND_DIR%\venv" (
    echo [ERROR] Virtual environment not found!
    echo Please run: python -m venv backend\venv
    echo Then install dependencies: pip install -r backend\requirements.txt
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist "%BACKEND_DIR%\.env" (
    echo [WARNING] .env file not found!
    echo Please create backend\.env file with your MySQL configuration.
    echo See WINDOWS_SETUP_GUIDE.md for details.
    pause
)

echo [1/6] Initializing database...
cd /d "%BACKEND_DIR%"
call venv\Scripts\activate.bat
python init_db.py
if errorlevel 1 (
    echo [ERROR] Database initialization failed!
    pause
    exit /b 1
)
echo [OK] Database initialized
echo.

echo [2/6] Starting API Gateway (Port 5000)...
start "API Gateway - Port 5000" cmd /k "cd /d "%BACKEND_DIR%\api_gateway" && call "%BACKEND_DIR%\venv\Scripts\activate.bat" && python app.py"
timeout /t 3 /nobreak >nul
echo [OK] API Gateway started
echo.

echo [3/6] Starting Customer Service (Port 5001)...
start "Customer Service - Port 5001" cmd /k "cd /d "%BACKEND_DIR%\services\customer_service" && call "%BACKEND_DIR%\venv\Scripts\activate.bat" && python app.py"
timeout /t 2 /nobreak >nul
echo [OK] Customer Service started
echo.

echo [4/6] Starting Menu Service (Port 5003)...
start "Menu Service - Port 5003" cmd /k "cd /d "%BACKEND_DIR%\services\menu_service" && call "%BACKEND_DIR%\venv\Scripts\activate.bat" && python app.py"
timeout /t 2 /nobreak >nul
echo [OK] Menu Service started
echo.

echo [5/6] Starting Order Service (Port 5004)...
start "Order Service - Port 5004" cmd /k "cd /d "%BACKEND_DIR%\services\order_service" && call "%BACKEND_DIR%\venv\Scripts\activate.bat" && python app.py"
timeout /t 2 /nobreak >nul
echo [OK] Order Service started
echo.

echo [6/6] Starting Frontend Server (Port 8000)...
start "Frontend Server - Port 8000" cmd /k "cd /d "%FRONTEND_DIR%" && python -m http.server 8000"
timeout /t 2 /nobreak >nul
echo [OK] Frontend Server started
echo.

echo ========================================
echo   All Services Started Successfully!
echo ========================================
echo.
echo Access the Application:
echo   Customer Interface: http://localhost:8000/index.html
echo   Admin Dashboard:    http://localhost:8000/admin.html
echo.
echo Login Credentials:
echo   Customer: username: customer ^| password: iamcustomer
echo   Admin:    username: admin    ^| password: iamadmin
echo.
echo Services Running On:
echo   API Gateway:      http://localhost:5000
echo   Customer Service: http://localhost:5001
echo   Menu Service:     http://localhost:5003
echo   Order Service:    http://localhost:5004
echo   Frontend:         http://localhost:8000
echo.
echo [NOTE] Keep all terminal windows open while using the app.
echo        To stop services, close the terminal windows or press Ctrl+C in each.
echo.
pause

