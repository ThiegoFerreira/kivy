from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout ##Container para os Widgets
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (600,600)

class Programa(App):
    def build(self):
        body = BoxLayout(orientation = "vertical")
        teclas = GridLayout(cols=4)

        display = Label(text = "0") 
        botao1 = Button(text = "7")
        botao2 = Button(text='8') 
        botao3 = Button(text='9') 
        botao4 = Button(text='-') 
        botao5 = Button(text='4') 
        botao6 = Button(text='5') 
        botao7 = Button(text='6') 
        botao8 = Button(text=':') 
        botao9 = Button(text='1') 
        botao10 = Button(text='2') 
        botao11= Button(text='3') 
        botao12 = Button(text='/') 
        botao13 = Button(text='0') 
        botao14 = Button(text='C') 
        botao15 = Button(text='AC') 
        botao16 = Button(text='+') 

        teclas.add_widget(botao1)
        teclas.add_widget(botao2)
        teclas.add_widget(botao3)
        teclas.add_widget(botao4)
        teclas.add_widget(botao5)
        teclas.add_widget(botao6)
        teclas.add_widget(botao7)
        teclas.add_widget(botao8)
        teclas.add_widget(botao9)
        teclas.add_widget(botao10)
        teclas.add_widget(botao11)
        teclas.add_widget(botao12)
        teclas.add_widget(botao13)
        teclas.add_widget(botao14)
        teclas.add_widget(botao15)
        teclas.add_widget(botao16)

        body.add_widget(display)
        body.add_widget(teclas)



        return body
    
if __name__=="__main__":
    Programa().run()