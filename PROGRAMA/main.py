from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Programa(App):
    def build(self):
        return Button(text = 'Clique', font_size='50px')
    
if __name__=="__main__":
    Programa().run() ## instancia a classe e chama o run