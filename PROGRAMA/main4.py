from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##Container para os Widgets
from kivy.core.window import Window

Window.size = (600,600)

class Programa(App):
    def build(self):
        layout = BoxLayout(orientation ='horizontal')

        self.botao = Button(text='-', font_size= "50px")
        self.texto = Label(text='0', font_size = "50px")
        self.botao2 = Button(text='+', font_size= "50px")
        
        self.botao.bind(on_press = self.menos)
        self.botao2.bind(on_press = self.mais)

        layout.add_widget(self.botao)
        layout.add_widget(self.texto)
        layout.add_widget(self.botao2)

        return layout
    
    def mais(self,event):
        self.texto.text = str(int(self.texto.text)+1)
    def menos(self,event):
        self.texto.text = str(int(self.texto.text)-1)
    
if __name__=="__main__":
    Programa().run()