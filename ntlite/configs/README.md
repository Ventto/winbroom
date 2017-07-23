TODO
============

## Common
* Components:
  - [ ] Remove Cortana (Post-Setup script: rename: "Microsoft.Windows.Cortana_cw5n1h2txyewy")
  - [ ] Remove OneDrive
  - [ ] Remove Store [NTLITE]
* Custom:
  - [x] Remove/Disable Narrator
  - [ ] No Background while locking screen **[REG: Failed]**
  - [x] Unpin Cortana from MainTab (maybe linked to a disabled service)
  - [x] Unpin OneDrive from MainTab (maybe linked to a disabled service)
  - [ ] Unpin Store from MainTab
  - [ ] Background: Solid Color/Blue **[REG: Failed]** (default values only ?)
  - * Appearences
      - [ ] Allow changing Windows Color: OFF
      - [ ] Allow Color scheme changes: OFF
      - [ ] Allow changing the font size: OFF
      - [ ] Change desktop bg: OFF
      - [ ] Allow changing screensaver: OFF
      - [ ] Effect optimizations **[REG: remains active effects]**
  * Settings:
      * System:
          - [x] Hide app icons on the taskbar in table mode: OFF
    * Devices:
      - [x] Remove Fax **[REG]**
      - [ ] Use AutoPlay for all media and devices: OFF **[REG: Failed]**
      - [x] The default printer is the last used printer: OFF **(reg)**
    * Time & Language:
      * Time zone: Europe/Paris
      * Time format:
          * First day of week: Monday
          * Short date: dd-MMM-yyyy
          * Short time: HH:mm
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
      - [x] Windows should ask for my feedback: Never [REG]
      - [ ] Apps use my advertising ID for experiences across apps [REG][?]
      - [ ] In the Speech, Inking, & Typing area: [REG][?]
      - [ ] Send your device data to Microsoft: OFF
      - [ ] Let's run Store in background: OFF
    * Update and Security:
      - [x] Help us make Windows Defender better: OFF [REG]
      - [ ] For developers: Developer mode
      - [ ] No auto-reboot with logged users: ON [REG][?]
      - [ ] Auto updates: Check but don't download [REG][?]
    * Personalization:
      - [ ] Show most used apps: OFF
      - [ ] Show recently added apps: OFF
      - [ ] Choose Which folder appear on Start: +Personal Folder
* Account
  - [ ] Administrator: Password
  - [ ] User Tom: Passwrd + Limited Account
  - [x] To prevent communication to the Microsoft Account cloud authentication service
- [x] Turn off Wi-Fi Sense that automatically connects devices to known hotspots and to the wireless networks the person’s contacts have shared with them~~

## Guest Mode
* Services:
  - [x] Remove/Disable Windows Audio
  - [x] Remove/Disable Windows Printing  Spoiler
  - [x] Remove/Disable Windows Audio Endpoin
  - [x] Remove Windows Power Management
  - [x] Disable Theme
* Custom:
  * Settings:
    * System:
      - [x] Power & Sleep, On Battery power, turn off after: Never (linked to the power service)
      - [x] Power & Sleep, When plugged in, turn off after: Never (linked to the power service)
