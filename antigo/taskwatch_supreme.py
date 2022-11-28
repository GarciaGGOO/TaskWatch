"""taskwatch_view"""
from datetime import date
from PySimpleGUI import PySimpleGUI as sg


#pegando data do dia
data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

# Lógica e Classes

class Node: #Nó das listas encadeadas, com uma propriedade a mais.
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.done = False

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)

class LinkedList: #Criando a Lista encadeada em sí
  
    def __init__(self):
        self.root = None

    def __repr__(self):
        return '[' + str(self.root) + ']'

    #definindo metodos uteis da lista.

    def Insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node
    
    def insert_after_node(self, previous_node, new_data):
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def linked_show(self):
        current = self.root
        info_list = [
            [0,0] ###idk
        ]

        while current.next:#
            info_list.append([current.data,current.done],)
            current = current.next
        return info_list

    def change_done(self, data):
        current = self.root
        while current and current.data != data:
            current.next
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

#CRIAR LISTA ENCADEADA AQUI.
lista = LinkedList()
LinkedList.Insert_at_beginning(lista,"Lavar o Carro")

#telas
sg.theme('DarkGrey2')
def janela_incial():
    layout = [
        [sg.Text('TaskWatch')],
        [sg.Button('Acessar Lista', size=(20, 1))],
        [sg.Button('Configurações', size=(20,1))]           
    ]
    return sg.Window('TaskWatch', layout=layout,finalize=True)

def janela_config():
    layout = [
        [sg.Text("Insira seu e-mail, para receber um relatório de suas tarfas no fim do dia.")],
        [sg.Text('E-mail:'), sg.Input(key='email', size=(30,1)), sg.Button('Salvar E-mail', size=(10,1))],
        [sg.Text("Escolha a hora em que deseja receber o relatório em seu email.")],
        [sg.Text('Insira o horário em formato "hh:mm"'),sg.Input(key='hora',size=(5,1)), sg.Button("Salvar horário")],
        [sg.Text("             "),sg.Button('Voltar', size=(10,1))]
    ]
    return sg.Window('TaskWatch', layout=layout,finalize=True)

def janela_table():
    headings = ['  Tarefa  ', '  Estado  '] 
    input_info = [
    #['Escovar os dentes','Completo'], #PlaceHolder
    #['Lavar o Carro', 'Incompleto'] #PlaceHolder2
    ]

    layout = [
        [sg.Text("Lista de hoje: " + data_em_texto ),sg.Text("                    ")],

        [sg.Table(values=input_info,headings=headings,
        auto_size_columns=True, display_row_numbers=True,
        justification='center',key='-TABLE-', size=(50,20))],

        [sg.Button("Excluir"),sg.Text("                 "),
        sg.Button("Voltar"),sg.Button("Completar"),sg.Button("Adicionar")]
    ]
    return sg.Window('TaskWatch', layout=layout,finalize=True)

def janela_inserir():
    layout = [
        [sg.Text("Tarefa:"),sg.Input(key='tarefa', size=(30,1)),sg.Button("Adicionar no Começo")],
        [sg.Text("Adicione no começo para colocar a tarefa em primeiro da lista, \n ou adicione-a logo após a tarefa selecionada.")],
        [sg.Button("Adicionar após..."), sg.Combo(('meteoro','chuva'), default_value=None,size=30), sg.Text("ou"), sg.Button("Voltar")]
    ]
    return sg.Window('TaskWatch', layout=layout, finalize=True)
    



janela1,janela2,janela3,janela4 = janela_incial(), None, None,None
email = '' 
horario = ''

while True:
    window,event,values = sg.read_all_windows()   
    #fechar janelas
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        janela4.hide()

    #alternar telas
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


    #botoes funcionais
    if window == janela2 and event == "Salvar E-mail":
        email = values['email']
        ##pegar email aqui.
    if window == janela2 and event == "Salvar horário":
        horario = values['hora']
        ##pegar horário aqui.
