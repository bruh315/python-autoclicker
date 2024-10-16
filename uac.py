import tkinter as tk
from tkinter import messagebox
from pyautogui import click

def perform_clicks():
    try:
        # Get the number of clicks and button type from user input
        a = int(entry_clicks.get())
        b = entry_button.get().lower()
        
        # Validate button type and perform clicks
        if b == "lmb":
            for i in range(a):
                click()
                print(f"Click: {b}, count: {i + 1}")
        elif b == "rmb":
            for i in range(a):
                click(button="right")
                print(f"Click: {b}, count: {i + 1}")
        else:
            messagebox.showerror("Error", "Invalid button type. Please enter 'LMB' or 'RMB'.")
            return

        # Success message
        messagebox.showinfo("Success", f"Performed {a} clicks with {b.upper()}.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the number of clicks.")

# Create the main window
root = tk.Tk()
root.title("Clicker Application")

# Create and place the labels and entry fields
label_clicks = tk.Label(root, text="How many times to click:")
label_clicks.pack(pady=5)

entry_clicks = tk.Entry(root)
entry_clicks.pack(pady=5)

label_button = tk.Label(root, text="LMB or RMB:")
label_button.pack(pady=5)

entry_button = tk.Entry(root)
entry_button.pack(pady=5)

# Create and place the click button
button_click = tk.Button(root, text="Start Clicking", command=perform_clicks)
button_click.pack(pady=20)

# Start the GUI event loop
root.mainloop()
