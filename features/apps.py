import subprocess
import platform
import os

def open_notepad():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["notepad.exe"])
        else:
            os.system("gedit")  # For Linux as fallback
    except Exception as e:
        print(f"❌ Failed to open Notepad: {e}")

def open_calculator():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["calc.exe"])
        else:
            os.system("gnome-calculator")  # Linux fallback
    except Exception as e:
        print(f"❌ Failed to open Calculator: {e}")
