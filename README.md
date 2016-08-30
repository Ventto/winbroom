Win-Broom
===================
Win-Broom is personal repo which contains a little assembly of scripts and configuration files to deploy an almost cleanup Windows 7+.

----------

## Assembly

### Tools

* **Chocolatey v0.10.0** -  Machine Package Manager, like apt-get for Windows
* **NTLite v1.1.0.4135** - Cutting edge Windows configuration tool **[must be installed]**

### Arborescence

- `chocolatey/choco-*.batch`: scripts to manage the auto-installation of package/software lists.
- `chocolatey/package-profiles/`:  contains the package list xml files.

- `ntlite/configs`: contains the NTLite xml config files to custom Windows features & components.
- `ntlite/registration-entries`: contains Windows registration entries configuration.

## Workflow

### NTLite 

1. Extract an original Windows iso archive and load it with NTLite
2. Import the adequate xml config files (can be used in conjunctions)
3. (Optional) add .bat, .ps1, .exe, .reg, etc... for the Post-Setup step *[(cf. Post-Setup section in ntlite/README)](https://github.com/venthom/win-broom/tree/master/ntlite/)*
3. Apply the change and create a new iso
4. Deploy the new Windows image on your machine or virtualizers.

For more details *[(cf. ntlite/README)](https://github.com/venthom/win-broom/tree/master/ntlite/)*

### Chocolatey

4. After Windows being installed, import the content of `chocolatey/` directory.
5. Dowload and install Chocolatey
6. Run the auto-installation of package lists

For more details *[(cf. chocolatey/README)](https://github.com/venthom/win-broom/tree/master/chocolatey/)*

## TODO
- Install chocolatey packages safely using [Boxstarter](http://boxstarter.org/)
- Take advantage of Boxstarter to custom Windows (like REG entries for instance) easier.
	- Remove useless chocolatey Batch scripts.
	- Use the [Lauch from the Web technique](http://boxstarter.org/WebLauncher).
-  (If Boxstarter does not custom enough): 
	- Create a Batch/PS script that would parse a XML in which HKCU entries (subkeys and values) are declared.
	- The script would use REG.EXE to add HKLM/Active Setup subkeys accordingly to apply the change for all users. 
	- Both files would be imported via NTLite in Post-Setup phase. *[(cf. HKCU for all users section in ntlite/README)](https://github.com/venthom/win-broom/tree/master/ntlite/)*
