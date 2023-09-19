import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        update_table(df)

def update_table(data):
    for row in tree.get_children():
        tree.delete(row)
    for index, row_data in data.iterrows():
        tree.insert("", "end", values=list(row_data))

app = tk.Tk()
app.title("CSV Viewer")

frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

tree = ttk.Treeview(frame)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

btn_upload = ttk.Button(app, text="Upload CSV", command=upload_csv)
btn_upload.pack(pady=10)

app.mainloop()
