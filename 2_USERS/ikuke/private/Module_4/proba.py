import tkinter as tk

class ResistanceCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Resistance Calculator")

        self.label_r1 = tk.Label(self, text="R1 (ohm):")
        self.label_r1.grid(row=0, column=0)
        self.entry_r1 = tk.Entry(self)
        self.entry_r1.grid(row=0, column=1)

        self.label_r2 = tk.Label(self, text="R2 (ohm):")
        self.label_r2.grid(row=1, column=0)
        self.entry_r2 = tk.Entry(self)
        self.entry_r2.grid(row=1, column=1)

        self.label_result_parallel = tk.Label(self, text="Total Resistance (Parallel):")
        self.label_result_parallel.grid(row=2, column=0, columnspan=2)

        self.label_result_series = tk.Label(self, text="Total Resistance (Series):")
        self.label_result_series.grid(row=3, column=0, columnspan=2)

        self.entry_r1.bind("<KeyRelease>", self.calculate_resistances)
        self.entry_r2.bind("<KeyRelease>", self.calculate_resistances)

    def calculate_resistances(self, event):
        try:
            r1 = float(self.entry_r1.get())
            r2 = float(self.entry_r2.get())
            total_resistance_parallel = 1 / (1/r1 + 1/r2)
            total_resistance_series = r1 + r2
            self.label_result_parallel.config(text=f"Total Resistance (Parallel): {total_resistance_parallel:.2f} ohm")
            self.label_result_series.config(text=f"Total Resistance (Series): {total_resistance_series:.2f} ohm")
        except ValueError:
            self.label_result_parallel.config(text="Invalid input!")
            self.label_result_series.config(text="Invalid input!")


if __name__ == "__main__":
    app = ResistanceCalculator()
    app.mainloop()
