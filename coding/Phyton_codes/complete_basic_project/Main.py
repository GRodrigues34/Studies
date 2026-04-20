from Frontend import *
import Backend as core

app = None

def view_command():
    print("button click")
    rows = core.view()
    app.listClients.delete(0,END)
    for r in rows:
        app.listClients.insert(END,r)
    
def search_command():
    app.listClients.delete(0,END)

    rows = core.search(app.txtName.get(), app.txtSecondName.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClients.insert(END, r)

def post_command():
    core.insert(app.txtName.get(), app.txtSecondName.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()    

def update_command():
    core.update(selected[0],app.textName.get(),app.txtSecondName.get(),app.txtEmail.get(),app.txtCPF.get())
    view_command

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listClients.curselection()[0]
    selected = app.listClients.get(index)
    app.entName.delete(0,END)
    app.entName.insert(END,selected[1])
    app.entSecondName.delete(0,END)
    app.entSecondName.insert(END,selected[2])
    app.entEmail.delete(0,END)
    app.entEmail.insert(END,selected[3])
    app.entCPF.delete(0,END)
    app.entCPF.insert(END,selected[4])
    return selected

if __name__ == "__main__":
    app = Gui()
    app.listClients.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnSearch.configure(command=search_command)
    app.btnPost.configure(command=post_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
    