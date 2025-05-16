import tkinter as tk
from tkinter import messagebox, simpledialog
from password_manager_backend import login, logout



root = tk.Tk()
root.title("Password manager")
root.geometry("500x400")

def on_click_login():
    login(frame_login, main_frame)

def on_click_logout():
    logout(main_frame, frame_login, entry_master)


# Ekran logowanie

frame_login = tk.Frame(root)
label_login = tk.Label(frame_login, text="Enter master password: ")
entry_master = tk.Entry(frame_login, show="*")
button_login = tk.Button(frame_login, text="Zaloguj", command=on_click_login)

label_login.pack(pady=10, fill="x")
entry_master.pack(pady=5, fill="x")
button_login.pack(pady=10, fill="x")
frame_login.pack(expand=True)

# main frame

main_frame = tk.Frame(root)
label_title = tk.Label(main_frame, text="Saved passoword's")
label_title.pack()
listbox = tk.Listbox(main_frame, width=60)
listbox.pack(pady=10, expand=True, fill="both")

logout_button = tk.Button(main_frame, text="Logout", command=on_click_logout)
logout_button.place(anchor="nw")

# okno dodawania

entry_site = tk.Entry(main_frame)
entry_site.insert(0, "serwis")
entry_username = tk.Entry(main_frame)
entry_username.insert(0, "Login")
entry_password = tk.Entry(main_frame, show="*")
entry_password.insert(0, "Password")
entry_button = tk.Button(main_frame, text="Add password")


entry_site.pack(pady=10, fill="x")
entry_username.pack(pady=10, fill="x")
entry_password.pack(pady=10, fill="x")
entry_button.pack(pady=10, fill="x")

root.mainloop()
