import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry field for user input
        self.entry_field = tk.Entry(master, width=50)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Create number buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create clear button
        tk.Button(master, text="Clear", width=10, command=self.clear_entry).grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            self.entry_field.insert(tk.END, button)

    def clear_entry(self):
        self.entry_field.delete(0, tk.END)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
