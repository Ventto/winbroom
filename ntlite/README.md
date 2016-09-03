NTLite
===================

# Configuration files

In `configs/`:
* **common.xml** - Personal primary configuration for Windows 7+ images.
* **w7_pro** - For Windows 7.
* **w10_guest** - For Windows 10 as guest OS.

In `registration-entries/`:
* **wb_activesetup.py** - Generate Batch file for adding HKCU subkeys in HKLM Active Setup
* **wb_reg2xml.py** - Convert REG files into XML
* `HCKU/` - REG files containing HKCU values

The config files can be used in conjunction (common.xml & w7_pro or common.xml & w10_guest).

# Custom the Windows Post-Setup Phase

It's a NTLite feature that allows you to run Batch/Powershell scripts or add [registration entrie files (.REG)](https://en.wikipedia.org/wiki/Windows_Registry#.REG_files) automatically after a Windows setup.

We could obviously take advantage of that feature to custom some configurations easier.

## Registration Entries Configuration for future users

We may need to custom some REG values for your future users.

Well-known issue, in this section we explain succintly the solution.

### Solution

>**Active Setup** is useful if you need to add an entry to HKCU for all users of a machine. It works by adding a key to HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name% with a version number. When a user logs in Windows checks this location and compares it to HKCU\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%. **If it is missing or a lower version then it runs whatever has been set in HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\%package name%\StubPath.**<br>
> -- <br><cite>[WPKG.org](https://wpkg.org/Adding_Registry_Settings#Adding_entries_to_HKCU_for_all_users)</cite>

<br> 

An example to illustrate the principe above (in REG format) :
```
[HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\SearchboxTaskbarMode]
"Version"="1"
"StrubPath"="reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search /v SearchboxTaskbarMode /d 0 /t REG_DWORD /f"

```

<br>

### Implementing the solution

**Workflow:**

* Generate (from exported REG file) or create manually a XML file containing custom HKCU subkeys and values
* Parse the XML file and generate Batch script to add values into `Active Setup`
* Import the Batch script into the Windows Post-Setup phase via NTLite

<br>

**Steps**

* **Step 0**, Exported .REG file from Windows Registry:
```
[HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search]
"SearchboxTaskbarMode"=dword:00000000
```

* **Step 1**, REG to XML:
``` 
<?xml version="1.0" encoding="utf-8"?>
<regEntries>
	<entry name="HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" >
		<value name="SearchboxTaskbarMode">
			<data>0</data>
			<dataType>REG_DWORD</dataType>
		</value>
	</entry>
<regEntries>
```
* **Step 2**, Parse the XML file and generate Batch script:
```
@echo off
reg add "HLM\SOFTWARE\Microsoft\Active Setup\Installed Components\Search_SearchboxTaskbarMode" ^
	/v "Version" ^
	/d "1" ^
	/t REG_SZ ^ 
	/f
	
reg add "HLM\SOFTWARE\Microsoft\Active Setup\Installed Components\Search_SearchboxTaskbarMode" ^
	/v "StubPath" ^
	/d "reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /v "SearchboxTaskbarMode" /d "0" /t REG_DWORD /f" ^
	/f
```
* **Step 3**, Import the script above into Post-Setup section of NTLite ([screenshot](./ntlite.jpeg))

