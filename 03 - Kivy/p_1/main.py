from kivy.app import App  # Criar janela
from kivy.uix.button import Button  # Importa botão


class Multtec(App):  # Classe com o nome do App, herdando características da Classe App
    def build(self):  # Método que vai inicializar e construir o Aplicativo
        # Tudo que retorna é mostrato no Aplicativo
        return Button(text='Olá mundo')


Multtec().run()  # Invocando instância e usando uma função herdada.
