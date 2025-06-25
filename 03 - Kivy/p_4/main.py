from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class incrementador(BoxLayout):
    pass


class Pugnator(App):
    def build(self):
        return incrementador()


Pugnator().run()
