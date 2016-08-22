@echo off
set /p choco_package_profile=Package Profile:
set PATH=%PATH%;C:\Chocolatey\bin;
set DIR=%~dp0%;
call cinst -y %DIR%package-profiles\%choco_package_profile%.config;
pause
