from tkinter import HORIZONTAL, VERTICAL
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Pugnator(App):
    def build(self):
        # Invocando método de Layouat na var box
        box = BoxLayout(orientation='vertical')

        # Ivocando método da class App na Var button
        button = Button(text='Botão 1')
        # Ivocando método da class App na Var Label
        label = Label(text='Label 1')

        # Adicionando a VAR button no layout de nome box, com o widget
        box.add_widget(button)
        # Adicionando a VAR Label no layout de nome box, com o widget
        box.add_widget(label)



        box2 = BoxLayout()  # Criando outro layout com o nome box2

        button2 = Button(text='Botão 2')
        label2 = Label(text='Label 2')

        box2.add_widget(button2)
        box2.add_widget(label2)

        # Adicionando o segundo layout dentro do primeiro Layout
        box.add_widget(box2)

        return box


Pugnator().run()
