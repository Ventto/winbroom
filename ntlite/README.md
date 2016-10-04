NTLite
===================

## Configuration files

* `configs/`: NTLite configuration session files
* `registration-entries/HKCU/`: .REG files to custom Windows

## Custom the Windows

### HKCU for all users with NTLite 

Export .REG files from Windows Registry, import them into NTLite directly.

### HKCU for all users with WPKG method

>**Active Setup** is useful if you need to add an entry to HKCU for all users of a machine. It works by adding a key to HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name% with a version number. When a user logs in Windows checks this location and compares it to HKCU\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%. **If it is missing or a lower version then it runs whatever has been set in HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%\StubPath.**<br>
> -- <br><cite>[WPKG.org](https://wpkg.org/Adding_Registry_Settings#Adding_entries_to_HKCU_for_all_users)</cite>
