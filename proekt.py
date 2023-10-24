import tkinter as tk
from tkinker import ttk 
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

 def init_main(self):
        toolbar = tk.Frame(bg='#d7d7d7', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    btn_add = tk.Button(toolbar, text='Добавить', bg='#d7d7d7', relief=tk.RIDGE,
                            bd=3, command=self.open_child)
        btn_add.pack(side=tk.LEFT)

    btn_upd = tk.Button(toolbar, text='Изменить', bg='#d7d7d7',
                            bd=3, command=self.open_update_child, relief=tk.RIDGE)
        btn_upd.pack(side=tk.LEFT)

    btn_del = tk.Button(toolbar, text='Удалить', bg='#d7d7d7',
                            bd=3, command=self.delete_records, relief=tk.RIDGE)
        btn_del.pack(side=tk.LEFT)

    btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d7d7',
                            bd=3, command=self.open_search, relief=tk.RIDGE)
        btn_search.pack(side=tk.LEFT)

    scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

# хранение и инициализация объектов GUI

class Update(Child):
    def __init__(self):
        super().__init__()
        self.db = db
        self.init_edit()
        self.load_data()

    def init_edit(self):
        self.title('Редактирование контакта')
        self.btn_ok.destroy()
        self.btn_ok = tk.Button(self, text='Редактировать')
        self.btn_ok.bind('<Button-1>', lambda ev: self.view.edit_record(
            self.entry_name.get(),
            self.entry_tel.get(),
            self.entry_email.get(),
            self.entry_salary.get()))
        self.btn_ok.bind('<Button-1>', lambda ev: self.destroy(), add='+')
        self.btn_ok.place(x=300, y=200)

    def load_data(self):
        self.db.cursor.execute('''SELECT * FROM users WHERE id = ?''',
                               self.view.tree.set(self.view.tree.selection()[0], '#1'))
        row = self.db.cursor.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_tel.insert(0, row[2])
        self.entry_email.insert(0, row[3])
        self.entry_salary.insert(0, row[4])

    def init_search(self):
        self.title('Найти контакт')
        self.geometry('300x100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.iconbitmap('./img/icon.ico') 
        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=30)
        self.entry_name = tk.Entry(self)
        self.entry_name.place(x=150, y=30)

#получение информации из текстовых полей

    def add_employee():
    fio = fio_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()
#вставка в базу данных

    conn.execute("INSERT INTO employees (fio, phone, email, selary) VALURS (Иванов, +79992134410, ivanov205@gmail.com, 44500)", (fio, phone, email, selary))
    conn.commit()

    def open_update_employees()
    fio = fio_combobox.get()
    phone = phone_entry.get()
    email = email_entry.get()
    salary = salary_entry.get()
#Обновление данных
    conn.execute("UPDATE employees SET phone = ?, email = ?, salary = ?, WHERE fio = ?", (phone, email, salary, fio))
    conn.commit()

    def delete_employees():
        fio_combobox.get()

conn.execute("DELETE FROM employees WHERE fio = ?", (fio))
conn.commit()

    def search_employees():
    fio = search_entry.get()
#Выполнение поиска с помощью оператора LIKE

cursor = conn.execute("SELECT * FROM employees WHERE fio LIKE ?", ('%' + fio '%'))
for row in cursor:
    print(row)
#Создание базы данных
conn = sqlite3.connect('company.db')
conn.execute("CREATE TABLE IF NOT EXISTS employees (fio TEXT, phone TEXT, email TEXT, salary REAL)")

#Главное окно и рамка

root = tk.Tk()
frame = ttk.Frome(root)
frame.pack(padx = 10, pady = 10)

#Виджет для создание сотрудника

ttk.Label(frame, text="ФИО":).grid(row = 0, column = 0, sticky = tk.W)
fio_entry = ttk.Entry(frame)
fio_entry.grid(row = 0, column = 1)

ttk.Label(frame, text="Телефон":).grid(row = 0, column = 1, sticky = tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row = 1, column = 1)

ttk.Label(frame, text="Email":).grid(row = 2, column = 0, sticky = tk.W)
email_entry = ttk.Entry(frame)
email_entry.grid(row = 2, column = 1)

ttk.Label(frame, text="Заработная плата":).grid(row = 3, column = 0, sticky = tk.W)
salary_entry = ttk.Entry(frame)
salary_entry.grid(row = 3, column = 1)

add_button = ttk.button(frame, text="добавить", command = add_employees)
add_button.grid(row = 4, column = 0, columnspan = 2 pady = 10)

#Виджет для изменение сотрудника

ttk.Label(frame, text = "Выберете сотрудника:").grid(row = 5, column = 0, sticky = tk.W)
fio_combobox = ttk.combobox(frame)
fio_combobox.grid(row = 5, column = 1)

ttk.Label(frame, text = "Телефон:").grid(row = 6, column = 0, sticky = tk.W)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row = 6, column = 1)

ttk.Label(frame, text = "Email:").grid(row = 7, column = 0, sticky = tk.W)
email_entry = ttk.Entry(frame)
email_entry.grid(row = 7, column = 1)

ttk.Label(frame, text = "Заработная плата:").grid(row = 8, column = 0, sticky = tk.W)
salary_entry = ttk.Entry(frame)
salary_entry.grid(row = 8, column = 1)

update_button = ttk.button(frame, text = "изменить", command = update_employees)
update_button.grid(row =9, column = 0, columnspan = 2, pady = 10)

#Виджет для удаление сотрудника

ttk.Label(frame, text = "Выберете сотрудника:").grid(row = 10, column = 0, sticky = tk.W)
fio_combobox = ttk.combobox(frame)
fio_combobox.grid(row = 10, column = 1)

delete_button = ttk.button(frame, text = "удалить", command = delete_employees)
delete_button.grid(row =11, column = 0, columnspan = 2, pady = 10)

#Виджет для поиска сотрудника

ttk.Label(frame, text = "Введите ФИО:").grid(row = 12, column = 0, sticky = tk.W)
search_entry = ttk.Entry(frame)
search_entry.grid(row = 12, column = 1)

search_button = ttk.Button(frame, text = "Найти", command = search_employees)
search_button.grid(row = 13, column = 0, columnspan = 2, pady = 10)

#запуск приложения

 if __name__ == '__proekt__':
    root = tk.Tk()
    db = Db()
    app = Main(root)
root.mainloop()