from turtle import color
import customtkinter


class WarpApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.title("shadown")
        self.geometry("1200x200")
        customtkinter.set_appearance_mode("dark")

        self.button = customtkinter.CTkButton(
            self, text="Warp", fg_color="grey", hover_color="dark grey")
        self.button.grid(row=1, column=1, padx=20, pady=20)

        self.button = customtkinter.CTkButton(
            self, text="VS CODE", fg_color="grey", hover_color="dark grey")
        self.button.grid(row=2, column=1, padx=20, pady=20)


inicialização = WarpApp()
inicialização.iconbitmap("00_python/01_Projetos/Warp/estenografo.ico")
inicialização.mainloop()
