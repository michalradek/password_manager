import tkinter as tk
import sqlite3
import bcrypt
from tkinter import messagebox

conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

def check_database():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS master (
        id INTEGER PRIMART KEY ,
        passwd TEXT
        )""")
    conn.commit()

def login(frame_login, main_frame, entry_master):
    check_database()
    cursor.execute("SELECT passwd FROM master WHERE id = 1")
    master_key = cursor.fetchone()
    if len(entry_master.get()) < 6:
        messagebox.showinfo("Error", "Password must be 6 charts lenght minimum")
    else:
        if master_key is None:
            hashed = bcrypt.hashpw(entry_master.get().encode(), bcrypt.gensalt())
            cursor.execute("INSERT INTO master (id, passwd) VALUES (1, ?)", (hashed.decode(),))
            conn.commit()
            messagebox.showinfo("Info", "Master password set")
        elif bcrypt.checkpw(entry_master.get().encode(), master_key[0].encode()):
            frame_login.pack_forget()
            main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        else:
            messagebox.showinfo("Error", "Wrong master password")
    
def logout(main_frame, frame_login, entry_master):
    main_frame.pack_forget()
    frame_login.pack(expand=True)
    entry_master.delete(0, tk.END)
    
    

    
 
    