import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    if score <= 2:
        return "Weak", "red"
    elif score == 3 or score == 4:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    strength, color = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

title_label = tk.Label(frame, text="Enter Password:", font=("Arial", 12))
title_label.pack()

entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

check_button = tk.Button(frame, text="Check Strength", command=on_check, font=("Arial", 12))
check_button.pack()

result_label = tk.Label(frame, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
