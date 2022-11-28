"""taskwatch_view"""
from PySimpleGUI import PySimpleGUI as sg
from datetime import date
from taskwatch_backgound import EmailBackgroundTask

data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)

#CRIAR LISTA ENCADEADA AQUI.

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
        [sg.Text("Insira seu e-mail, para receber um \nrelatório de suas tarfas no fim do dia")],
        [sg.Text('e-mail:'), sg.Input(key='email', size=(26,1))],
        [sg.Text("             "), sg.Button('Salvar E-mail', size=(10,1)), sg.Button('Voltar', size=(10,1))]
    ]
    return sg.Window('TaskWatch', layout=layout,finalize=True)

def janela_table():
    headings = ['  Tarefa  ', '  Estado  ']
    input_info = [
    ['Escovar os dentes','Completo'] #PlaceHolder
    ]

    layout = [
        [sg.Text("Lista de hoje: " + data_em_texto ),sg.Text("                    ")],

        [sg.Table(values=input_info,headings=headings,
        auto_size_columns=True, display_row_numbers=True,
        justification='center',key='-TABLE-', size=(50,20))],

        [sg.Button("Excluir"),sg.Text("                 "),sg.Button("Voltar"),sg.Button("Completar"),sg.Button("Adicionar")]
    ]
    return sg.Window('TaskWatch', layout=layout,finalize=True)



janela1,janela2,janela3 = janela_incial(), None, None

t = EmailBackgroundTask()
t.start()

while True:
    window,event,values = sg.read_all_windows()
    
    #fechar janelas
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break

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

    
    #botoes funcionais
    if window == janela2 and event == "Salvar E-mail":
        print(values['email'])
        ##pegar email aqui.


