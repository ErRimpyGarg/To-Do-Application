from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image
import random

window = Tk()
window.geometry("500x500")
window.title("My Todo")

# For Image
# def showImage():
    
#     label.config(image=image)

# button = Button(window, text="Click me", command=showImage)
# button.pack()

# # images = ['img1.jpg', 'img2.jpg']

# Creating Image Object
# image = ImageTk.PhotoImage(Image.open('img1.jpg'))

# label = Label(window)
# label.pack()

# Entry Widget
text_lbl = Label(window, text="Add a Task:")
text_lbl.pack(pady=10)

name_ent = Entry(window)
name_ent.pack(pady=10)

def showValue():
    with open('task.txt', 'r') as f:
        tasks = f.readlines()

    for i in range(len(tasks)):
        lb.insert(i+1,f"{i+1}. {tasks[i]}")

def addTask():
    task = name_ent.get()

    if task:
        with open('task.txt','a') as f:
            f.write(f"{task}\n")
        messagebox.showinfo("Success Information", "Your task has been added!")
    else:
        messagebox.showerror("Error", "Sorry, Please add a task!")

    # Delete a listbox completely
    lb.delete(0, END)

    showValue()

def deleteTask():
    delete_index = dlt_ent.get()
    if delete_index and delete_index.isnumeric():
        with open('task.txt', 'r') as f:
            tasks = f.readlines()
        tasks.pop(int(delete_index)-1)
        with open("task.txt","w") as f:
            for task in tasks:
                f.write(task)
        messagebox.showinfo("Delete Confirmation", "You task has been deleted!")

        lb.delete(0,END) # ???? why
        showValue()

    else:
        messagebox.showerror("Delete Error", "Please perovide a valid number!")



button = Button(window,text="Add Task",command=addTask)
button.pack(pady=10)


lb = Listbox(window)

showValue()


lb.pack()



dlt_label = Label(window, text="Delete a task")
dlt_label.pack(pady=10)

dlt_label_no = Label(window, text="Enter task no from the above")
dlt_label_no.pack(pady=10)


dlt_ent = Entry(window)
dlt_ent.pack(pady=10)




dlt_button = Button(window,text="Delete Task",command=deleteTask)
dlt_button.pack(pady=10)




window.mainloop()