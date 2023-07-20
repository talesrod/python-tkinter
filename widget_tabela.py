import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

#define columns
columns = ('first_name','last_name','email')

table =  ttk.Treeview(root,columns=columns,show='headings')

#define headings
table.heading('first_name',text='First Name')
table.heading('last_name',text='Last Name')
table.heading('email',text='Email')

#generate sample data
contacts=[]
for n in range(1,100):
    contacts.append((f'first {n}',f'last {n}',f'email{n}@example.com'))

#add data to the treeview
for contact in contacts:
    table.insert('',tk.END,values=contact)


def item_selected(event):
    for selected_item in table.selection():
        item = table.item(selected_item)
        record = item['values']
        #show a message
        showinfo(title='Information',message=','.join(record))


table.bind('<<TreeviewSelect>>',item_selected)

table.grid(row=0,column=0,sticky='nsew')

#add a scrollbar
scrollbar = ttk.Scrollbar(root,orient=tk.VERTICAL,command=table.yview)
table.configure(yscroll = scrollbar.set)
scrollbar.grid(row=0,column=1,sticky='ns')

#run the app
root.mainloop()