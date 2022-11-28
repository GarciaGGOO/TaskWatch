import smtplib
import email.message


def enviar_email(email_destinatario, tasks_done, tasks_undone): 
    print('começo enviar email')
    tasks_done = str(tasks_done).strip('[]')
    tasks_undone = str(tasks_undone).strip('[]')
    print(tasks_done + '-' + tasks_undone)

	email_envio = """
    <h1><b>Relatório diário de tarefas</b></h1>
	<p>Prezado(a),</p>
    <p>Segue seu relatório diário do TaskWatch.</p>
    <p>Suas tarefas <b>completas:</b></p>
	{0}
	<p></p>
	<p>--------------------------</p>
	<p></p>
	<p>Suas tarefas <b>incompletas:</b></p>
	{1}
	<p></p>
	<p>--------------------------</p>
    <p>Ótimo dia</p>
    <p>Task Watch</p>
    """

    envio_email = corpo_email.format(tasks_done, tasks_undone)
    print('enviando email')
    msg = email.message.Message()
    msg['Subject'] = 'primeiro email'#'Assunto'
    msg['From'] = 'taskwatch2022@gmail.com'#'remetente' 
    msg['To'] = email_destinatario #'destinatario'
    password = 'jogqnmgmavnhyrbk'#'senha do email from'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
