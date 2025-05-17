import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from password_manager_backend import login, logout, add_password, print_all



root = tk.Tk()
root.title("Password manager")
root.geometry("600x500")

def on_click_login():
    login(frame_login, main_frame, entry_master)

def on_click_logout():
    logout(main_frame, frame_login, entry_master)

def on_click_add():
    add_password(entry_site, entry_username, entry_password)

def on_click_refresh():
    for i in tree.get_children():
        tree.delete(i)
    for line in print_all():
        tree.insert("", tk.END, values=(line[1], line[2], line[3]))
    
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

top_button_frame = tk.Frame(main_frame)
top_button_frame.pack(fill="x")
logout_button = tk.Button(top_button_frame, text="Logout", command=on_click_logout)
refresh_button = tk.Button(top_button_frame, text="Refresh", command=on_click_refresh)
logout_button.grid(row=0, column=0, sticky="w", padx=10, pady=5)
refresh_button.grid(row=0, column=1, sticky="e", padx=10, pady=5)
top_button_frame.grid_columnconfigure(0, weight=1)
top_button_frame.grid_columnconfigure(1, weight=1)

label_title = tk.Label(main_frame, text="Saved passoword's")
label_title.pack()
tree = ttk.Treeview(main_frame, columns=("service", "login", "password"), show="headings")
tree.heading("service", text="service")
tree.heading("login", text="login")
tree.heading("password", text="password")
tree.column("service", width=150)
tree.column("login", width=150)
tree.column("password", width=150)
tree.pack(expand=True, fill="both", padx=10, pady=10)


# okno dodawania

entry_site = tk.Entry(main_frame)
entry_site.insert(0, "serwis")
entry_username = tk.Entry(main_frame)
entry_username.insert(0, "Login")
entry_password = tk.Entry(main_frame, show="*")
entry_password.insert(0, "Password")
entry_button = tk.Button(main_frame, text="Add password", command=on_click_add)


entry_site.pack(pady=10, fill="x")
entry_username.pack(pady=10, fill="x")
entry_password.pack(pady=10, fill="x")
entry_button.pack(pady=10, fill="x")


root.mainloop()
