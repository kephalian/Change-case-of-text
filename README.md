# Change-case-of-text
A useful, small utility for changing the Case of sentences Convert to and from Lower case, Upper case, Title(First letter caps), tested on Android, Windows and Linux
2 builds without Regex and with Regex (re module)
## Dependency
```
import PySimpleGUI as sg
import pyperclip
import re
import sys
```
Download PyInstaller, Windows ready EXE version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.exe)
Python source code Regex version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.exe)
Python pure String version ![Here](https://github.com/kephalian/Change-case-of-text/blob/main/case_switch.py)

Using PyInstaller and build from source using this command, same Batch file is ![Here]()
```
pyinstaller  --clean --onefile --windowed --icon=icon1.ico --upx-dir=C:\upx-3.96-win64 -y case_switch.py
pause
````
