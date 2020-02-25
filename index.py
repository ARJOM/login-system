from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("DP Systems - Acess Panel")
root.geometry("600x300")
root.configure(background="white")
root.resizable(width=False, height=False)
# root.iconbitmap(default="icons/LogoIcon.ico")
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

# Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=25)
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

    # Inserindo botões de cadastro
    Register = ttk.Button(RightFrame, text="Register", width=25)
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
