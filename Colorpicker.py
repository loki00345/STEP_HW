import tkinter as tk

class ColorPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker")

        # Create a table
        self.table = tk.Frame(self.root)
        self.table.pack()

        # Colors
        colors = [
            {"name": "Red", "hex": "#FF0000"},
            {"name": "Green", "hex": "#00FF00"},
            {"name": "Blue", "hex": "#0000FF"},
            {"name": "Yellow", "hex": "#FFFF00"},
            {"name": "Purple", "hex": "#800080"},
            {"name": "Pink", "hex": "#FFC0CB"},
            {"name": "Orange", "hex": "#FFA500"},
            {"name": "Black", "hex": "#000000"},
            {"name": "White", "hex": "#FFFFFF"},
            {"name": "Gray", "hex": "#808080"}
        ]

        self.create_color_rows(colors)

    def create_color_rows(self, colors):
        for i, color in enumerate(colors, start=1):
            self.create_color_row(i, color)

    def create_color_row(self, row, color):
        
        name_label = tk.Label(self.table, text=color["name"])
        name_label.grid(row=row, column=0)

        
        preview_label = tk.Label(self.table, bg=color["hex"], width=10, height=1)
        preview_label.grid(row=row, column=1)

        
        code_label = tk.Label(self.table, text=color["hex"])
        code_label.grid(row=row, column=2)

if __name__ == "__main__":
    root = tk.Tk()
    color_picker = ColorPicker(root)
    root.mainloop()
