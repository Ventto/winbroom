Choco
===================
Here is resting the Chcolatey config files and Batch scripts to setup the ensemble.

----------

## Configuration files

In `./package-profiles/`:

* **base.config** - short list of vital packages
* **common.config** - shared by all Windows images
* **host.config** - packages only for host Windows
* **own.config** - personal packages

## Batch scripts

1. **choco-download.bat** - download and install a temporary Chocolatey
2. **choco-setup.bat** - install chocolately the Chocolatey package 
3. **choco-install-packages** - install package lists in `./package-profiles/`
