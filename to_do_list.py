from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def add_task():
    note=input_text.get()
    if len(note)!=0:
        taskbox.insert(END,note)
    else:
        messagebox.showinfo("warning","Please enter a task")
    text_entry.delete(0,"end")
def del_task():
     selection = taskbox.curselection()
     if len(selection)!=0:
         for i in selection[::-1]:
             taskbox.delete(i)
     else:
         messagebox.showinfo("warning","Please select a task")
def edit():
    selection = taskbox.curselection()
    if len(selection)!=0:
        edit_text=str((taskbox.get(ACTIVE)))
        input_text.set(edit_text)
        for i in selection[::-1]:
             taskbox.delete(i)
        
    else:
         messagebox.showinfo("warning","Please select a task")

def clear_tasks():
    msg_box=messagebox.showinfo("Delete All","Are you sure?")
    taskbox.delete(0,END)

    
todo= Tk()

todo.title("To-Do List")
todo['bg']='cornsilk'
todo.title('To-Do List')
todo.geometry('1000x617')
todo.resizable(0,0)

frame= Frame(todo,bg='black',width=1000,height=100).grid(row=0,columnspan=2)

Title= Label(frame,text='To-Do List',font=('Helvetica 30 bold italic'),bg='darkseagreen1',justify='center',bd=15,relief=GROOVE,height=1,width=15).grid(padx=(200,0),row=0)

Title_1= Label(text='Add the task:-',font=("Lucida Sans Unicode",20,"bold"),bg='cornsilk').grid(row=1,column=0,sticky=W,padx=(8,0))

input_text= StringVar()
text_entry= ttk.Entry(font=('Helvetica 30 '),width=35,textvariable=input_text,style='M.TEntry')
text_entry.grid(row=2,column=0,sticky=W,padx=(10,0),pady=5)

button = ttk.Button(todo, text='Add to List',style= 'M.TButton',command=add_task).grid(row=2,column=1,sticky=W)

edit= ttk.Button(todo, text='Edit',style= 'E.TButton',command=edit).grid(row=3,column=0,sticky=W,padx=(200,0))

delete= ttk.Button(todo, text='Delete',style= 'D.TButton',command=del_task).grid(row=3,column=0,sticky=E,padx=(0,215))

detele_all= ttk.Button(todo, text='Delete All',style= 'D.TButton',command=clear_tasks).grid(row=3,column=0,sticky=E,padx=(0,20))

Title_2= Label(text="Task's:-",font=("Lucida Sans Unicode",20,"bold"),bg ='cornsilk').grid(row=3,column=0,sticky=W,padx=(8,0))

taskbox = Listbox(todo,width=89,height=13,selectmode=MULTIPLE,relief=SOLID,font=('Adobe Caslon Pro', 15),borderwidth=2,bg='cornsilk')
taskbox.grid(row=4,columnspan=2,sticky=W,padx=(8,0))

scrollbar = ttk.Scrollbar(todo, orient= 'vertical')
scrollbar.grid(row=4,column=1,sticky=NS,padx=(164,0),pady=4)
taskbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=taskbox.yview)

exitbtn= Button(text='Exit',font=('Helvatic 15'),bg='brown1',bd=2,fg='black',width=10,relief=GROOVE,command=lambda:todo.destroy()).grid(row=8,column=0,padx=(0,250),pady=8,sticky=E)

style = ttk.Style()
style.configure('M.TButton',font=('Helvetica', 25),borderwidth = '20',relief='sunken',width=10,height=50)
style.configure('E.TButton',font=('Helvetica', 20))
style.configure('D.TButton',font=('Helvetica', 20))
style.configure('M.TEntry',relief='groove')
style.map('M.TEntry', lightcolor=[('focus', 'red')])
style.configure('TFrame',borderwidth='4',background='green')
style.map('M.TButton',foreground=[('pressed', 'green')],background = [('active', 'black')])
style.map('D.TButton',foreground=[('pressed', 'red')],background = [('active', 'black')])
       


todo.mainloop()
