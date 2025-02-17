#Configurações iniciais. Iport das Classes
import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.core.window import Window
Window.size = (300,700)

class MyCalc(App):
    def build(self):

        layout = BoxLayout (orientation = 'vertical')
        box_botoes = GridLayout(cols=4)

        self.display = Label(font_size='50px')

        self.button0 = Button(text = 'Zerar', size_hint=(1, .5))
        self.button0.bind(on_press = self.zerar) #Evento ao botão 0 chamando o método hello
        

        self.button1 = Button(text = '1')
        self.button2 = Button(text = '2')
        self.button3 = Button(text = '3')
        self.button4 = Button(text = '4')
        self.button5 = Button(text = '5')
        self.button6 = Button(text = '6')
        self.button7 = Button(text = '7')
        self.button8 = Button(text = '8')
        self.button9 = Button(text = '9')

        self.button_soma = Button(text = '+')
        self.button_sub = Button(text = '-')
        self.button_mult = Button(text = '*')
        self.button_div = Button(text = ':')
        self.button_pot = Button(text = 'Pot')
        self.button_raiz = Button(text = 'Raiz')
        self.button_back = Button(text = '<-')
        self.button_igual = Button(text = '=')

        self.button1.bind(on_press = self.armazenar)
        self.button2.bind(on_press = self.armazenar)
        self.button3.bind(on_press = self.armazenar)
        self.button4.bind(on_press = self.armazenar)
        self.button5.bind(on_press = self.armazenar)
        self.button6.bind(on_press = self.armazenar)
        self.button7.bind(on_press = self.armazenar)
        self.button8.bind(on_press = self.armazenar)
        self.button9.bind(on_press = self.armazenar)
    
        self.button_soma.bind(on_press = self.armazenar)
        self.button_sub.bind(on_press = self.armazenar)
        self.button_mult.bind(on_press = self.armazenar)
        self.button_div.bind(on_press = self.armazenar)
        self.button_pot.bind(on_press = self.armazenar)
        self.button_raiz.bind(on_press = self.armazenar)
        self.button_back.bind(on_press = self.apagar)

        self.button_igual.bind(on_press = self.calcular)

        

        box_botoes.add_widget  (self.button1)
        box_botoes.add_widget  (self.button2)
        box_botoes.add_widget  (self.button3)
        box_botoes.add_widget  (self.button4)
        box_botoes.add_widget  (self.button5)
        box_botoes.add_widget  (self.button6)
        box_botoes.add_widget  (self.button7)
        box_botoes.add_widget  (self.button8)
        box_botoes.add_widget  (self.button9)
        box_botoes.add_widget  (self.button_soma)
        box_botoes.add_widget  (self.button_sub)
        box_botoes.add_widget  (self.button_mult)
        box_botoes.add_widget  (self.button_div)
        box_botoes.add_widget  (self.button_pot)
        box_botoes.add_widget  (self.button_raiz)
        box_botoes.add_widget  (self.button_back)

        box_botoes.add_widget  (self.button_igual)
        

        layout.add_widget (self.button0)
        layout.add_widget (self.display) 
        layout.add_widget (box_botoes)
        


        return layout
    
    # def hello(self,event):#event é o evento de clicar
    #     print("Hello")
    #     print(event.text)
    
    def zerar(self,event):
        # print(self.display.text)
        self.display.text = ''
    
    def apagar(self,event):
        self.display.text = self.display.text[:-1]
        



        # print(type(self.display.text))
        # print(self.display.text[2])
        # print(self.display.text[-1])
        # back = list(self.display.text)
        # back.pop()
        # valor = "".join(str(n) for n in back)
        # self.display.text = valor

    def armazenar(self,event):
        # print(event.text)
        self.display.text += event.text

    def calcular(self,event):
        if '+' in self.display.text:
            numbers = self.display.text.split('+')
            soma = int(numbers[0]) + int(numbers[1])
            self.display.text = str(soma)
        elif '-' in self.display.text:
            numbers = self.display.text.split('-')
            subtracao = int(numbers[0]) - int(numbers[1])
            self.display.text = str(subtracao)
        elif '*' in self.display.text:
            numbers = self.display.text.split('*')
            multiplicacao = float(numbers[0]) * float(numbers[1])
            self.display.text = str(multiplicacao)
        elif ':' in self.display.text:
            numbers = self.display.text.split(':')
            divisao = float(numbers[0]) / float(numbers[1])
            self.display.text = str(divisao)
        elif 'Pot' in self.display.text:
            numbers = self.display.text.split('Pot')
            pot = float(numbers[0]) ** float(numbers[1])
            self.display.text = str(pot)
        elif 'Raiz' in self.display.text:
            numbers = self.display.text.split('Raiz')
            raiz = float(numbers[0])**(1/ float(numbers[1]))
            self.display.text = str(raiz)
        
        
        
        





if __name__ == "__main__":
    MyCalc().run()

