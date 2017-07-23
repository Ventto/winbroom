NTLite
===================

## Tree

`configs/`: NTLite configuration session files

`registration-entries/HKCU/`: .REG files to custom Windows

## HKCU for all users

* Export .REG files from Windows Registry, import them into NTLite directly.

* HKCU for all users with WPKG method:

>**Active Setup** is useful if you need to add an entry to HKCU for all users of a machine. It works by adding a key to HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name% with a version number. When a user logs in Windows checks this location and compares it to HKCU\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%. **If it is missing or a lower version then it runs whatever has been set in HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%\StubPath.**<br>
> -- <br><cite>[WPKG.org](https://wpkg.org/Adding_Registry_Settings#Adding_entries_to_HKCU_for_all_users)</cite>

## Configs

### Common
* Components:
  - [ ] Remove Cortana (Post-Setup script: rename: "Microsoft.Windows.Cortana_cw5n1h2txyewy")
  - [ ] Remove OneDrive
  - [ ] Remove Store **(ntlite: feature in process)**
* Custom:
  - [x] Remove/Disable Narrator
  - [ ] No Background while locking screen **(reg: failed)**
  - [x] Unpin Cortana from MainTab (maybe linked to a disabled service)
  - [x] Unpin OneDrive from MainTab (maybe linked to a disabled service)
  - [ ] Unpin Store from MainTab
  - [ ] Background: Solid Color/Blue **(reg: failed)** (default values only ?)
  * Appearences
    - [ ] Allow changing Windows Color: OFF
    - [ ] Allow Color scheme changes: OFF
    - [ ] Change desktop bg: OFF
    - [ ] Allow changing screensaver: OFF
    - [ ] Effect optimizations **(reg: remains active effects)**
  * Settings > System:
    - [x] Hide app icons on the taskbar in table mode: OFF
    * Devices:
      - [x] Remove Fax **(reg)**
      - [ ] Use AutoPlay for all media and devices: OFF **(reg: failed)**
      - [x] The default printer is the last used printer: OFF **(reg)**
    * Time & Language:
      - [ ] Time zone: Europe/Paris
      * Time format:
        - [ ] First day of week: Monday
        - [ ] Short date: dd-MMM-yyyy
        - [ ] Short time: HH:mm
    * Privacy:
      - [ ] Location: OFF
      - [ ] Let's app use my camera: OFF
      - [ ] Let's app use my micro: OFF
      - [ ] Let's app access my name, picture, account info: OFF
      - [ ] Let's app access my calendar: OFF (useless)
      - [ ] Let's app access call history: OFF (useless)
      - [ ] Let's app access and send email: OFF
      - [ ] Let's app read or send msgs txt or MMS: OFF (useless)
      - [ ] Let's app control radio: OFF
      - [ ] Let your apps auto share and sync info with wireless devices[...]: OFF
      - [x] Windows should ask for my feedback: Never **(reg)**
      - [ ] Apps use my advertising ID for experiences across apps
      - [ ] In the Speech, Inking, & Typing area:
      - [ ] Send your device data to Microsoft: OFF
      - [ ] Let's run Store in background: OFF
    * Update and Security:
      - [x] Help us make Windows Defender better: OFF **(reg)**
      - [ ] For developers: Developer mode
      - [ ] No auto-reboot with logged users: ON
      - [ ] Auto updates: Check but don't download
    * Personalization:
      - [ ] Show most used apps: OFF
      - [ ] Show recently added apps: OFF
      - [ ] Choose Which folder appear on Start: +Personal Folder
* Account
  - [ ] Administrator: Password
  - [ ] User Tom: Passwrd + Limited Account
  - [x] To prevent communication to the Microsoft Account cloud authentication service
  - [x] Turn off Wi-Fi Sense that automatically connects devices to known hotspots...

### Guest Mode
* Services:
  - [x] Remove/Disable Windows Audio
  - [x] Remove/Disable Windows Printing  Spoiler
  - [x] Remove/Disable Windows Audio Endpoin
  - [x] Remove Windows Power Management
  - [x] Disable Theme
* Custom > Settings > System:
  - [x] Power & Sleep, On Battery power, turn off after: Never (linked to the power service)
  - [x] Power & Sleep, When plugged in, turn off after: Never (linked to the power service)
