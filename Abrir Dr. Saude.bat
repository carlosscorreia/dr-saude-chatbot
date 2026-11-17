@echo off
title Dr. Saude
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (py atv_fan_01.py) else (python atv_fan_01.py)
