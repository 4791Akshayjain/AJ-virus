## AJ Virus

⚠️ IMPORTANT WARNING
AJ Virus actively interferes with normal Windows desktop usage.
While active, the program attempts to force the user to remain on the Windows desktop by monitoring the screen and simulating keyboard commands.
AJ Virus can also re-enable itself after the system restarts.
🔓 DEACTIVATION KEY
HOLD CTRL + A + J + V AT THE SAME TIME TO DEACTIVATE AJ VIRUS.
Remember this key combination before running the program.
Use this project only on computers that you own or have explicit permission to test.


📌 About AJ Virus
AJ Virus is a simple experimental Windows desktop-control program developed using Python.
It is designed for Windows 10 and Windows 11.
The program demonstrates how Python automation tools can be used to:

Simulate keyboard input
Monitor the Windows desktop
Detect changes on the screen
Automatically react to opened applications
Control desktop interaction
Automatically run again after a system restart

While AJ Virus is active, it attempts to keep the user on the Windows desktop.
If the program detects that the user has moved away from the desktop or opened another application, it simulates keyboard commands to attempt to close the active window.

⭐ Main Features

🖥️ Designed for Windows 10 and Windows 11
⌨️ Simulates keyboard commands
👁️ Continuously monitors the desktop
❌ Attempts to close active windows
🔒 Can function as an experimental secondary desktop lock
🔄 Can re-enable itself after the Windows system restarts
🔑 Includes a secret keyboard deactivation combination
📦 Available as a compiled Windows executable
🧪 Includes both newer and older versions


🔥 #IMPORTANT: RESTART BEHAVIOUR
AJ VIRUS CAN BECOME ACTIVE AGAIN AFTER WINDOWS RESTARTS
AJ Virus includes startup-related behaviour that allows the program to run again after the system is restarted.
Pressing the deactivation key combination:
CTRL + A + J + V
stops the currently active instance of AJ Virus.
However:

⚠️ DEACTIVATING AJ VIRUS DOES NOT NECESSARILY PERMANENTLY DISABLE IT.

If its automatic startup functionality is active, AJ Virus may launch again when Windows restarts.
This allows the project to function as an experimental persistent secondary desktop lock concept.

⚙️ How It Works
When AJ Virus starts, the program performs the following basic process:


Simulates the Win + D keyboard shortcut.


Windows displays the desktop.


AJ Virus captures a screenshot of the current desktop.


The desktop screenshot is temporarily stored on the system.


The program continuously monitors the visible screen.


AJ Virus checks whether the original desktop is still visible.


If the desktop is no longer detected, the program assumes that another window or application has been opened.


AJ Virus simulates keyboard commands to attempt to close the active window.


The monitoring process continues repeatedly.


The program stops when the correct deactivation key combination is detected.


The newer version also includes image-based detection using:
kill_switch.png

🔓 How to Deactivate AJ Virus
⚠️ READ THIS BEFORE RUNNING THE PROGRAM
To deactivate the currently running AJ Virus process:
HOLD CTRL + A + J + V
All four keys must be held at the same time.
The program will exit its active control loop and stop monitoring the desktop.
Remember:

AJ Virus may become active again after the computer restarts.

The deactivation key stops the currently running instance.
It may not permanently disable automatic startup behaviour.

📥 Installation
The repository contains compiled executable versions of AJ Virus.
Python is not required when using the compiled executable versions.
🔴 Current Version
Run:
Mouse control test.exe
This is the newer and more aggressive version of AJ Virus.
Recommended for testing the latest version.

🟡 Older Version
Run:
GG_setup.exe
This is an older and less aggressive version of AJ Virus.
The older version is included for comparison and testing.

▶️ How to Use
Using AJ Virus is simple.


Download the required executable.


Save all important work.


Remember the deactivation key: CTRL + A + J + V.


Run the executable.


AJ Virus starts automatically.


The program attempts to keep the computer on the Windows desktop.


Hold CTRL + A + J + V to stop the currently running instance.



⚠️ The program may become active again after Windows restarts.


🛠️ Built With
AJ Virus was developed using:

Python
PyAutoGUI
Keyboard
OpenCV-based image recognition used by PyAutoGUI
PyInstaller
Inno Setup


📂 Project Files
GG_beta4.py
The newer version of AJ Virus.
This version contains improved screen detection logic and additional image-based detection.
It also uses:
kill_switch.png

GG_beta3.py
An older and simpler version of AJ Virus.
It contains less aggressive desktop-control behaviour compared to the newer version.

Mouse control test.exe
The compiled executable for the newer version of AJ Virus.

⚠️ This is the more aggressive version.


GG_setup.exe
Installer/executable for the older version of AJ Virus.

This version is less aggressive than the current version.


kill_switch.png
An image used by the newer version for image-based screen detection.

script2.iss and script3.iss
Inno Setup scripts used while packaging and creating executable installers for the project.

🧠 Concepts Demonstrated
AJ Virus demonstrates several Python and Windows automation concepts.
These include:

Keyboard automation
Simulated keyboard input
Screen capture
Image recognition
Screen monitoring
Desktop detection
Windows keyboard shortcuts
Continuous monitoring loops
Automatic program startup
Executable packaging
Windows installer creation


💻 Compatibility
AJ Virus is designed for:

Windows 10
Windows 11

Other operating systems are not officially supported.

🚨 SAFETY WARNING
READ BEFORE EXECUTING AJ VIRUS
AJ Virus can actively interfere with normal computer usage.
While the program is active, it may:

Close opened applications
Interrupt normal desktop usage
Simulate keyboard commands
Prevent applications from remaining open
Repeatedly return the user to the desktop
Become active again after the system restarts

Before running AJ Virus:

SAVE ALL OPEN WORK
REMEMBER CTRL + A + J + V
DO NOT RUN IT ON ANOTHER PERSON'S COMPUTER WITHOUT PERMISSION
AVOID TESTING ON IMPORTANT OR PRODUCTION SYSTEMS
USE A CONTROLLED TEST ENVIRONMENT WHEN POSSIBLE


🔑 DEACTIVATION REMINDER
CTRL + A + J + V

The developer is not responsible for interrupted work, data loss, or other problems caused by improper use of this software.

🎓 Educational Purpose
AJ Virus was created as an experimental project to explore Python desktop automation and Windows input simulation.
The project is intended for:

Learning Python automation
Experimenting with PyAutoGUI
Understanding keyboard simulation
Exploring screen and image detection
Learning Windows desktop automation
Experimenting with secondary desktop-lock concepts
Learning Python executable packaging

This project should be used in a controlled and authorized environment.

👨‍💻 Developer
Akshay Jain
GitHub Username: 4791Akshayjain

⚖️ Disclaimer
AJ Virus is provided for educational, experimental, and controlled testing purposes.
Do not use this software to interfere with computers or systems that you do not own or have explicit permission to test.
The user is fully responsible for how the software is executed and used.
By running AJ Virus, the user acknowledges that the program may interfere with normal Windows usage and may become active again after a system restart.

🔑 FINAL REMINDER

TO DEACTIVATE THE CURRENT AJ VIRUS PROCESS
HOLD CTRL + A + J + V
AJ VIRUS MAY RE-ENABLE ITSELF AFTER WINDOWS RESTARTS

Read the warning. Remember the keys. Test responsibly.
