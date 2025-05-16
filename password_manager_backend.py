import tkinter as tk

def login(frame_login, main_frame):
    frame_login.pack_forget()
    main_frame.pack(padx=20, pady=20, fill="both", expand=True)
    
    
def logout(main_frame, frame_login, entry_master):
    main_frame.pack_forget()
    frame_login.pack(expand=True)
    entry_master.delete(0, tk.END)
    