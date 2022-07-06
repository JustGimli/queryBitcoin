import smtplib
from datetime import date
import configparser


def send_email(exc,FROM):

    try:

        conf = configparser.ConfigParser()
        conf.read('config.ini')
        
        mes = f'''Ошибка {exc} от {FROM}
        Время ошибки: {date.today()}'''

        server = smtplib.SMTP_SSL('smtp.yandex.com')
        server.login('JustGimli23@yandex.com',conf['sendmail']['pass'])
        server.sendmail("JustGimli23@yandex.com","JustGimli23@yandex.com",mes.encode(encoding='utf-8'))
        server.quit()

        print('Сообщение с ошибкой отправлено на почту.')

    except Exception as e:

        print(f'Собщение с ошибкой не отправлено.Ошибка отправки {e}')
