from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import databaser

root = Tk()
root.title("DP Systems - Acess Panel")
root.geometry("600x300")
root.configure(background="white")
root.resizable(width=False, height=False)
# root.iconbitmap(bitmap="icons/LogoIcon.ico", default="icons/LogoIcon.ico")
# Caso queira deixar transparente
# root.atributes("-alpha", 0.9)

# Carregando imagens
logo = PhotoImage(file="icons/logo.png")

# Widgets
LeftFrame = Frame(root, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(root, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=25)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=25, show="*")
PassEntry.place(x=150, y=160)

def login():
    username = UserEntry.get()
    password = PassEntry.get()
    databaser.cursor.execute("""
    select username, password
    from usuarios 
    where username=? and password=?
    """, (username, password))
    verificaLogin = databaser.cursor.fetchone()
    if verificaLogin is not None:
        messagebox.showinfo(title="Login Info", message="Acesso confirmado")
    else:
        messagebox.showerror(title="Login Error", message="Acesso negado")

# Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=25, command=login)
LoginButton.place(x=100, y=225)


def register():
    # Removendo Widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    # Inserindo Widgets de Cadastro
    NameLabel = Label(RightFrame, text="Name:", font=("Century gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NameLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=25)
    NameEntry.place(x=150, y=15)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=25)
    EmailEntry.place(x=150, y=60)

    def registerToDatabase():
        name = NameEntry.get()
        email = EmailEntry.get()
        username = UserEntry.get()
        password = PassEntry.get()

        if name == "" or email == "" or username == "" or password == "":
            messagebox.showerror(title="Register Error", message="Preencha todos os campos")
        else:
            databaser.cursor.execute("""
            insert into usuarios(name, email, username, password)
            values (?, ?, ?, ?)
            """, (name, email, username, password))
            databaser.conn.commit()
            messagebox.showinfo(title="Register Infor", message="Registrado com sucesso")

    # Inserindo botões de cadastro
    Register = ttk.Button(RightFrame, text="Register", width=25, command=registerToDatabase)
    Register.place(x=100, y=225)

    def backToLogin():
        # Removendo widgets de cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)

        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)

        # Removendo botões da tela de cadastro
        Back.place(x=5000)
        Register.place(x=5000)

        # Readicionando botões de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=backToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=register)
RegisterButton.place(x=125, y=260)

root.mainloop()
