import tkinter as tk
from tkinter import ttk
import pandas as pd


def display_sample(sample, stratification_column=None):

    print("\n" + "=" * 60)
    print("                  SAMPLE VIEW")
    print("=" * 60)

    print(f"\nSample Size : {len(sample)}")

    print("\nHow would you like to view the sample?")
    print("-" * 45)
    print("1. Short Preview")
    print("2. View Full Sample")
    print("3. Don't Display Sample")

    while True:

        choice = input("\nEnter choice: ").strip()

        if choice == "1":

            if stratification_column is not None:

                display_stratified_preview(
                    sample,
                    stratification_column
                )

            else:

                display_short_preview(sample)

            break

        elif choice == "2":

            display_full_sample(sample)

            break

        elif choice == "3":

            print("\n✅ Sample display skipped.")
            break

        else:

            print("❌ Please enter 1, 2, or 3.")


def display_short_preview(sample):

    print("\n👀 SAMPLE PREVIEW")
    print("-" * 60)

    print(
        sample.head(10).to_string(index=False)
    )

    if len(sample) > 10:

        print(
            f"\nShowing 10 of {len(sample)} records."
        )


def display_stratified_preview(
        sample,
        stratification_column
):

    print("\n" + "=" * 60)
    print("        STRATIFIED SAMPLE PREVIEW")
    print("=" * 60)

    print(
        f"\nStratification Column : "
        f"{stratification_column}"
    )

    print(
        "\nShowing records from each stratum:"
    )

    print("-" * 60)

    strata = sample[
        stratification_column
    ].dropna().unique()

    records_per_stratum = 3

    for stratum in strata:

        group = sample[
            sample[stratification_column] == stratum
        ]

        print(
            f"\n[{stratification_column}: {stratum}]"
        )

        print("-" * 60)

        preview = group.head(
            records_per_stratum
        )

        print(
            preview.to_string(index=False)
        )

        print(
            f"Showing "
            f"{min(records_per_stratum, len(group))} "
            f"records from this stratum."
        )


def display_full_sample(sample):

    root = tk.Tk()

    root.title(
        f"Full Sample - {len(sample)} Records"
    )

    root.geometry("1200x650")

    root.attributes("-topmost", True)

    frame = ttk.Frame(root)

    frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    columns = list(sample.columns)

    tree = ttk.Treeview(
        frame,
        columns=columns,
        show="headings"
    )

    for column in columns:

        tree.heading(
            column,
            text=str(column)
        )

        tree.column(
            column,
            width=150,
            minwidth=100,
            anchor="center"
        )

    for _, row in sample.iterrows():

        values = []

        for value in row:

            if pd.isna(value):

                values.append("")

            else:

                values.append(str(value))

        tree.insert(
            "",
            "end",
            values=values
        )

    vertical_scrollbar = ttk.Scrollbar(
        frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=vertical_scrollbar.set
    )

    horizontal_scrollbar = ttk.Scrollbar(
        frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(
        xscrollcommand=horizontal_scrollbar.set
    )

    tree.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    vertical_scrollbar.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    horizontal_scrollbar.grid(
        row=1,
        column=0,
        sticky="ew"
    )

    frame.rowconfigure(
        0,
        weight=1
    )

    frame.columnconfigure(
        0,
        weight=1
    )

    close_button = ttk.Button(
        root,
        text="Close",
        command=root.destroy
    )

    close_button.pack(
        pady=8
    )

    root.mainloop()