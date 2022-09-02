# Change-case-of-text
A useful, small utility for changing the Case of sentences Convert to and from Lower case, Upper case, Title(First letter caps), tested on Android, Windows and Linux
---
![Version1](https://github.com/kephalian/Change-case-of-text/blob/main/Screenshot%20from%202022-08-31%2022-21-18.png)
---
![Version2](https://github.com/kephalian/Change-case-of-text/blob/main/Screenshot%20from%202022-08-31%2022-21-30.png)
---
2 builds without Regex and with Regex (re module)
## Dependency
```
import PySimpleGUI as sg
import pyperclip
import re
import sys
```
---
#### DOWNLOAD
Download PyInstaller, Windows ready EXE version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.exe)

Python source code Regex version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.exe)

Python pure String version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.py)

[Jupyter Notebook](https://github.com/kephalian/Change-case-of-text/blob/main/Calander_maker.ipynb)

Using PyInstaller and build from source using this command, same Batch file is ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/new_exe.bat) and PyINstaller SPEC file ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.spec) My Icon has to be present
in current directory for build to be successful Icon is ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/icon1.ico)

```
pyinstaller  --clean --onefile --windowed --icon=icon1.ico --upx-dir=C:\upx-3.96-win64 -y case_switch.py
pause
````
Suggestions, Comments, Errors are always solicited!
