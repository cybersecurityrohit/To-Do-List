from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
                        font=('Arial', 25, 'bold'), width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font=('Arial', 18, 'bold'), width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=50)

        self.label3 = Label(self.root, text='Task',
                            font=('Arial', 18, 'bold'), width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font=("Arial", 20, "italic bold"))
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root, bd=5, height=2, width=24, font=('Arial', 10, 'bold'))
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                task = self.main_text.get(delete_)
                self.main_text.delete(delete_)
                
                with open('data.txt', 'r') as f:
                    lines = f.readlines()
                
                with open('data.txt', 'w') as f:
                    for line in lines:
                        if task.strip() != line.strip():
                            f.write(line)

        try:
            with open('data.txt', 'r') as file:
                read = file.readlines()
                for task in read:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass

        self.button_add = Button(self.root, text="Add", font=('Arial', 20, 'bold italic'),
                                width=9, bd=5, bg='orange', fg='black', command=add)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text="Delete", font=('Arial', 20, 'bold italic'),
                                    width=9, bd=5, bg='orange', fg='black', command=delete)
        self.button_delete.place(x=30, y=260)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
