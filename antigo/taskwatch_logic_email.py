from datetime import datetime
import time
from taskwatch_envio_email import enviar_email

lista = []
class DisparoEmail():
    horario = ''
    email = ''

    def __init__(self, horario, email):
        self.horario = horario
        self.email = email 

    def atualizar_lista(self, lista):
        self.lista = lista 

    def ciclo(self):   
         while True: #gatilho pro email?
            hora_atual = datetime.now()
            hora_atual_text = hora_atual.strftime('%H:%M')
            print(hora_atual_text)
            time.sleep(5)
            if hora_atual_text == self.horario:
                print('Enviando relatório diário para: ' + self.email)
                if self.lista != '':
                    enviar_email(self.email, self.lista)
                    break
            else:
                continue


