import pandas as pd
import tkinter as tk
from tkinter import filedialog


def load_dataset():

    print("\n" + "=" * 60)
    print("                    LOAD DATASET")
    print("=" * 60)

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = filedialog.askopenfilename(
        parent=root,
        title="Select Your Dataset",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx *.xls"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        print("\n⚠ No file selected.")
        root.destroy()
        return None

    try:

        if file_path.lower().endswith(".csv"):
            data = pd.read_csv(file_path)

        elif file_path.lower().endswith((".xlsx", ".xls")):
            data = pd.read_excel(file_path)

        else:
            print("\n❌ Unsupported file format.")
            root.destroy()
            return None

        if data.empty:
            print("\n❌ Dataset is empty.")
            root.destroy()
            return None

        print("\n✅ Dataset loaded successfully!")
        print(f"Rows    : {data.shape[0]}")
        print(f"Columns : {data.shape[1]}")

        root.destroy()

        return data

    except Exception as e:

        print("\n❌ Error loading dataset:")
        print(e)

        root.destroy()
        return None