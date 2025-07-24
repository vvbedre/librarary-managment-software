import tkinter as tk
from tkinter import messagebox
from reference_books import reference_books

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# --- In-memory student/member list ---
members = [
    {'name': 'Aarav Sharma', 'email': 'aarav.sharma@example.com', 'phone': '9876543210'},
    {'name': 'Priya Singh', 'email': 'priya.singh@example.com', 'phone': '9876543211'},
    {'name': 'Rohan Patel', 'email': 'rohan.patel@example.com', 'phone': '9876543212'},
    {'name': 'Isha Verma', 'email': 'isha.verma@example.com', 'phone': '9876543213'},
    {'name': 'Aditya Kumar', 'email': 'aditya.kumar@example.com', 'phone': '9876543214'},
    {'name': 'Sneha Nair', 'email': 'sneha.nair@example.com', 'phone': '9876543215'},
    {'name': 'Vikram Joshi', 'email': 'vikram.joshi@example.com', 'phone': '9876543216'},
    {'name': 'Ananya Reddy', 'email': 'ananya.reddy@example.com', 'phone': '9876543217'},
    {'name': 'Rahul Mehra', 'email': 'rahul.mehra@example.com', 'phone': '9876543218'},
    {'name': 'Pooja Desai', 'email': 'pooja.desai@example.com', 'phone': '9876543219'},
]

# --- In-memory issued books list ---
issued_books = []

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title('Dentistry Library Login')
        master.geometry('300x180')
        
        tk.Label(master, text='Username:').pack(pady=(20, 5))
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()
        self.username_entry.insert(0, ADMIN_USERNAME)  # Prefill username
        
        tk.Label(master, text='Password:').pack(pady=5)
        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()
        self.password_entry.insert(0, ADMIN_PASSWORD)  # Prefill password
        
        tk.Button(master, text='Login', command=self.check_login).pack(pady=15)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.master.destroy()
            open_dashboard()
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password')

def open_dashboard():
    dash = tk.Tk()
    dash.title('Dentistry Library Management')
    dash.geometry('400x350')
    tk.Label(dash, text='Library Management Dashboard', font=('Arial', 16)).pack(pady=20)
    tk.Button(dash, text='Book Management', width=25, command=open_book_management).pack(pady=10)
    tk.Button(dash, text='Member Management', width=25, command=open_member_management).pack(pady=10)
    tk.Button(dash, text='Issue/Return Books', width=25, command=open_issue_return).pack(pady=10)
    tk.Button(dash, text='Reports', width=25, command=open_reports).pack(pady=10)
    tk.Button(dash, text='Book Search', width=25, command=open_book_search).pack(pady=10)
    dash.mainloop()

# --- Section Windows ---
def open_book_management():
    win = tk.Toplevel()
    win.title('Book Management')
    win.geometry('400x350')
    tk.Label(win, text='Book Management Section', font=('Arial', 14)).pack(pady=10)

    # --- Add Book Form ---
    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text='Title:').grid(row=0, column=0, sticky='e')
    title_entry = tk.Entry(form_frame, width=30)
    title_entry.grid(row=0, column=1, pady=2)

    tk.Label(form_frame, text='Author:').grid(row=1, column=0, sticky='e')
    author_entry = tk.Entry(form_frame, width=30)
    author_entry.grid(row=1, column=1, pady=2)

    tk.Label(form_frame, text='Year:').grid(row=2, column=0, sticky='e')
    year_entry = tk.Entry(form_frame, width=30)
    year_entry.grid(row=2, column=1, pady=2)

    tk.Label(form_frame, text='ISBN:').grid(row=3, column=0, sticky='e')
    isbn_entry = tk.Entry(form_frame, width=30)
    isbn_entry.grid(row=3, column=1, pady=2)

    tk.Label(form_frame, text='Subject:').grid(row=4, column=0, sticky='e')
    subject_entry = tk.Entry(form_frame, width=30)
    subject_entry.grid(row=4, column=1, pady=2)

    def add_book():
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        year = year_entry.get().strip()
        isbn = isbn_entry.get().strip()
        subject = subject_entry.get().strip()
        if not (title and author and year and isbn and subject):
            messagebox.showerror('Error', 'All fields are required!')
            return
        try:
            year_int = int(year)
        except ValueError:
            messagebox.showerror('Error', 'Year must be a number!')
            return
        new_book = {'title': title, 'author': author, 'year': year_int, 'isbn': isbn}
        if subject in reference_books:
            reference_books[subject].append(new_book)
        else:
            reference_books[subject] = [new_book]
        messagebox.showinfo('Success', f'Book "{title}" added to subject "{subject}".')
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        year_entry.delete(0, tk.END)
        isbn_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)

    tk.Button(win, text='Add Book', command=add_book, width=20).pack(pady=10)

def open_member_management():
    win = tk.Toplevel()
    win.title('Member Management')
    win.geometry('400x300')
    tk.Label(win, text='Member Management Section', font=('Arial', 14)).pack(pady=10)

    # --- Add Student Form ---
    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text='Name:').grid(row=0, column=0, sticky='e')
    name_entry = tk.Entry(form_frame, width=30)
    name_entry.grid(row=0, column=1, pady=2)

    tk.Label(form_frame, text='Email:').grid(row=1, column=0, sticky='e')
    email_entry = tk.Entry(form_frame, width=30)
    email_entry.grid(row=1, column=1, pady=2)

    tk.Label(form_frame, text='Phone:').grid(row=2, column=0, sticky='e')
    phone_entry = tk.Entry(form_frame, width=30)
    phone_entry.grid(row=2, column=1, pady=2)

    def add_student():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        if not (name and email and phone):
            messagebox.showerror('Error', 'All fields are required!')
            return
        members.append({'name': name, 'email': email, 'phone': phone})
        messagebox.showinfo('Success', f'Student "{name}" added.')
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

    tk.Button(win, text='Add Student', command=add_student, width=20).pack(pady=10)

def open_issue_return():
    win = tk.Toplevel()
    win.title('Issue/Return Books')
    win.geometry('500x350')
    tk.Label(win, text='Issue/Return Books Section', font=('Arial', 14)).pack(pady=10)

    # --- Issue Book Form ---
    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)

    tk.Label(form_frame, text='Select Student:').grid(row=0, column=0, sticky='e')
    student_names = [m['name'] for m in members] if members else ['No students']
    student_var = tk.StringVar(value=student_names[0])
    student_menu = tk.OptionMenu(form_frame, student_var, *student_names)
    student_menu.grid(row=0, column=1, pady=2)

    tk.Label(form_frame, text='Select Book:').grid(row=1, column=0, sticky='e')
    all_titles = []
    for subject, books in reference_books.items():
        for book in books:
            all_titles.append(book['title'])
    book_var = tk.StringVar(value=all_titles[0] if all_titles else 'No books')
    book_menu = tk.OptionMenu(form_frame, book_var, *all_titles)
    book_menu.grid(row=1, column=1, pady=2)

    def issue_book():
        student = student_var.get()
        book = book_var.get()
        if student == 'No students' or book == 'No books':
            messagebox.showerror('Error', 'Please add students and books first!')
            return
        for record in issued_books:
            if record['book'] == book and record['returned'] is False:
                messagebox.showerror('Error', f'Book "{book}" is already issued!')
                return
        issued_books.append({'student': student, 'book': book, 'returned': False})
        messagebox.showinfo('Success', f'Book "{book}" issued to {student}.')

    tk.Button(win, text='Issue Book', command=issue_book, width=20).pack(pady=5)

    # --- Return Book Form ---
    tk.Label(win, text='Return Book:', font=('Arial', 12)).pack(pady=(15, 0))
    return_frame = tk.Frame(win)
    return_frame.pack(pady=5)
    issued_titles = [rec['book'] for rec in issued_books if not rec['returned']]
    return_var = tk.StringVar(value=issued_titles[0] if issued_titles else 'No issued books')
    return_menu = tk.OptionMenu(return_frame, return_var, *issued_titles)
    return_menu.grid(row=0, column=0, padx=5)

    def return_book():
        book = return_var.get()
        for record in issued_books:
            if record['book'] == book and not record['returned']:
                record['returned'] = True
                messagebox.showinfo('Success', f'Book "{book}" returned.')
                return
        messagebox.showerror('Error', 'No such issued book found!')

    tk.Button(return_frame, text='Return Book', command=return_book, width=15).grid(row=0, column=1, padx=5)

def open_reports():
    win = tk.Toplevel()
    win.title('Reports')
    win.geometry('500x400')
    tk.Label(win, text='Reports Section', font=('Arial', 14)).pack(pady=10)

    # --- Members Report ---
    tk.Label(win, text='Registered Members:', font=('Arial', 12, 'bold')).pack(anchor='w', padx=10, pady=(10, 0))
    if members:
        for m in members:
            info = f"- {m['name']} (Email: {m['email']}, Phone: {m['phone']})"
            tk.Label(win, text=info, font=('Arial', 10)).pack(anchor='w', padx=20)
    else:
        tk.Label(win, text='No members registered.', font=('Arial', 10)).pack(anchor='w', padx=20)

    # --- Issued Books Report ---
    tk.Label(win, text='\nIssued Books:', font=('Arial', 12, 'bold')).pack(anchor='w', padx=10, pady=(15, 0))
    any_issued = False
    for rec in issued_books:
        if not rec['returned']:
            info = f"- {rec['book']} (Issued to: {rec['student']})"
            tk.Label(win, text=info, font=('Arial', 10)).pack(anchor='w', padx=20)
            any_issued = True
    if not any_issued:
        tk.Label(win, text='No books currently issued.', font=('Arial', 10)).pack(anchor='w', padx=20)

# --- Book Search Window ---
def open_book_search():
    search_win = tk.Toplevel()
    search_win.title('Book Search')
    search_win.geometry('600x500')

    tk.Label(search_win, text='Search Book Title:', font=('Arial', 12)).pack(pady=(10, 0))
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_win, textvariable=search_var, width=40)
    search_entry.pack(pady=5)

    # Listbox for autocomplete suggestions
    suggestion_box = tk.Listbox(search_win, width=50, height=5)
    suggestion_box.pack(pady=(0, 10))
    suggestion_box.pack_forget()  # Hide initially

    # Frame for subject-wise listing
    list_frame = tk.Frame(search_win)
    list_frame.pack(fill='both', expand=True)

    # Flatten all book titles for autocomplete
    all_books = []
    for subject, books in reference_books.items():
        for book in books:
            all_books.append({'title': book['title'], 'subject': subject, 'author': book['author'], 'year': book['year'], 'isbn': book['isbn']})

    def update_suggestions(event=None):
        typed = search_var.get().strip().lower()
        suggestion_box.delete(0, tk.END)
        if typed:
            matches = [b['title'] for b in all_books if typed in b['title'].lower()]
            if matches:
                for title in matches:
                    suggestion_box.insert(tk.END, title)
                suggestion_box.pack()
            else:
                suggestion_box.pack_forget()
        else:
            suggestion_box.pack_forget()

    def on_suggestion_select(event):
        if suggestion_box.curselection():
            selected_title = suggestion_box.get(suggestion_box.curselection())
            search_var.set(selected_title)
            suggestion_box.pack_forget()
            show_book_details(selected_title)

    def show_book_details(title):
        for widget in list_frame.winfo_children():
            widget.destroy()
        for book in all_books:
            if book['title'] == title:
                details = f"Title: {book['title']}\nAuthor: {book['author']}\nSubject: {book['subject']}\nYear: {book['year']}\nISBN: {book['isbn']}"
                tk.Label(list_frame, text=details, font=('Arial', 12), justify='left').pack(anchor='w', padx=10, pady=10)
                break

    def show_subjectwise_list():
        for widget in list_frame.winfo_children():
            widget.destroy()
        for subject, books in reference_books.items():
            tk.Label(list_frame, text=subject, font=('Arial', 11, 'bold')).pack(anchor='w', padx=10, pady=(10, 0))
            for book in books:
                info = f"  - {book['title']} (by {book['author']}, {book['year']})"
                tk.Label(list_frame, text=info, font=('Arial', 10), justify='left').pack(anchor='w', padx=20)

    # Bindings
    search_entry.bind('<KeyRelease>', update_suggestions)
    suggestion_box.bind('<<ListboxSelect>>', on_suggestion_select)

    # Show all books subject-wise by default
    show_subjectwise_list()

    # If user presses Enter in search, show details if exact match
    def on_enter(event):
        title = search_var.get().strip()
        if title:
            for book in all_books:
                if book['title'].lower() == title.lower():
                    show_book_details(book['title'])
                    return
    search_entry.bind('<Return>', on_enter)

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop() 