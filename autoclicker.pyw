import time
import threading
import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard
from plyer import notification

pyautogui.FAILSAFE = True

running = False
clicking = False

INTERVALS = {
    "30 seconds": 30,
    "1 minute": 60,
    "5 minutes": 300,
    "10 minutes": 600,
    "30 minutes": 1800,
    "1 hour": 3600,
}

# COLORS
BG = "#111318"
CARD = "#1A1D24"
CARD2 = "#20242C"
TEXT = "#FFFFFF"
SUBTEXT = "#9AA1AC"
GREEN = "#39D98A"
RED = "#FF5C5C"
BORDER = "#2B303A"


# NOTIFICATIONS
def notification_loop(interval):
    notification.notify(
        title="Auto-Clicker Active",
        message="Hold C to click.\nPress Q to stop.",
        app_name="AutoClicker",
        timeout=5
    )

    while running:
        for _ in range(interval):
            if not running:
                return
            time.sleep(1)

        if running:
            notification.notify(
                title="Auto-Clicker Running",
                message="The auto-clicker is still active.",
                app_name="AutoClicker",
                timeout=4
            )


# AUTO CLICKER
def click_loop():
    global running
    global clicking

    while running:
        try:
            if keyboard.is_pressed("c"):
                clicking = True

                x, y = pyautogui.position()
                pyautogui.click(x, y)

                time.sleep(0.01)
            else:
                clicking = False
                time.sleep(0.01)

        except pyautogui.FailSafeException:
            running = False
            root.after(0, emergency_stop)
            return


# START
def start_bot():
    global running

    if running:
        return

    running = True

    interval = INTERVALS[interval_var.get()]

    status_label.config(
        text="● RUNNING",
        fg=GREEN
    )

    status_description.config(
        text="Auto-clicker is active",
        fg=SUBTEXT
    )

    start_button.config(
        state="disabled"
    )

    stop_button.config(
        state="normal"
    )

    click_thread = threading.Thread(
        target=click_loop,
        daemon=True
    )

    click_thread.start()

    notification_thread = threading.Thread(
        target=notification_loop,
        args=(interval,),
        daemon=True
    )

    notification_thread.start()


# STOP
def stop_bot():
    global running
    global clicking

    if not running:
        return

    running = False
    clicking = False

    status_label.config(
        text="● STOPPED",
        fg=RED
    )

    status_description.config(
        text="Auto-clicker is not running",
        fg=SUBTEXT
    )

    start_button.config(
        state="normal"
    )

    stop_button.config(
        state="disabled"
    )

    notification.notify(
        title="Auto-Clicker Stopped",
        message="The auto-clicker has been stopped.",
        app_name="AutoClicker",
        timeout=3
    )


# EMERGENCY STOP
def emergency_stop():
    global running
    global clicking

    running = False
    clicking = False

    status_label.config(
        text="● EMERGENCY STOP",
        fg=RED
    )

    status_description.config(
        text="Mouse moved to a screen corner",
        fg=RED
    )

    start_button.config(
        state="normal"
    )

    stop_button.config(
        state="disabled"
    )

    notification.notify(
        title="Emergency Stop",
        message="Auto-clicker stopped.",
        app_name="AutoClicker",
        timeout=3
    )


# Q KEY
def check_q_key():
    if keyboard.is_pressed("q") and running:
        stop_bot()

    root.after(100, check_q_key)


# CLOSE APP
def close_app():
    global running

    running = False
    root.destroy()


# ============================================================
# GUI
# ============================================================

root = tk.Tk()

root.title("Auto-Clicker")
root.geometry("520x620")
root.configure(bg=BG)
root.resizable(False, False)


# TITLE
title = tk.Label(
    root,
    text="Auto-Clicker",
    font=("Segoe UI", 26, "bold"),
    bg=BG,
    fg=TEXT
)

title.pack(pady=(30, 3))


subtitle = tk.Label(
    root,
    text="Fast • Simple • Lightweight",
    font=("Segoe UI", 10),
    bg=BG,
    fg=SUBTEXT
)

subtitle.pack(pady=(0, 25))


# STATUS CARD
status_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

status_card.pack(
    padx=30,
    fill="x"
)


status_title = tk.Label(
    status_card,
    text="STATUS",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=SUBTEXT
)

status_title.pack(
    anchor="w",
    padx=20,
    pady=(18, 3)
)


status_label = tk.Label(
    status_card,
    text="● STOPPED",
    font=("Segoe UI", 17, "bold"),
    bg=CARD,
    fg=RED
)

status_label.pack(
    anchor="w",
    padx=20
)


status_description = tk.Label(
    status_card,
    text="Auto-clicker is not running",
    font=("Segoe UI", 9),
    bg=CARD,
    fg=SUBTEXT
)

status_description.pack(
    anchor="w",
    padx=20,
    pady=(2, 18)
)


# SETTINGS CARD
settings_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

settings_card.pack(
    padx=30,
    pady=18,
    fill="x"
)


settings_title = tk.Label(
    settings_card,
    text="SETTINGS",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=SUBTEXT
)

settings_title.pack(
    anchor="w",
    padx=20,
    pady=(18, 12)
)


notification_label = tk.Label(
    settings_card,
    text="Notification frequency",
    font=("Segoe UI", 11),
    bg=CARD,
    fg=TEXT
)

notification_label.pack(
    anchor="w",
    padx=20
)


interval_var = tk.StringVar(
    value="1 minute"
)


interval_dropdown = ttk.Combobox(
    settings_card,
    textvariable=interval_var,
    values=list(INTERVALS.keys()),
    state="readonly",
    font=("Segoe UI", 10),
    width=30
)

interval_dropdown.pack(
    padx=20,
    pady=(7, 18),
    anchor="w"
)


# CONTROLS
controls_title = tk.Label(
    root,
    text="CONTROLS",
    font=("Segoe UI", 9, "bold"),
    bg=BG,
    fg=SUBTEXT
)

controls_title.pack(
    anchor="w",
    padx=30,
    pady=(2, 10)
)


button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(
    padx=30,
    fill="x"
)


start_button = tk.Button(
    button_frame,
    text="START",
    command=start_bot,
    font=("Segoe UI", 11, "bold"),
    bg=GREEN,
    fg="#07150E",
    activebackground=GREEN,
    activeforeground="#07150E",
    relief="flat",
    bd=0,
    height=2,
    cursor="hand2"
)

start_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 7)
)


stop_button = tk.Button(
    button_frame,
    text="STOP",
    command=stop_bot,
    font=("Segoe UI", 11, "bold"),
    bg=CARD2,
    fg=TEXT,
    activebackground="#292E37",
    activeforeground=TEXT,
    relief="flat",
    bd=0,
    height=2,
    cursor="hand2",
    state="disabled"
)

stop_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(7, 0)
)


# KEYBOARD CONTROLS
hotkey_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

hotkey_card.pack(
    padx=30,
    pady=20,
    fill="x"
)


hotkey_title = tk.Label(
    hotkey_card,
    text="KEYBOARD CONTROLS",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=SUBTEXT
)

hotkey_title.pack(
    anchor="w",
    padx=20,
    pady=(18, 12)
)


hotkey_text = tk.Label(
    hotkey_card,
    text="C     Hold to auto-click\n\nQ     Stop auto-clicker",
    font=("Segoe UI", 10),
    justify="left",
    bg=CARD,
    fg=TEXT
)

hotkey_text.pack(
    anchor="w",
    padx=20,
    pady=(0, 18)
)


# EMERGENCY STOP
emergency_text = tk.Label(
    root,
    text="Move your mouse to any screen corner for EMERGENCY STOP",
    font=("Segoe UI", 9),
    bg=BG,
    fg=SUBTEXT
)

emergency_text.pack(
    pady=(0, 15)
)


# START Q CHECK
root.after(
    100,
    check_q_key
)


# CLOSE EVENT
root.protocol(
    "WM_DELETE_WINDOW",
    close_app
)


# START GUI
root.mainloop()