import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import Frame, Label

class Employee:
    def _init_(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeManagementSystem:
    def _init_(self, master):
        self.find_window = None 
        self.master = master
        self.master.title("Employee Management System | Developed by Harshitha and Aparna")
        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Set window size to fit the screen
        self.master.geometry(f"{screen_width}x{screen_height}")

        background_image = Image.open("empbg.jpg")
        background_image = background_image.resize((1900, 1200), Image.BILINEAR)
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.employees = []

        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(expand=True, fill="both")

        # Set the background image
        self.background_label = tk.Label(self.frame, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Open the image
        icon_image = Image.open("emplogo.jpg")
        desired_width = 80  
        desired_height = 80  
        icon_image = icon_image.resize((desired_width, desired_height), Image.BILINEAR)
        self.icon_label = ImageTk.PhotoImage(icon_image)
        self.label = tk.Label(self.frame, text="Welcome to Employee Management System", image=self.icon_label, compound="left", font=("Helvetica", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20, pady=10)
        self.label.pack(fill="x")

        #left menu
        leftmenu=Frame(self.master,bd=2,relief=tk.RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=920)
    
        menu=Label(leftmenu,text="Menu",height=4, font=("Helvetica",25),bg="#009688").pack(side=tk.TOP,fill=tk.X)

        self.buttons_frame = tk.Frame(self.frame, bg="#f0f0f0")
        self.buttons_frame.pack(pady=10)

        self.add_button = tk.Button(leftmenu, text="Add Employee", command=self.add_employee, bg="#4CAF50",fg="white", font=(40), height=5,width=15)
        self.add_button.pack(fill="x", padx=10, pady=10)

        self.view_button = tk.Button(leftmenu, text="View Employees", command=self.view_employees, bg="#008CBA", fg="white",font=(40), height=5,width=15)
        self.view_button.pack(fill="x", padx=10, pady=10)

        self.update_button = tk.Button(leftmenu, text="Update Employee", command=self.update_employee, bg="#f44336", fg="white",font=(40), height=5,width=15)
        self.update_button.pack(fill="x", padx=10, pady=10)

        self.delete_button = tk.Button(leftmenu, text="Delete Employee", command=self.delete_employee, bg="#FF9800", fg="white",font=(40), height=5,width=15)
        self.delete_button.pack(fill="x", padx=10, pady=10)

        self.find_button = tk.Button(leftmenu, text="Find Employees", command=self.find_employees_by_position, bg="#FFC107", fg="white",font=(40), height=5,width=15)
        self.find_button.pack(fill="x", padx=10, pady=10)

        self.quit_button = tk.Button(leftmenu, text="Quit", command=self.master.quit, bg="#555", fg="white",font=(40), height=5,width=15)
        self.quit_button.pack(fill="x", padx=10, pady=10)


    def add_employee(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Employee")
        add_window.geometry("300x200")
        add_window.configure(bg="#f0f0f0")

        fields_frame = tk.Frame(add_window, bg="#f0f0f0")
        fields_frame.pack(pady=10)

        labels_texts = ["ID:", "Name:", "Position:", "Salary:"]
        entries = []

        for i, text in enumerate(labels_texts):
            label = tk.Label(fields_frame, text=text, bg="#f0f0f0")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entry = tk.Entry(fields_frame)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            entries.append(entry)

        def add():
            try:
                employee_id = int(entries[0].get())
                name = entries[1].get()
                position = entries[2].get()
                salary = float(entries[3].get())
                 # Validating name: Only characters allowed
                if not name.isalpha():
                    raise ValueError

                # Validating salary: Only numbers allowed
                if not str(salary).replace('.', '', 1).isdigit():
                    raise ValueError
                employee = Employee(employee_id, name, position, salary)
                self.employees.append(employee)
                messagebox.showinfo("Success", "Employee added successfully")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid data.")

        add_button = tk.Button(add_window, text="Add", command=add, bg="#4CAF50", fg="white")
        add_button.pack(pady=10)

    def view_employees(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Employees")
        view_window.geometry("820x400")
        view_window.configure(bg="#f0f0f0")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Position", "Salary"), show="headings")
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Position", text="Position", anchor=tk.CENTER)
        tree.heading("Salary", text="Salary", anchor=tk.CENTER)
        tree.pack(pady=10)

        if len(self.employees) == 0:
            messagebox.showinfo("Info", "No employees found.")
        else:
            for employee in self.employees:
                tree.insert("", tk.END, values=(employee.id, employee.name, employee.position, employee.salary))

    def update_employee(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Employee")
        update_window.geometry("300x200")
        update_window.configure(bg="#f0f0f0")

        id_label = tk.Label(update_window, text="Enter ID of employee to update:", bg="#f0f0f0")
        id_label.pack(pady=5)

        id_entry = tk.Entry(update_window)
        id_entry.pack(pady=5)

        def update():
            try:
                employee_id = int(id_entry.get())
                employee = next((emp for emp in self.employees if emp.id == employee_id), None)
                if employee:
                    add_window = tk.Toplevel(self.master)
                    add_window.title("Update Employee")
                    add_window.geometry("300x200")
                    add_window.configure(bg="#f0f0f0")

                    fields_frame = tk.Frame(add_window, bg="#f0f0f0")
                    fields_frame.pack(pady=10)

                    labels_texts = ["ID:", "Name:", "Position:", "Salary:"]
                    entries = []

                    for i, text in enumerate(labels_texts):
                        label = tk.Label(fields_frame, text=text, bg="#f0f0f0")
                        label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
                        entry = tk.Entry(fields_frame)
                        entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
                        entries.append(entry)

                    # Populate fields with employee details
                    entries[0].insert(0, str(employee.id))
                    entries[1].insert(0, employee.name)
                    entries[2].insert(0, employee.position)
                    entries[3].insert(0, str(employee.salary))

                    def add():
                        try:
                            employee.id = int(entries[0].get())
                            employee.name = entries[1].get()
                            employee.position = entries[2].get()
                            employee.salary = float(entries[3].get())
                            messagebox.showinfo("Success", "Employee updated successfully")
                            add_window.destroy()
                        except ValueError:
                            messagebox.showerror("Error", "Invalid input. Please enter valid data.")

                    add_button = tk.Button(add_window, text="Update", command=add, bg="#4CAF50", fg="white")
                    add_button.pack(pady=10)

                else:
                    messagebox.showerror("Error", "Employee not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid data.")

        update_button = tk.Button(update_window, text="Update", command=update, bg="#f44336", fg="white")
        update_button.pack(pady=5)

    def delete_employee(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Employee")
        delete_window.geometry("300x200")
        delete_window.configure(bg="#f0f0f0")

        id_label = tk.Label(delete_window, text="Enter ID of employee to delete:", bg="#f0f0f0")
        id_label.pack(pady=5)

        id_entry = tk.Entry(delete_window)
        id_entry.pack(pady=5)

        def delete():
            try:
                employee_id = int(id_entry.get())
                employee = next((emp for emp in self.employees if emp.id == employee_id), None)
                if employee:
                    self.employees.remove(employee)
                    messagebox.showinfo("Success", "Employee deleted successfully")
                    delete_window.destroy()
                else:
                    messagebox.showerror("Error", "Employee not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid data.")

        delete_button = tk.Button(delete_window, text="Delete", command=delete, bg="#FF9800", fg="white")
        delete_button.pack(pady=5)

    def find_employees_by_position(self):
        find_window = tk.Toplevel(self.master)
        find_window.title("Find Employees by Position and Salary")
        find_window.geometry("500x300")
        find_window.configure(bg="#f0f0f0")

        position_label = tk.Label(find_window, text="Enter Position:", bg="#f0f0f0")
        position_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        position_entry = tk.Entry(find_window)
        position_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        salary_label = tk.Label(find_window, text="Enter Salary Range (e.g., 2000-3000):", bg="#f0f0f0")
        salary_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        salary_entry = tk.Entry(find_window)
        salary_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        def find():
            position = position_entry.get()
            salary_range = salary_entry.get()

        # Extracting salary range values if provided
            if salary_range:
                try:
                    min_salary, max_salary = map(float, salary_range.split('-'))
                except ValueError:
                    messagebox.showerror("Error", "Invalid salary range format. Please enter the range as 'min-max'.")
                    return
            else:
                min_salary, max_salary = float('-inf'), float('inf')

            found_employees = []

        # Filter employees based on position if position is provided
            if position:
                found_employees = [emp for emp in self.employees if emp.position.lower() == position.lower()]

        # Filter employees based on salary range if salary range is provided
            if salary_range:
            # If there are already filtered employees by position, use them as the starting point
                if found_employees:
                    found_employees = [emp for emp in found_employees if min_salary <= emp.salary <= max_salary]
                else:
                    found_employees = [emp for emp in self.employees if min_salary <= emp.salary <= max_salary]

            if found_employees:
                result_window = tk.Toplevel(self.master)
                result_window.title("Search Results")
                result_window.geometry("800x700")
                result_window.configure(bg="#f0f0f0")

                tree = ttk.Treeview(result_window, columns=("ID", "Name", "Position", "Salary"), show="headings")
                tree.heading("ID", text="ID", anchor=tk.CENTER)
                tree.heading("Name", text="Name", anchor=tk.CENTER)
                tree.heading("Position", text="Position", anchor=tk.CENTER)
                tree.heading("Salary", text="Salary", anchor=tk.CENTER)
                tree.pack(pady=10)

                for employee in found_employees:
                    tree.insert("", tk.END, values=(employee.id, employee.name, employee.position, employee.salary))
            else:
                messagebox.showinfo("Info", "No employees found with the given criteria.")

        find_button = tk.Button(find_window, text="Find", command=find, bg="#4CAF50", fg="white")
        find_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def main():
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()

if _name_ == "_main_":
    main()
