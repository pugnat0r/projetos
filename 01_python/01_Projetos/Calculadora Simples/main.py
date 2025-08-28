from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class calculadora(BoxLayout):
    pass


class Pugnator(App):
    def build(self):

        return calculadora()


Pugnator().run()
