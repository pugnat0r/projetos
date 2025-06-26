from tkinter import font
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Pugnator(App):
    def build(self):

        box = BoxLayout(orientation='vertical')

        # on_release é o evento que queremos realizar! No caso é ao soltar. Toda vez que acontecer esse evento vai chamar o método incrementar que criamos.
        button = Button(text='Botão 1', font_size=30, on_release=self.incrementar) 

        # font_size é o tamanho da fonte
        # Usando self. para criar a variável Label dentro da instância self. Self é a instância da class sefl = Pugnator ()
        self.label = Label(text='1', font_size=30) 

        box.add_widget(button)
        box.add_widget(self.label)

        return box

    # nosso método que criamos, ele tem o acesso ao button
    def incrementar(self, button):

        # mudando o argumento de texto do botão
        button.text = 'soltei'

        # Pegamos o valor de texto alteramos para inteiro, somamos mais 1, voltamos para string. A cada click
        self.label.text = str(int(self.label.text)+1)


Pugnator().run()
