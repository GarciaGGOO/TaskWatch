"""taskwatch_view"""
from datetime import date
from PySimpleGUI import PySimpleGUI as sg
from taskwatch_backgound import EmailBackgroundTask

# pegando data do dia
data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
                                  data_atual.year)

# Lógica e Classes


class Node:  # Nó das listas encadeadas, com uma propriedade a mais.
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.done = False

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class LinkedList:  # Criando a Lista encadeada em sí

    def __init__(self):
        self.root = None

    def __repr__(self):
        return '[' + str(self.root) + ']'

    # definindo metodos uteis da lista.

    def find_length(self):
        current = self.root
        count = 0
        while (current != None):
            count = count + 1
            current = current.next
        return count

    def search(self, data):
        current = self.root
        while current and current.data != data:
            current = current.next
        return current

    def converter_data(self):
        data_list = []
        current = self.root
        while (current != None):
            data_list.append(current.data)
            current = current.next
        return data_list

    def converter_done(self):
        done_list = []
        current = self.root
        while (current != None):
            if current.done == False:
                estado = "Incompleto"
            else:
                estado = "Completo"
            done_list.append(estado)
            current = current.next
        return done_list

    def to_array_tasks_done(self):
        done_list = []
        current = self.root
        while (current != None):
            if current.done == True:
                done_list.append(current.data)
            current = current.next
        return done_list
    
    def to_array_tasks_undone(self):
        done_list = []
        current = self.root
        while (current != None):
            if not current.done == True:
                done_list.append(current.data)
            current = current.next
        return done_list

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node

    def insert_after_node(self, find, new_data):
        # achando o anterior
        current = self.root
        while current and current.data != find:
            current = current.next
        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node

    def change_done(self, data):
        current = self.root
        while current and current.data != data:
            current = current.next
        if current.done == False:
            current.done = True
        else:
            current.done = False

    def remove(self, data):
        if self.root.data == data:
            self.root = self.root.next
        else:
            previous_node = None
            current_node = self.root
            while current_node and current_node.data != data:
                previous_node = current_node
                current_node = current_node.next
            if current_node:
                previous_node.next = current_node.next
            else:
                previous_node.next = None
    
    def isEmpyt(self):
        return self.root == None


# CRIAR LISTA ENCADEADA AQUI.
lista = LinkedList()
task = EmailBackgroundTask()
# telas
sg.theme('DarkGrey2')


def janela_incial():
    layout = [
        [sg.Text('          TaskWatch', font="unispace,26")],
        [sg.Button('Acessar Lista', size=(20, 1))],
        [sg.Button('Configurações', size=(20, 1))]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


def janela_config():
    layout = [
        [sg.Text(
            "Insira o e-mail e o horário em que deseja receber \n um relatório sobre as suas tarefas do dia.")],
        [sg.Text('E-mail:'), sg.Input(key='email', size=(30, 1))],
        [sg.Text('Insira o horário em formato "hh:mm"'), sg.Input(
            key='hora', size=(6, 1))],
        [sg.Text("             "), sg.Button('Voltar', size=(10, 1)),
         sg.Button('Salvar Configurações', disabled=False)]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


def janela_table():
    conteudo_data = LinkedList.converter_data(lista)
    conteudo_done = LinkedList.converter_done(lista)
    limite = LinkedList.find_length(lista)
    show_list = []
    headings = ['  Tarefa  ', '  Estado  ']

    for i in range(limite):
        show_list.append([conteudo_data.pop(0), conteudo_done.pop(0)])

    layout = [
        [sg.Text("Lista de hoje: " + data_em_texto)],
        [sg.Table(values=(show_list), headings=headings,
                  auto_size_columns=True, display_row_numbers=True,
                  justification='center', key='tabela', size=(50, 20), 	enable_click_events=True)],
        [sg.Button("Estado"), sg.Button("Excluir"),
         sg.Text("               "), sg.Button("Voltar"), sg.Button("Adicionar"), ]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


def janela_inserir():
    layout = [
        [sg.Text("Tarefa:"), sg.Input(key='tarefa', size=(30, 1)),
         sg.Button("Adicionar no Começo")],
        [sg.Text("Adicione no começo para colocar a tarefa em primeiro da lista, \n ou adicione-a logo após a tarefa selecionada.")],
        [sg.Button("Adicionar após..."), sg.Combo((conteudo), key='combo',
         default_value=None, size=30), sg.Text("ou"), sg.Button("Voltar")]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


def janela_estado():
    layout = [
        [sg.Combo((conteudo), key='select', default_value=None, size=40)],
        [sg.Button("Alterar estado"), sg.Button("Voltar")]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


def janela_excluir():
    layout = [
        [sg.Combo((conteudo), key='selected', default_value=None, size=40)],
        [sg.Button('Excluir'), sg.Button("Voltar")]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)


janela1, janela2, janela3, janela4, janela5, janela6 = janela_incial(
), None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()
    conteudo = LinkedList.converter_data(lista)

    
    # fechar janelas
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        janela4.hide()
    if window == janela5 and event == sg.WIN_CLOSED:
        janela5.hide()
    if window == janela6 and event == sg.WIN_CLOSED:
        janela6.hide()

    # alternar telas
    if window == janela1 and event == 'Configurações':
        janela1.hide()
        janela2 = janela_config()

    if window == janela1 and event == 'Acessar Lista':
        janela3 = janela_table()
        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()

    if window == janela3 and event == "Adicionar":
        janela4 = janela_inserir()

    if window == janela4 and event == 'Voltar':
        janela4.hide()

    if window == janela3 and event == "Estado":
        janela5 = janela_estado()

    if window == janela5 and event == 'Voltar':
        janela5.hide()

    if window == janela3 and event == 'Excluir':
        janela6 = janela_excluir()

    if window == janela6 and event == "Voltar":
        janela6.hide()

    # funcionais
    # configurações

    if window == janela2 and event == "Salvar Configurações":
        if values['email'] == "" or values['hora'] == "":
            print('Preencha ambos os campos antes de Salvar suas configurações')
        else:
            destinatario_email = values['email']
            hora_email = values['hora']
            print(destinatario_email)
            print(hora_email)
            EmailBackgroundTask.configura(task, destinatario_email, hora_email)
            task.start()
# pegar email e horário aqui.
    
    # inserir
    if window == janela4 and event == "Adicionar no Começo":
        LinkedList.insert_at_beginning(lista, values['tarefa'])
        print(lista)  # teste pra ver se inseriu
        janela4.hide()
        janela3.hide()
        janela3 = janela_table()
        if LinkedList.isEmpyt(lista):
            print('[Interface][InsertBegin]: Lista vazia')
        else:
            tasks_done = LinkedList.to_array_tasks_done(lista)
            tasks_undone = LinkedList.to_array_tasks_undone(lista)
            task.atualizar_lista(tasks_done, tasks_undone)

    elif window == janela4 and event == "Adicionar após...":
        if values['combo'] == "":
            print('Escolha uma opção válida na Combo Box.')
        else:
            LinkedList.insert_after_node(
                lista, values['combo'], values['tarefa'])  # previous_node, new_data
            print(lista)  # teste pra ver se inseriu 2
            janela4.hide()
            janela3.hide()
            janela3 = janela_table()
            if LinkedList.isEmpyt(lista):
                print('[Interface][InsertAfterNode]: lista vazia')
            else:
                tasks_done = LinkedList.to_array_tasks_done(lista)
                tasks_undone = LinkedList.to_array_tasks_undone(lista)
                task.atualizar_lista(tasks_done, tasks_undone)

    # alterar estado
    if window == janela5 and event == "Alterar estado":
        if values['select'] == "":
            print("Escolha uma opção válida na Combo Box.")
        else:
            LinkedList.change_done(lista, values['select'])
            janela5.hide()
            janela3.hide()
            janela3 = janela_table()
            tasks_done = LinkedList.to_array_tasks_done(lista)
            tasks_undone = LinkedList.to_array_tasks_undone(lista)
            task.atualizar_lista(tasks_done, tasks_undone)
    # excluir
    if window == janela6 and event == "Excluir":
        if values['selected'] == "":
            print("Escolha uma opção váliad na Combo Box.")
        else:
            LinkedList.remove(lista, values['selected'])
            print(lista)  # teste pra ver se excluiu
            janela6.hide()
            janela3.hide()
            janela3 = janela_table()
            tasks_done = LinkedList.to_array_tasks_done(lista)
            tasks_undone = LinkedList.to_array_tasks_undone(lista)
            task.atualizar_lista(tasks_done, tasks_undone)