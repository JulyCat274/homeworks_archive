def send_email(message, recipient, *, sender='university.help@gmail.com'):
    i = {1:'@', 2:'.com', 3:'.ru', 4:'.net'}
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif not ((i[2] in recipient) or (i[3] in recipient) or (i[4] in recipient)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not ((i[2] in sender) or (i[3] in sender) or (i[4] in sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not (i[1] in recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not (i[1] in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif 'university.help@gmail.com' != sender:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')