import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def on_login():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Login attempt with username: {username}, password: {password}")


# Create the main application window
top = tk.Tk()
top.title("Login Form")
top.geometry("400x400")

# Apply a themed style
style = ThemedStyle(top)
style.set_theme("radiance")

# Create and pack widgets
label_username = ttk.Label(top, text="Username:")
label_username.pack(pady=5)

entry_username = ttk.Entry(top)
entry_username.pack(pady=5)

label_password = ttk.Label(top, text="Password:")
label_password.pack(pady=5)

entry_password = ttk.Entry(top, show="*")  # Use show="*" to hide the password
entry_password.pack(pady=5)

login_button = ttk.Button(top, text="Login", command=on_login)
login_button.pack(pady=10)

# Run the Tkinter main loop
top.mainloop()
