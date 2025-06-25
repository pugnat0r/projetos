from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class tarefas(BoxLayout):
    pass


class Pugnator(App):
    def build(self):
        return tarefas()


Pugnator().run()
