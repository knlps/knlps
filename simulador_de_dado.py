#Simulador de Dado
#Objetivo: Simular um dado gerando um valor de 1 a 6
import random

class SimuladordeDado:
    def __init__(self): #Comportamento inicial da classe
        self.valor_minimo = 1 #O dado tem 6 lados, o menor é o 1
        self.valor_maximo = 6 #O maior valor do dado tem que ser 6
        self.mensagem = 'Você gostaria de gerar um novo valor com o dado?' #Mensagem para o usuário quando rodar o dado
            

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == "Sim" or resposta == 'sim':
            self.ValordoDado()
        elif resposta == 'Não' or resposta == 'não' or resposta == 'nao':
            print('Agradecemos sua participação!')
        else:
            print('Favor digitar Sim ou Não')

    def ValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
simulador = SimuladordeDado()
simulador.Iniciar()