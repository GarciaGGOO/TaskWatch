"""taskwatch_email"""
from datetime import datetime

hora_email = '17:49' ##definir hora do email

while True: #gatilho pro email?
    hora_atual = datetime.now()
    hora_atual_text = hora_atual.strftime('%H:%M')
    print(hora_atual_text)
    if hora_atual_text == hora_email:
        print('Enviando relatório diário.')
        break
    else:
        continue
