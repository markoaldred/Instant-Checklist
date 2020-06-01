#InstantChecklist.py by Nishant S

import tkinter as tk
from datetime import datetime
from datetime import date
from datetime import time

#function to_do is designed to take a list of tasks and to split them so as to
#intake multiple tasks and be able to differentiate between them using the space
#that sperates them, these tasks then are displayed in the label box
def to_do(tasks):
    list_of_tasks = tasks.split()
    lot = list_of_tasks
    label['text'] = tasks_display(lot)

#function tasks_display displays all the tasks the user has input, and can be
#constantly updated by the user as they update their remaining tasks and lets
#the user known when they have completed all their tasks
def tasks_display(lot):
    while lot:
        for task in lot:
            return (f"Remaining tasks: \n{lot}")
    else:
        return "No tasks remaining"

root = tk.Tk()


WIDTH = 800
HEIGHT = 600
bckg = tk.PhotoImage(file='bckg.png')


canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

frame = tk.Label(root,image=bckg)
frame.place(relheight=1, relwidth=1)

button = tk.Button(frame, text="UPDATE",bg='white',fg='#58f089',
                  command = lambda:to_do(entry.get()))
button.place(relx=0.785,rely=0.05, relheight=0.100,relwidth=0.2)

entry = tk.Entry(frame, text='type in tasks seperated by a space'
                ,bg="white",font=90,fg='#58f089')
entry.place(relx=0.015,rely=0.05, relheight=0.1,relwidth=0.75)

label = tk.Label(root,text='''In the box above, type in your tasks seperated by
a space \n\nAs you complete your tasks, delete them from your entry and click
\'UPDATE\' to update your list.''',font=100, fg='#58e8b4')
label.place(relx=0.015,rely=0.2,relheight =0.725,relwidth=0.97)

now = datetime.now()
current = now.strftime("%b %d,%Y")

currentTimeAndDate = tk.Label(frame,text=f"{current}",bg='#59def0',font=130,fg='white')
currentTimeAndDate.place(relx=0.3,rely=0.95,relheight=0.05,relwidth=0.425)

root.mainloop()
