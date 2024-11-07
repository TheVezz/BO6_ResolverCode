# BO6 Resolver Code

## Description
BO6 Resolver Code is an application that allows you to calculate and solve specific codes using X, Y and Z variables.

## Features
- Simple graphical user interface (GUI).
- Ability to choose symbols for X, Y and Z in any order

## Requirements without EXE file
- **Python 3.12** or later.
- **Pillow** for image handling.

## Usage without EXE file
- Download the source code
- Extract the compressed archive
- Run the script with python

## Building the EXE yourself
- Navigate to the file directory in the terminal
- Run in cmd "pyinstaller --noconsole --onefile --add-data "img/*.png;img" ResolverCode.py"
- If you have not set the environment variables specify the python directory, for example installed from Microsoft Store "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\python.exe -m PyInstaller --noconsole --onefile --add-data "img/*.png;img" --icon="icon.ico" ResolverCode.py"

## Usage of EXE file
- Download the EXE file
- Run the EXE file

## Procedure for using the tool
- Select the desired variable X, Y, Z (default order X,Y,Z)
- Select the symbol
- Move to the next variable
- When you enter all three you get the results
- Now you can insert the code into the game
