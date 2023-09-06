import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class TrainingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Training GUI")

        # Load the JSON file
        with open("train.json", "r") as f:
            self.config = json.load(f)

        # Create and place the widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a label and entry for each key in the JSON
        row = 0
        col = 0
        self.entries = {}
        for key, value in self.config.items():
            label = tk.Label(self.root, text=key)
            label.grid(row=row, column=col, sticky="w", padx=10, pady=5)

            # Display value without quotation marks if it's a string
            display_value = value if not isinstance(value, str) else value
            entry = tk.Entry(self.root)
            entry.insert(0, str(display_value))
            entry.grid(row=row, column=col+1, padx=10, pady=5)
            self.entries[key] = entry

            # Update row and column for next widget
            if col < 2:
                col += 2
            else:
                col = 0
                row += 1

        # Create a start button
        start_button = tk.Button(self.root, text="Start Training", command=self.start_training)
        start_button.grid(row=row+1, column=0, columnspan=4, pady=20)

    def start_training(self):
        # Update the JSON file with the values from the entries
        for key, entry in self.entries.items():
            value = entry.get()
            try:
                # Convert string values to their respective types (int, float, bool, null)
                self.config[key] = json.loads(value)
            except json.JSONDecodeError:
                # If it's not a recognized type, treat it as a string
                self.config[key] = value

        # Save the updated JSON
        with open("train.json", "w") as f:
            json.dump(self.config, f, indent=4)

        # Run the training command
        os.system("python train.py --config train.json")
        messagebox.showinfo("Info", "Training started!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingGUI(root)
    root.mainloop()
