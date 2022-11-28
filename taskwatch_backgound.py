"""taskwatch_email"""
from datetime import datetime
import threading 
import time
from taskwatch_envio_email import enviar_email

class EmailBackgroundTask(threading.Thread):

    def run(self, *args, **kwargs):
        if self.email != '' and self.horario != '':
            while True: 
                hora_atual = datetime.now()
                hora_atual_text = hora_atual.strftime('%H:%M')
                print(hora_atual_text)
                time.sleep(5)
                if hora_atual_text == self.horario:
                    print('[Background]: Enviando relatório diário para: ' + self.email)
                    if len(self.tasks_done) > 0 or len(self.tasks_undone) > 0:
                        print('[Background]: Lista tem tarefas registradas.. enviando email')
                        print('[Background]: Detalhes da lista ->' + str(self.tasks_undone).strip('[]'))
                        enviar_email(self.email, self.tasks_done, self.tasks_undone)
                        break
                else:
                    continue

    def configura(self, email, horario):
        self.email = email
        self.horario = horario
        
    def atualizar_lista(self, tasks_done, tasks_undone):
        if len(tasks_done) > 0 or len(tasks_undone) > 0:
            print('[Background][AtualizarLista]: Atualizando lista do brackgound')
            self.tasks_done = tasks_done 
            self.tasks_undone = tasks_undone
        else:
            print('[Background][AtualizarLista]: Lista Está Vazia, não atualizar')

    email = ''
    horario = ''
    tasks_done = []
    tasks_undone = []



