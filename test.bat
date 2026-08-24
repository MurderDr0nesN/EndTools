@echo off
title End-Tools - by Rezhu E Occhi
chcp 65001 >nul
cd Files
:start
call :banner

:menu
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A
echo.
echo.
echo 1) redtiger lite
echo 2) RedTiger Normal
echo 3) DoxTracker Master
echo 4) DoxxerX main
echo 5) sherlock
echo 6) slash-main
echo 7) vector
echo 8) Void
echo 9) tokengrabber
echo 10) zphisher
echo 11) zphisher Master
set /p input=.%BS%
if /I %input% EQU 1 start RedTiger-Tools\redtiger.py
if /I %input% EQU 2 start RedTiger-main\RedTiger.py
if /I %input% EQU 3 start DoxTracker-master\DoxTracker-master\DoxTracker.py
if /I %input% EQU 4 start 
if /I %input% EQU 5 start Sherlock\sherlock-master\avvia_sherlock.bat"
if /I %input% EQU 6 start 
if /I %input% EQU 7 start 
if /I %input% EQU 8 start Void-Tools-v2.0-main\Void-Tools-v2.0-main\start.bat
if /I %input% EQU 9 start 
if /I %input% EQU 10 start 
if /I %input% EQU 11 start 
cls
goto start

:Banner 
echo.
echo.
echo           [92m███████╗███╗   ██╗██████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗[0m
echo           [32m██╔════╝████╗  ██║██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝[0m
echo           [38;5;34m█████╗  ██╔██╗ ██║██║  ██║█████╗██║   ██║   ██║██║   ██║██║     ███████╗[0m
echo           [38;5;28m██╔══╝  ██║╚██╗██║██║  ██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║[0m
echo           [38;5;22m███████╗██║ ╚████║██████╔╝      ██║   ╚██████╔╝╚██████╔╝███████╗███████║[0m
echo           [38;2;0;48;0m╚══════╝╚═╝  ╚═══╝╚═════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝[0m
echo.
echo.
pause                                                                   