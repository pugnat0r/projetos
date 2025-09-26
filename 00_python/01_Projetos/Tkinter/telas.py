import customtkinter


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
            # 👈 recebe parent e controller
            frame = tela_class(self.container, self)
            self.frames[tela_class] = frame

        frame = self.frames[tela_class]

        # Esconde todas as telas
        for f in self.frames.values():
            f.pack_forget()

        # Mostra a escolhida
        frame.pack(fill="both", expand=True)


class WalletLogin(customtkinter.CTkFrame):  # 👈 Agora é um frame
    def __init__(self, parent, controller):
        super().__init__(parent)

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
        self.label0.pack(pady=10)

        self.label1 = customtkinter.CTkLabel(
            self,
            text="Login",
            font=("Arial", 19),
            text_color="green"
        )
        self.label1.pack(pady=10)

        self.entry_username = customtkinter.CTkEntry(
            self,
            placeholder_text="CPF do usuário"
        )
        self.entry_username.pack(pady=10)

        self.entry_password = customtkinter.CTkEntry(
            self,
            placeholder_text="Senha do usuário",
            show="*"
        )
        self.entry_password.pack(pady=10)

        # Botão que troca de tela para HomePage
        self.button0 = customtkinter.CTkButton(
            self,
            text="Entrar",
            command=lambda: controller.show_frame(HomePage)
        )
        self.button0.pack(pady=10)

        self.button1 = customtkinter.CTkButton(
            self,
            text="Cadastrar-se",
            command=lambda: print("Cadastrar...")
        )
        self.button1.pack(pady=10)

        self.button2 = customtkinter.CTkButton(
            self,
            text="Sair",
            command=controller.destroy
        )
        self.button2.pack(pady=10)


class HomePage(customtkinter.CTkFrame):  # 👈 Outra tela
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = customtkinter.CTkLabel(self, text="Bem-vindo à HomePage!")
        label.pack(pady=20)

        voltar_btn = customtkinter.CTkButton(
            self,
            text="Voltar para Login",
            command=lambda: controller.show_frame(WalletLogin)
        )
        voltar_btn.pack(pady=10)


inicializacao = WalletApp()
inicializacao.mainloop()
