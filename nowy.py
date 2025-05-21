import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from password_manager_backend import login, logout, add_password, print_all, delete_position



root = tk.Tk()
root.title("Password manager")
root.geometry("1200x700")
root.resizable(False, False)


def on_click_login():
    login(login_frame, main_frame, master_entry)
    on_click_refresh()

def on_click_logout():
    logout(main_frame, login_frame, master_entry)

def on_click_add():
    add_password(entry_site, entry_username, entry_password)
    on_click_refresh()

def on_click_refresh():
    for i in tree.get_children():
        tree.delete(i)
    for line in print_all():
        tree.insert("", tk.END, values=(line[1], line[2], line[3]))

def on_tree_select(event):
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, 'values')
        details_service_var.set(values[0])
        details_login_var.set(values[1])
        details_password_var.set(values[2])
        

def on_right_click(event):
    selected_item = tree.identify_row(event.y)
    if selected_item:
        tree.selection_set(selected_item)
        popup_menu.post(event.x_root, event.y_root)

def delete_selected_item():
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item[0], 'values')
        if messagebox.askyesno("Confirm deletion", f"Delete password for {values[0]}?"):
            tree.delete(selected_item[0])
            delete_position(values[0], values[1], values[2])
        
def toggle_password_visibility():
    if details_password_entry.cget("show") == "*":
        details_password_entry.config(state="normal", show="")
    else:
        details_password_entry.config(state="normal", show="*")
    details_password_entry.config(state="readonly")
# login frame

login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Enter master password: ")
master_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Zaloguj", command=on_click_login)

login_label.pack(pady=10, fill="x")
master_entry.pack(pady=5, fill="x")
login_button.pack(pady=10, fill="x")
login_frame.pack(expand=True)

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
title_label = tk.Label(main_frame, text="Saved passoword's")
title_label.pack()

content_frame = tk.Frame(main_frame)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)
tree = ttk.Treeview(content_frame, columns=("service", "login", "password"), show="headings")
tree.heading("service", text="service")
tree.heading("login", text="login")
tree.heading("password", text="password")
tree.column("service", width=250)
tree.column("login", width=250)
tree.column("password", width=250)
tree.bind("<<TreeviewSelect>>", on_tree_select)
tree.bind("<Button-3>", on_right_click)
tree.grid(row=0, column=0, sticky="nsew")

#details frame

details_frame = tk.Frame(content_frame, borderwidth=2)
details_frame.grid(row=0, column=1, sticky="nsew", padx=(10,0))
details_label = tk.Label(details_frame, text="Details")
details_label.pack(pady=(10,20))

content_frame.columnconfigure(0, weight=0)
content_frame.columnconfigure(1, weight=0)
content_frame.rowconfigure(0, weight=1)

# service details frame 

details_service_frame = tk.Frame(details_frame)
details_service_label = tk.Label(details_service_frame, text="Service: ")
details_service_var = tk.StringVar()
details_service_entry = tk.Entry(details_service_frame, justify="left", textvariable=details_service_var, state="readonly", width=40)

details_service_frame.pack(fill="both", padx=10, pady=10)
details_service_label.grid(row=0, column=0, sticky="w", padx=(10,0))
details_service_entry.grid(row=0, column=1, sticky="e", padx=(10,0))

details_service_frame.columnconfigure(0, weight=1)
details_service_frame.columnconfigure(1, weight=1)
details_service_frame.rowconfigure(0, weight=1)

# login details frame

details_login_frame = tk.Frame(details_frame)
details_login_label = tk.Label(details_login_frame, text="Login: ")
details_login_var = tk.StringVar()
details_login_entry = tk.Entry(details_login_frame, justify="left", textvariable=details_login_var, state="readonly", width=40)

details_login_frame.pack(fill="both", padx=10, pady=10)
details_login_label.grid(row=0, column=0, sticky="w", padx=(10,0))
details_login_entry.grid(row=0, column=1, sticky="e", padx=(10,0))

details_login_frame.columnconfigure(0, weight=1)
details_login_frame.columnconfigure(1, weight=1)
details_login_frame.rowconfigure(0, weight=0)

# password details frame

details_password_frame = tk.Frame(details_frame)
details_password_label = tk.Label(details_password_frame, text="Password: ")
details_password_var = tk.StringVar()
details_password_entry = tk.Entry(details_password_frame, justify="left", textvariable=details_password_var, state="readonly", width=40, show="*")
details_password_show = tk.Button(details_password_frame, text="Show password", command=toggle_password_visibility)

details_password_frame.pack(fill="both", padx=10, pady=10)
details_password_label.grid(row=0, column=0, sticky="w", padx=(10,0))
details_password_entry.grid(row=0, column=1, sticky="e", padx=(10,0))
details_password_show.grid(row=1, column=1, sticky="nsew", padx=(10,0))

details_password_frame.columnconfigure(0, weight=1)
details_password_frame.columnconfigure(1, weight=1)
details_password_frame.rowconfigure(0, weight=0)
details_password_show.rowconfigure(1, weight=0)


# right click popup_menu

popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="delete", command=delete_selected_item)

# entry frame

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
