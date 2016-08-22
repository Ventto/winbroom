powershell Set-ExecutionPolicy RemoteSigned;
powershell iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'));
pause
