"""taskwatch_email"""
from datetime import datetime
from taskwatch_supreme import *

print('Iniciando TaskWatch_Test')

while True: 
    hora_atual = datetime.now()
    hora_atual_text = hora_atual.strftime('%H:%M')
    print(hora_atual_text)
    if hora_atual_text == "19:45":
        print('[Background]: Enviando relatório diário para: alguem')
        break
    else:
        continue
