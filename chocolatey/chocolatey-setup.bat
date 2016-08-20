powershell Set-ExecutionPolicy RemoteSigned;
powershell iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'));
powershell Set-ExecutionPolicy Restricted;
set PATH=%PATH%;C:\Chocolatey\bin;
call cinst -y chocolatey;
pause
