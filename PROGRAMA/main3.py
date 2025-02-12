from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##Container para os Widgets
from kivy.core.window import Window

Window.size = (600,600)

class Programa(App):
    def build(self):
        container = BoxLayout(orientation ='vertical')
        header = BoxLayout(orientation ='horizontal')

        self.texto = Label(text='One')
        self.botao = Button(text='Two')
        
        self.botao.bind(on_press = self.hello)#função clicar no botão

        header.add_widget(self.texto)
        header.add_widget(self.botao)

        

        container.add_widget(header)
        

        return container
    def hello(self,event):
        print("Hello")
        self.texto.text = self.botao.text
    
if __name__=="__main__":
    Programa().run()