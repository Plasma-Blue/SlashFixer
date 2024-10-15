<p align="center">
  <img src="icon.png" alt="SlashFixer Icon" width="100" height="100">
</p>

# SlashFixer
[English](README.md) | [简体中文](README_zh.md)

Automatically converts backslashes (\\) to forward slashes (/) in the Windows clipboard.

Great for Python programming on Windows. Say goodbye to backslash problems!

## Features

- Real-time clipboard monitoring
- Backslash to forward slash conversion
- System tray icon for easy access
- Visual notification of substitutions
- Instant on/off substitution

## Installation

### Option 1: Source code

1. Clone or download the repository
2. Install the dependencies: `pip install -r requirements.txt`
3. Run: `python SlashFixer.py`

### Option 2: Compiled binary

1. Download the latest release
2. Extract the zip file
3. Run SlashFixer.exe

Note: Windows Defender or other anti-virus software may report the compiled .exe as a potential threat. This is a false positive due to the nature of compiled Python applications. The executable is safe to run. If you're concerned, you can view the source code and compile it yourself using the instructions below.

## Usage

1. Run the program:
   - Source code: `python SlashFixer.py`.
   - Compiled binary: Double click on SlashFixer.exe
2. Look for the "\w/" icon in the system tray.
3. Replacement is enabled by default
4. Copy text with backslashes; they'll be replaced automatically
5. Right click on the tray icon to
   - Toggle substitution
   - Exit the program

## Compiling to binary

Create a standalone executable using Nuitka:

1. Install Nuitka: `pip install nuitka`
2. Compile: `nuitka --windows-disable-console --standalone --onefile --windows-icon-from-ico=icon.png SlashFixer.py`
3. Find the executable in the same directory

Note: Compilation may take a few minutes. The resulting file will be larger, but can be run without Python installed.

Important: Windows Defender or other anti-virus software may report the compiled .exe as a potential threat. This is a common false positive for compiled Python applications and is not a real security risk. You can safely add an exception for SlashFixer.exe in your antivirus software.

## Notes

This program only runs on Windows systems.

## Contribute

Feel free to submit bug reports and feature requests.

## License

[GNU General Public License v3.0](LICENSE)
