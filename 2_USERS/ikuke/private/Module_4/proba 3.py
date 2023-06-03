import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook

# Worker data
workers = {
    "prvi": "1111",
    "drugi": "2222",
    "treci": "3333"
}

# Project data
projects = {
    "rezija": "1",
    "rad": "2"
}

class TimeSheetManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Sheet Management")

        self.login_frame = LoginFrame(self)
        self.login_frame.pack()

        self.admin_frame = AdminFrame(self)
        self.worker_frame = WorkerFrame(self)

        self.admin_frame.hide()
        self.worker_frame.hide()

    def show_admin_frame(self):
        self.login_frame.hide()
        self.admin_frame.show()

    def show_worker_frame(self, username):
        self.login_frame.hide()
        self.worker_frame.show(username)

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "1234":
            self.master.show_admin_frame()
        elif username in workers and password == workers[username]:
            self.master.show_worker_frame(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack()

class AdminFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_title = tk.Label(self, text="Admin Panel")
        self.label_title.pack()

        self.label_total_hours = tk.Label(self, text="Total Hours Worked")
        self.label_total_hours.pack()

        self.button_monthly_total = tk.Button(self, text="Total Hours per Month", command=self.calculate_total_hours_per_month)
        self.button_monthly_total.pack()

        self.button_employee_total = tk.Button(self, text="Total Hours per Employee", command=self.calculate_total_hours_per_employee)
        self.button_employee_total.pack()

    def calculate_total_hours_per_month(self):
        # Add your code to calculate total hours per month
        messagebox.showinfo("Total Hours per Month", "Total hours per month calculated")

    def calculate_total_hours_per_employee(self):
        # Add your code to calculate total hours per employee
        messagebox.showinfo("Total Hours per Employee", "Total hours per employee calculated")

    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack()

class WorkerFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_title = tk.Label(self, text="Worker Panel")
        self.label_title.pack()

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
        self.label_username_value = tk.Label(self, text="")
        self.label_username_value.pack()

        self.label_date = tk.Label(self, text="Date:")
        self.label_date.pack()
        self.entry_date = tk.Entry(self)
        self.entry_date.pack()

        self.label_project = tk.Label(self, text="Project:")
        self.label_project.pack()
        self.project_var = tk.StringVar(self)
        self.project_var.set("rezija")
        self.project_dropdown = tk.OptionMenu(self, self.project_var, *projects.keys())
        self.project_dropdown.pack()

        self.label_project_id = tk.Label(self, text="Project ID:")
        self.label_project_id.pack()
        self.entry_project_id = tk.Entry(self)
        self.entry_project_id.pack()

        self.label_hours = tk.Label(self, text="Hours:")
        self.label_hours.pack()
        self.entry_hours = tk.Entry(self)
        self.entry_hours.pack()

        self.button_submit = tk.Button(self, text="Submit", command=self.submit_time_sheet)
        self.button_submit.pack()

    def show(self, username):
        self.label_username_value.config(text=username)
        self.pack()

    def hide(self):
        self.pack_forget()

    def submit_time_sheet(self):
        username = self.label_username_value.cget("text")
        date = self.entry_date.get()
        project = self.project_var.get()
        project_id = self.entry_project_id.get()
        hours = self.entry_hours.get()

        # Save time sheet entry to Excel file
        workbook = openpyxl.load_workbook("time_sheet.xlsx")
        sheet = workbook.active

        row = [username, date, project, project_id, hours]
        sheet.append(row)

        workbook.save("time_sheet.xlsx")
        messagebox.showinfo("Time Sheet Submission", "Time sheet submitted")


if __name__ == "__main__":
    # Create a new Excel file
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Username", "Date", "Project", "Project ID", "Hours"])
    workbook.save("time_sheet.xlsx")

    app = TimeSheetManagement()
    app.mainloop()
