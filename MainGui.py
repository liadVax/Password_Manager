import  tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import Safe as sf
import Encrypter as enc


#Functions
#submit a line to the file connected to the submit button
def submit_data():
    site=entry_site.get()
    username=entry_username.get()
    password=entry_password.get()
    if len(site)==0:
        entry_site.focus()
        messagebox.showerror('Error','Please fill in Site field')
        return
    elif len(username) == 0:
        entry_username.focus()
        messagebox.showerror('Error', 'Please fill in Username field')
        return
    elif len(password) == 0:
        entry_password.focus()
        messagebox.showerror('Error', 'Please fill in Password field')
        return
    safe=sf.data_lines()
    safe.add_data_to_file(site,username,password)
    entry_site.delete(0,'end')
    entry_username.delete(0,'end')
    entry_password.delete(0,'end')
    read_data()

#delete a line from the file connected to delete button
def delete_data():
    item=tree.selection()
    if not item:
        return
    selected_items =tree.item(item)['values'][0]
    safe=sf.data_lines()
    safe.deleted_lines(selected_items)
    read_data()

#reads all the data from the file and update the gui
def read_data():
    file = open("MySafe.txt", 'a+') #if file not exist
    file.close()
    for row in tree.get_children():
        tree.delete(row)
    file=open("MySafe.txt",'r')
    count=0
    for line in file:
        line_data=line.split(',')
        insert_data_to_gui(tree,line_data[1],line_data[2],line_data[3].strip('\n'),count)
        count+=1
    file.close()

#after submiting data to the file add the data to the gui
def insert_data_to_gui(tree,site,user,password,row):
    s=enc.dencrypt(site)
    u = enc.dencrypt(user)
    p = enc.dencrypt(password)
    tree.insert('','end',values=(str(row),s,u,p))

#deletes all the data from the file connected to clear all button
def clear_all():
    if len(tree.get_children())!=0:
        ans=messagebox.askquestion('Clear All','Are you sure you want to clear all?')
        if ans=='yes':
            safe=sf.data_lines()
            safe.clear_all()
            read_data()


#gui window
root=tk.Tk()
root.geometry('400x350')
root.resizable(0,0)
root.title("MySafe")

main_frame=tk.Frame(root,bg='#7F8C8D')
main_frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#top label
title=tk.Label(main_frame,text="~ MySafe ~",bg='#7F8C8D',justify=tk.CENTER,font=('Times New Roman', 16,'bold'))
title.pack()

#frame for the entries and label
frame_detail=tk.LabelFrame(main_frame,bd=10,width=300,height=100,relief=tk.RIDGE)
frame_detail.pack(side='top',fill='both')
#labels
label_site=tk.Label(frame_detail,text="Site",bd=7,font=('Arial', 10,'bold'))
label_site.grid(row=0,column=0,sticky='W')
label_username=tk.Label(frame_detail,text="Username",bd=7,font=('Arial', 10,'bold'))
label_username.grid(row=1,column=0,sticky='W')
label_password=tk.Label(frame_detail,text="Password",bd=7,font=('Arial', 10,'bold'))
label_password.grid(row=2,column=0,sticky='W')
#entries
entry_site=ttk.Entry(frame_detail,width=40)
entry_site.grid(row=0,column=1,padx=2,pady=2)
entry_username=ttk.Entry(frame_detail,width=40)
entry_username.grid(row=1,column=1,padx=4,pady=2)
entry_password=ttk.Entry(frame_detail,width=40)
entry_password.grid(row=2,column=1,padx=4,pady=2)
frame_detail.columnconfigure(1, weight=1)
frame_detail.rowconfigure(1, weight=1)
#frame for the buttons
frame_button=tk.Frame(main_frame,bg='#7F8C8D')
frame_button.pack()
#buttons
button_submit=tk.Button(frame_button, text='Submit', width=10,command=submit_data)
button_submit.grid(row=1,column=1,pady=5,padx=20)
button_delete=tk.Button(frame_button,text='Delete',width=10,command=delete_data)
button_delete.grid(row=1,column=0,pady=5,padx=20)
button_delete=tk.Button(frame_button,text='Clear all',width=10,command=clear_all)
button_delete.grid(row=1,column=2,pady=5,padx=20)
#treeview with the data
tree=ttk.Treeview(main_frame,height=10,selectmode='browse', show=["headings"])
tree.pack(side=tk.TOP,fill='both')
tree["columns"]=("index","site","username","password")
tree["displaycolumns"]=("site","username","password")
tree.heading("#0",text="",anchor="w")
tree.column("#0",anchor="center",width=0,stretch=tk.NO)
tree.heading("site",text="site")
tree.column("site",anchor="center",width=100,stretch=tk.NO)
tree.heading("username",text="username")
tree.column("username",anchor="center",width=150,stretch=tk.NO)
tree.heading("password",text="password")
tree.column("password",anchor="center",width=150,stretch=tk.NO)

#scroll bar
scroll = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
scroll.place(relx=1, rely=1,height=143, anchor='se')



read_data()
root.mainloop()
