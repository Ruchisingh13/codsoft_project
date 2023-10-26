import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("Own To-Do List")

def task_adding():
    todo = task_add.get()
    if todo != "":
        Todo_box.insert(tkinter.END, todo)  # Changed 'todo' to 'Todo_box'
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!", message="To add a task, please enter some task !!")

def task_removing():
    try:
        index_todo = Todo_box.curselection()[0]  # Changed 'list_frame' to 'Todo_box'
        Todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!", message="To delete a task, you must select a task !!")

def task_load():
    try:
        todo_list = pickle.load(open("tasks.dat", "rb"))
        Todo_box.delete(0, tkinter.END)  # Changed 'list_frame' to 'Todo_box'
        for todo in todo_list:  # Changed 'tasks' to 'todo_list'
            Todo_box.insert(tkinter.END, todo)
    except:
        tkinter.messagebox.showwarning(title="Attention !!", message="Cannot find tasks.dat")

def task_save():
    todo_list = Todo_box.get(0, tkinter.END)  # Changed 'list_frame' to 'Todo_box'
    pickle.dump(todo_list, open("tasks.dat", "wb"))

list_frame = tkinter.Frame(window)
list_frame.pack()

Todo_box = tkinter.Listbox(list_frame, height=20, width=50)
Todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

Todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=Todo_box.yview)

task_add = tkinter.Entry(window, width=70)
task_add.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK", font=("arial", 20, "bold"), background="red", width=40, command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK", font=("arial", 20, "bold"), background="yellow", width=40, command=task_removing)
remove_task_button.pack()

load_task_button = tkinter.Button(window, text="CLICK TO LOAD TASK", font=("arial", 20, "bold"), background="green", width=40, command=task_load)
load_task_button.pack()

save_task_button = tkinter.Button(window, text="CLICK TO SAVE TASK", font=("arial", 20, "bold"), background="blue", width=40, command=task_save)
save_task_button.pack()

window.mainloop()
