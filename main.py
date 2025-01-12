import tkinter as tk
from tkinter import filedialog,messagebox
import os
import shutil

def select_folder():
    selected_folder = filedialog.askdirectory()
    folder_path.set(selected_folder)
    print(selected_folder)


def categories():
    return {
        'Images': ['.jpeg', '.jpg', '.png', '.gif'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv'],
        'Documents': ['.pdf', '.txt', '.xlsx', '.docx'],
        'Other': []
    }

def makeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def organize():
    source_folder = folder_path.get()

    if not source_folder:
        messagebox.showerror('ERROR' , 'Please select a folder')
        return
    try:
        for file_name in os.listdir(source_folder):
            file_path = os.path.join(source_folder , file_name);
            if os.path.isdir(file_path):
             continue
        
        file_ext = os.path.splitext(file_path)[1].lower()
        
        folder_exists = False
        
        for category , extensions in categories().items():
            folder_exists = True
            if file_ext in extensions:
                path = os.path.join(source_folder , category)
                makeDir(path)
                destination = os.path.join(path, file_name)
                shutil.move(file_name  , destination)
                break
        
        if not folder_exists:
            path = os.path.join(source_folder, 'Others')
            makeDir(path)
            destination = os.path.join(path, file_name)
            shutil.move(file_name , destination)

        messagebox.showinfo("SUCCESS" , 'Folder organized')
        
    except Exception as e:
             messagebox.showerror("Error", f"An error occurred: {e}")     


root = tk.Tk()

root.title("FILE ORGANIZER TOOL")

root.geometry("400x200")

folder_path = tk.StringVar()

tk.Label(root , text="Select Source Folder:").pack(pady=10)
tk.Entry(root, textvariable=folder_path, width=40).pack(pady=5)
tk.Button(root , text="Browse" , command=select_folder).pack(pady=5)
tk.Button(root , text="Organize Files", command=organize ,bg="green" , fg="white").pack(pady=20)

root.mainloop()