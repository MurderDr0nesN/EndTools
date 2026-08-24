@echo off
title Sherlock - Remodel By Rezhu
chcp 65001 >nul
:start
call :banner

:menu
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A

:Banner
echo.
echo.
echo          [92m  ▄▄▄▄▄▄▄ ▄▄                ▄▄                    
echo          [32m█████▀▀▀ ██                ██             ▄▄     
echo          [38;5;34m  ▀████▄  ████▄ ▄█▀█▄ ████▄ ██ ▄███▄ ▄████ ██ ▄█▀ 
echo          [38;5;28m   ▀████ ██ ██ ██▄█▀ ██ ▀▀ ██ ██ ██ ██    ████   
echo          [38;5;22m ███████▀ ██ ██ ▀█▄▄▄ ██    ██ ▀███▀ ▀████ ██ ▀█▄ 
echo.
echo.