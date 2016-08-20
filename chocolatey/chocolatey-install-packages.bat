@echo off
set /p profile=Package Profile: 
set PATH=%PATH%;C:\Chocolatey\bin;
set DIR=%~dp0%;
call cinst -y %DIR%package-profiles\%profile%.config;
pause
