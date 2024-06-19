import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(file_paths, target, replacement):
    try:
        if not file_paths:
            raise ValueError("ファイルが選択されていません。")
        if not target:
            raise ValueError("置換前の文字列が入力されていません。")
        
        for file_path in file_paths:
            directory, filename = os.path.split(file_path)
            if target in filename:
                new_filename = filename.replace(target, replacement)
                new_file_path = os.path.join(directory, new_filename)
                
                if os.path.exists(new_file_path):
                    raise FileExistsError(f"ファイル '{new_file_path}' は既に存在します。")
                
                os.rename(file_path, new_file_path)
        
        messagebox.showinfo("成功", "ファイル名の置換が完了しました。")
    except FileExistsError as fee:
        messagebox.showerror("エラー", str(fee))
    except ValueError as ve:
        messagebox.showwarning("警告", str(ve))
    except PermissionError:
        messagebox.showerror("エラー", "ファイルのアクセス権がありません。管理者として実行するか、ファイルの権限を確認してください。")
    except Exception as e:
        messagebox.showerror("エラー", f"予期しないエラーが発生しました: {e}")

def select_files():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        files_entry.delete(0, tk.END)
        files_entry.insert(0, ", ".join(file_paths))

def start_renaming():
    file_paths = files_entry.get().split(", ")
    target = target_entry.get()
    replacement = replacement_entry.get()
    
    rename_files(file_paths, target, replacement)

# GUIの設定
root = tk.Tk()
root.title("ファイル名一括置換")

tk.Label(root, text="ファイル:").grid(row=0, column=0, padx=10, pady=10)
files_entry = tk.Entry(root, width=50)
files_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="選択", command=select_files).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="置換前の文字列:").grid(row=1, column=0, padx=10, pady=10)
target_entry = tk.Entry(root, width=50)
target_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="置換後の文字列:").grid(row=2, column=0, padx=10, pady=10)
replacement_entry = tk.Entry(root, width=50)
replacement_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="実行", command=start_renaming).grid(row=3, columnspan=3, pady=20)

root.mainloop()
