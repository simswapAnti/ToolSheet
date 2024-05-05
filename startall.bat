@echo off
title Anti's ToolBox - Downloading Dependency's

rem Install dependencies
pip install colorama fade requests

rem Check if installation was successful
if %errorlevel% neq 0 (
    echo Dependency installation failed.
    pause
    exit /b %errorlevel%
)

rem Run the Python script
python Menu.py

rem Pause to keep the window open after the script finishes
pause
