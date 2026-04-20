from tkinter import * 

class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30


    window = Tk()
    window.wm_title("PYSQL v1")

    txtName = StringVar()
    txtSecondName = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    # Criando os objetos que farão parte das janelas

    lblname        = Label(window, text="name")
    lblSecondName   = Label(window, text="SecondName")
    lblemail       = Label(window, text="Email")
    lblcpf         = Label(window, text="CPF")
    entName        = Entry(window, textvariable=txtName, width=width_entry)

    entSecondName   = Entry(window, textvariable=txtSecondName, width=width_entry)
    entEmail       = Entry(window, textvariable=txtEmail, width=width_entry)
    entCPF         = Entry(window, textvariable=txtCPF, width=width_entry)
    listClients   = Listbox(window, width=100)
    scrollClients = Scrollbar(window)
    btnViewAll     = Button(window, text="See All")
    btnSearch      = Button(window, text="Search")
    btnPost     = Button(window, text="Post")
    btnUpdate      = Button(window, text="Update Selected")
    btnDel         = Button(window, text="Delete Selected")
    btnClose       = Button(window, text="Close")

    lblname.grid(row=0, column=0)
    lblSecondName.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblcpf.grid(row=3, column=0)
    entName.grid(row=0, column=1, padx=50, pady=50)
    entSecondName.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClients.grid(row=0, column=2, rowspan=10)
    scrollClients.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnSearch.grid(row=5, column=0, columnspan=2)
    btnPost.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    listClients.configure(yscrollcommand=scrollClients.set)
    scrollClients.configure(command=listClients.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def run(self):
        Gui.window.mainloop()

