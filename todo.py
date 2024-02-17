from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do List App', font='Arial 25 bold', width=20, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task', font='Arial 18 bold', width=20, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', font='Arial 18 bold', width=20, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, width=23, bd=5, font="Arial 16 italic")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        # Add your widgets here (buttons, entry fields, etc.)

        # Add task function
        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        # Delete task function
        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if look not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)    
            file.close()

        self.button = Button(self.root, text="Add",font='sarif, 20 bold italic',
                     width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                      width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)


def main():
    root = Tk()
    u1 = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
