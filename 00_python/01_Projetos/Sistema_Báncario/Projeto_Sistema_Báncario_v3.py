from cgitb import text
from textwrap import fill
import customtkinter

global usuarios
usuarios = []


class WalletApp(customtkinter.CTk):

    def __init__(self):

        super().__init__()
        self.geometry("600x500")
        self.title("Pugnator Wallet")
        customtkinter.set_appearance_mode("dark")

        # Container onde as telas ficam
        self.container = customtkinter.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Guardar telas criadas
        self.frames = {}

        # Mostra a tela inicial (LoginPage)
        self.show_frame(WalletLogin)

    def show_frame(self, tela_class):
        """Mostra a tela desejada"""
        if tela_class not in self.frames:
            frame = tela_class(self.container, self)
            self.frames[tela_class] = frame
        else:
            frame = self.frames[tela_class]

        # Esconde todas as telas
        for f in self.frames.values():
            f.pack_forget()

        # Mostra a escolhida
        frame.pack(fill="both", expand=True)


class WalletLogin(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.label0 = customtkinter.CTkLabel(
            self,
            text="Sistema Bancário v3.0",
            font=("Arial", 15),
            text_color="grey"
        )
        self.label0.grid(row=2, column=1, pady=(190, 5))

        self.label1 = customtkinter.CTkLabel(
            self,
            text="Login",
            font=("Arial", 19),
            text_color="green"
        )
        self.label1.grid(row=1, column=1, pady=1)

        self.entry_username = customtkinter.CTkEntry(
            self,
            placeholder_text="     CPF do usuário"
        )
        self.entry_username.grid(row=1, column=1, pady=(80, 5))

        self.entry_password = customtkinter.CTkEntry(
            self,
            placeholder_text="     Senha do usuário",
            show="*"  # opcional para esconder senha
        )
        self.entry_password.grid(row=1, column=1, pady=(160, 5))

        self.button3 = customtkinter.CTkButton(
            self,
            text="O",
            width=25,
            height=25,
            command=lambda: self.entry_password.configure(
                show="" if self.entry_password.cget("show") == "*" else "*")
        )
        self.button3.grid(row=1, column=1, pady=(160, 5), padx=(175, 0))

        self.button0 = customtkinter.CTkButton(
            self,
            text="Entrar",
            command=self.login
        )
        self.button0.grid(row=1, column=1, pady=(240, 5))

        self.button1 = customtkinter.CTkButton(
            self,
            text="Cadastrar-se",
            command=lambda: controller.show_frame(RegisterPage))

        self.button1.grid(row=2, column=2, pady=(190, 5))

        self.button2 = customtkinter.CTkButton(
            self,
            text="Sair ",
            command=self.controller.destroy  # aqui melhor usar o controller
        )
        self.button2.grid(row=2, column=0, pady=(190, 5))

    def login(self):
        cpf = self.entry_username.get()
        senha = self.entry_password.get()

        for usuario in usuarios:
            if cpf == usuario["CPF"] and senha == usuario["senha"]:
                self.entry_username.delete(0, 'end')
                self.entry_password.delete(0, 'end')
                self.controller.show_frame(HomePage)
                return

        self.label1.configure(text="Login inválido!", text_color="#ff6666")
        self.label1.after(5000, lambda: self.label1.configure(
            text="Login", text_color="green"))


class RegisterPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        global usuarios
        usuarios = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.entry_nome = customtkinter.CTkEntry(
            self,
            placeholder_text="     Nome do usuário",
        )
        self.entry_nome.grid(row=0, column=1, pady=(0, 140))

        self.entry_born_date = customtkinter.CTkEntry(
            self,
            placeholder_text="  Data de nascimento",
        )
        self.entry_born_date.grid(row=0, column=1, pady=(0, 70))

        self.entry_cpf = customtkinter.CTkEntry(
            self,
            placeholder_text="     CPF do usuário",
        )
        self.entry_cpf.grid(row=0, column=1, pady=(0, 0))

        self.entry_address = customtkinter.CTkEntry(
            self,
            placeholder_text="     Qual seu estado?",
        )
        self.entry_address.grid(row=0, column=1, pady=(70, 0))

        self.entry_password = customtkinter.CTkEntry(
            self,
            placeholder_text="     Senha do usuário",
        )
        self.entry_password.grid(row=0, column=1, pady=(140, 5))

        self.button = customtkinter.CTkButton(
            self,
            text="Criar conta",
            command=self.validate
        )
        self.button.grid(row=0, column=1, pady=(210, 5))

        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=2, column=1, pady=(0, 0))

        self.button = customtkinter.CTkButton(
            self,
            text="Voltar",
            command=lambda: [self.label.configure(
                text=""), controller.show_frame(WalletLogin)]
        )
        self.button.grid(row=3, column=0, pady=(0, 0))

        self.button = customtkinter.CTkButton(
            self,
            text="REGRAS",
            command=lambda: controller.show_frame(WalletLogin)
        )
        self.button.grid(row=3, column=2, pady=(0, 0))

    def validate(self):
        nome = self.entry_nome.get()
        born_date = self.entry_born_date.get()
        cpf = self.entry_cpf.get()
        address = self.entry_address.get()
        password = self.entry_password.get()

        # -----------------------------------------------------------------------------------

        if born_date.isdigit() and len(born_date) == 8:
            born_date = f"{born_date[:2]}/{born_date[2:4]}/{born_date[4:8]}"
        else:

            return self.label.configure(text="\n\n    Entre com uma data no formato certo! 13122001! \n\n")
        # -----------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------

        if cpf.isdigit() and len(cpf) == 11:
            if any(cpf == interando["CPF"] for interando in usuarios):
                return self.label.configure(text="\n\n    CPF já cadastrado! \n\n")

        else:

            return self.label.configure(text="\n\n    Entre com um cpf no formato certo! xxxXXXxxxXX \n\n")
        # -----------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------------
        address = f"{address[:2]}"
        # -----------------------------------------------------------------------------------

        usuarios.append(
            {"nome": nome, "born_date": born_date, "CPF": cpf,
             "address": address, "senha": password, "saldo": 0, "extrato": ""}
        )

        self.entry_born_date.delete(0, 'end')
        self.entry_nome.delete(0, 'end')
        self.entry_cpf.delete(0, 'end')
        self.entry_address.delete(0, 'end')
        self.entry_password.delete(0, 'end')

        # deletar os dados dos entrys e apagar as mensagem de erro
        self.label.configure(text="")
        self.controller.show_frame(WalletLogin)

        # -----------------------------------------------------------------------------------

        print(usuarios)


class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Home Page")
        self.label.grid(row=1, column=1, pady=(0, 0))

        self.button = customtkinter.CTkButton(
            self,
            text="logout",
            command=lambda: controller.show_frame(WalletLogin)
        )
        self.button.grid(row=2, column=0, pady=(190, 5))


inicialização = WalletApp()
inicialização.mainloop()
