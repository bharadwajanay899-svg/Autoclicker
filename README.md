# Auto-Clicker

A simple, lightweight Python auto-clicker with a modern GUI.

## Features

* Modern dark-themed GUI
* Hold **C** to auto-click
* Press **Q** to stop
* Move the mouse to a screen corner for the PyAutoGUI emergency stop
* Adjustable notification frequency
* Background notifications
* Start and Stop buttons
* No command-line menu
* Lightweight and easy to use

## Requirements

* Windows
* Python 3.13 (64-bit)
* PyAutoGUI
* Keyboard
* Plyer
* Tkinter

## Installation

### 1. Install Python

Install **Python 3.13 (64-bit)**.

Make sure Python is added to PATH during installation.

### 2. Install required packages

Open Command Prompt or the VS Code terminal and run:

```bash
python -m pip install pyautogui keyboard plyer
```

### 3. Download the project

Put these files in the same folder:

```text
AutoClicker/
│
├── autoclicker.pyw
└── README.md
```

## Running the Auto-Clicker

Double-click:

```text
autoclicker.pyw
```

The GUI should open without showing a Command Prompt window.

You can also run it from a terminal while testing:

```bash
python autoclicker.pyw
```

## How to Use

### Start

1. Open `autoclicker.pyw`.
2. Choose your notification frequency.
3. Click **START**.
4. Hold **C** wherever you want to click.

### Stop

You can stop the auto-clicker in three ways:

* Click **STOP**
* Press **Q**
* Move your mouse to a screen corner to trigger the emergency stop

## Notification Frequency

The GUI currently provides:

```text
30 seconds
1 minute
5 minutes
10 minutes
30 minutes
1 hour
```

The selected interval controls how frequently the program sends background status notifications.

## Click Speed

The auto-clicker uses:

```python
time.sleep(0.02)
```

This is approximately:

```text
50 clicks per second
```

To change the click speed, modify the value in `click_loop()`.

For example:

```python
time.sleep(0.05)
```

would result in approximately:

```text
20 clicks per second
```

## Emergency Stop

PyAutoGUI's failsafe is enabled:

```python
pyautogui.FAILSAFE = True
```

Moving the mouse to a screen corner can trigger the failsafe while PyAutoGUI is active.

The GUI will display:

```text
● EMERGENCY STOP
```

## Project Structure

```text
AutoClicker/
│
├── autoclicker.pyw
└── README.md
```

### `autoclicker.pyw`

The main application containing:

* GUI
* Auto-clicking
* Keyboard controls
* Notifications
* Emergency stop
* Settings

### `README.md`

Project documentation and usage instructions.

## Troubleshooting

### `Import "plyer" could not be resolved`

Install Plyer:

```bash
python -m pip install plyer
```

Then make sure VS Code is using:

```text
Python 3.13 (64-bit)
```

You can check Plyer with:

```bash
python -c "from plyer import notification; print('PLYER WORKS')"
```

### The GUI does not appear

Try running:

```bash
python autoclicker.pyw
```

If there is an error, temporarily rename the file to:

```text
autoclicker.py
```

and run:

```bash
python autoclicker.py
```

This allows you to see errors in the terminal.

## License

This project is provided for personal and educational use.

You are free to modify the source code for your own projects.

## Disclaimer

Use the auto-clicker responsibly. Some games, websites, and applications may prohibit automation or auto-clicking. Check the applicable rules before using it.

## Author

Created as a Python GUI auto-clicker project.
