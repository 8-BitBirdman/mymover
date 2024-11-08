import pyautogui
import time
import random
import threading
import tkinter as tk

def move_mouse():
    while running:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Move mouse a small, random amount
        new_x = x + random.randint(-10, 10)
        new_y = y + random.randint(-10, 10)
        
        pyautogui.moveTo(new_x, new_y, duration=0.25)
        
        # Wait for a few seconds before moving again
        time.sleep(random.uniform(5, 10))

def start_mover():
    global running
    running = True
    threading.Thread(target=move_mouse, daemon=True).start()

def stop_mover():
    global running
    running = False
    root.destroy()

# Set up the Tkinter window
root = tk.Tk()
root.title("Mouse Mover")
root.geometry("300x100")
root.attributes("-topmost", True)  # Keep window on top

# Label to indicate that the script is running
label = tk.Label(root, text="Mouse Mover is Running", font=("Helvetica", 14))
label.pack(pady=20)

# Button to stop the script
stop_button = tk.Button(root, text="Stop", command=stop_mover)
stop_button.pack()

# Start the mouse mover in a separate thread
start_mover()

# Start the Tkinter main loop
root.mainloop()
