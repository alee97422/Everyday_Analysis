import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import pandas as pd
import tkinter as tk

root = ttk.Window(themename="solar")
root.geometry("300x600")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        display_data(df)

def display_data(df):
    # Create a new window to display the data
    data_window = tk.Toplevel()
    data_window.title("Data Preview")

    text_widget = tk.Text(data_window)
    text_widget.pack()

    # Display the first few rows of the DataFrame in the Text widget
    text_widget.insert(tk.END, df.head().to_string())

open_button = ttk.Button(root, text="Open CSV File", command=open_file)
open_button.grid(row=0, column=0, padx=10, pady=20)


b1 = ttk.Button(root, text="Initial Data Analysis", bootstyle=SUCCESS, command=display_data)
b1.grid(row=1, column=0, padx=5, pady=10)

root.mainloop()