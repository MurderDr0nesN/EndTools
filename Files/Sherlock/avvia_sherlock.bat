@echo off
start powershell -NoExit -Command "Set-Location '%~dp0'; python main.py"
exit
