import tkinter as tk
import sqlite3
import bcrypt
from tkinter import messagebox

conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

def check_database(table_name, column):
    allowed_tables = {"master", "list"}
    if table_name not in allowed_tables:
        raise ValueError("Invalid table name")
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        {column}
        )""")
    conn.commit()

def login(frame_login, main_frame, entry_master):
    check_database("master", "id INTEGER PRIMARY KEY, passwd BLOB")
    cursor.execute("SELECT passwd FROM master WHERE id = 1")
    master_key = cursor.fetchone()
    if len(entry_master.get()) < 6:
        messagebox.showinfo("Error", "Password must be at least 6 characters long.")
    else:
        if master_key is None:
            hashed = bcrypt.hashpw(entry_master.get().encode(), bcrypt.gensalt())
            cursor.execute("INSERT INTO master (id, passwd) VALUES (1, ?)", (hashed,))
            conn.commit()
            messagebox.showinfo("Info", "Master password set")
        elif bcrypt.checkpw(entry_master.get().encode(), master_key[0]):
            frame_login.pack_forget()
            main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            messagebox.showinfo("Error", "Wrong master password")
    
def logout(main_frame, frame_login, entry_master):
    main_frame.pack_forget()
    frame_login.pack(expand=True)
    entry_master.delete(0, tk.END)
    
def add_password(entry_site, entry_username, entry_password):
    check_database("list", "id INTEGER PRIMARY KEY, service TEXT, login TEXT, password TEXT")
    cursor.execute("""
        INSERT INTO list (service, login, password) VALUES (?, ?, ?)
    """, (entry_site.get(), entry_username.get(), entry_password.get()))
    conn.commit()
    messagebox.showinfo("Info", "Credentials added")

def delete_position(service, login, password):
    check_database("list", "id INTEGER PRIMARY KEY, service TEXT, login TEXT, password TEXT")
    cursor.execute("""
        DELETE FROM list WHERE service=? AND login=? AND password=?""", (service, login, password))
    conn.commit()
    messagebox.showinfo("Info", "Credentials deleted")
    
def print_all():
    check_database("list", "id INTEGER PRIMARY KEY, service TEXT, login TEXT, password TEXT")
    cursor.execute("SELECT * FROM list")
    wyniki = cursor.fetchall()
    return wyniki
    
    
    
    

    
 
    