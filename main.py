# Configuracoes gerais do app
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
Config.set('graphics','resizable','0') # Tamanho fixo

from kivy.app import App
from kivy.lang import Builder

# Iremos usar para a avaliacao das expressoes numericas 
import math

# Widgets
interface = Builder.load_file("tela.kv")

# Definicao da janela do app
class Calculadora(App):
    
    def build(self):
        self.title = "Calculadora"
        return interface
    
    # Adiciona o texto do botão pressionado no TextInput
    def add_input(self, text):
        expression = interface.ids.text_input.text
        expression += text
        interface.ids.text_input.text = expression
    
    # Avaliacao da expressao numerica
    def eval_expression(self):
        try:
            expression = interface.ids.text_input.text
            result = eval(expression) # a funcao eval avalia espressao
            print(f"{expression}={result}")
            interface.ids.text_input.text = str(result)
        except Exception as e:
            print(e)
            interface.ids.text_input.text = "ERRO!!!"


# Instancia e inicia a aplicação
if __name__ == '__main__':
    Calculadora().run()
