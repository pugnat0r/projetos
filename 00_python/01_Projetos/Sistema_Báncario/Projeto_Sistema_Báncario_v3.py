import customtkinter

# watchmedo auto-restart -d . -p "*.py" -- python Projeto_Sistema_Báncario_v3.py


class WalletApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Sistema Bancário v3.0")

        # add widgets to app
        self.label = customtkinter.CTkLabel(
            self,
            text="Bem-vindo ao Sistema Bancário v3.0",
            font=("Arial", 19),
            text_color="black"
        )
        self.label.place(x=150, y=0)




        self.label = customtkinter.CTkLabel(
            self, text="Entrar", font=("Arial", 19), text_color="green")
        self.label.place(x=150, y=35)

        # Campo de entrada para o nome de usuário
        self.entry_username = customtkinter.CTkEntry(
            self, placeholder_text="     nome de usuário")
        self.entry_username.place(x=150, y=65)

        # self.label = customtkinter.CTkLabel(
        #     self, text="Senha", font=("Arial", 19), text_color="grey")
        # self.label.place(x=150, y=0)

    def on_button_click(self):
        self.label.configure(text="Você clicou no botão!")

    def main(self):
        self.mainloop()


inicialização = WalletApp()
inicialização.main()
