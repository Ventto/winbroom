TODO
============

## Common
* Components:
  * Remove Cortana (Post-Setup script: rename: "Microsoft.Windows.Cortana_cw5n1h2txyewy")
  * Remove OneDrive
  * Remove Store [NTLITE]
* Custom:
  * ~~Remove/Disable Narrator~~ 
  * No Background while locking screen [REG][FAILED]
  * ~~Unpin Cortana from MainTab (maybe linked to a disabled service)~~
  * ~~Unpin OneDrive from MainTab (maybe linked to a disabled service)~~
  * Unpin Store from MainTab
  * Background: Solid Color, Blue [REG][FAILED] (must be standard values ?)
  * Appearences
      * Allow changing Windows Color: OFF [REG][?]
      * Allow Color scheme changes: OFF [REG][?]
      * Allow changing the font size: OFF [REG][?]
      * Change desktop bg: OFF [REG][?]
      * Allow changing screensaver: OFF [REG][?]
      * Effect optimizations [REG][INCOMPLETE]
  * Settings:
      * System:
          * ~~Hide app icons on the taskbar in table mode: OFF~~
    * Devices:
      * ~~Remove Fax [REG]~~
      * Use AutoPlay for all media and devices: OFF [REG][FAILED]
      * ~~The default printer is the last used printer: OFF [REG]~~
    * Time & Language:
      * Time zone: Europe/Paris
      * Time format:
          * First day of week: Monday
          * Short date: dd-MMM-yyyy
          * Short time: HH:mm
    * Privacy:
      * Location: OFF
      * Let's app use my camera: OFF
      * Let's app use my micro: OFF
      * Let's app access my name, picture, account info: OFF
      * Let's app access my calendar: OFF (useless)
      * Let's app access call history: OFF (useless)
      * Let's app access and send email: OFF
      * Let's app read or send msgs txt or MMS: OFF (useless)
      * Let's app control radio: OFF
      * Let your apps auto share and sync info with wireless devices[...]: OFF
      * ~~Windows should ask for my feedback: Never [REG]~~
      * Apps use my advertising ID for experiences across apps [REG][?]
      * In the Speech, Inking, & Typing area: [REG][?]
      * Send your device data to Microsoft: OFF
      * Let's run Store in background: OFF
    * Update and Security:
      * ~~Help us make Windows Defender better: OFF [REG]~~
      * For developers: Developer mode
      * No auto-reboot with logged users: ON [REG][?]
      * Auto updates: Check but don't download [REG][?]
    * Personalization: 
      * Show most used apps: OFF
      * Show recently added apps: OFF
      * Choose Which folder appear on Start: +Personal Folder
* Account
  * Administrator: Password
  * User Tom: Passwrd + Limited Account
  * ~~To prevent communication to the Microsoft Account cloud authentication service~~
* ~~Turn off Wi-Fi Sense that automatically connects devices to known hotspots and to the wireless networks the person’s contacts have shared with them~~

## Guest Mode
* ~~Services:~~
  * ~~Remove/Disable Windows Audio [SERVICE]~~
  * ~~Remove/Disable Windows Printing  Spoiler [SERVICE]~~
  * ~~Remove/Disable Windows Audio Endpoin [SERVICE]~~
  * ~~Remove Windows Power Management [SERVICE]~~
  * ~~Disable Theme [SERVICE]~~
* Custom:
  * Settings:
    * System:
      * ~~Power & Sleep, On Battery power, turn off after: Never (linked to the power service)~~
      * ~~Power & Sleep, When plugged in, turn off after: Never (linked to the power service)~~
