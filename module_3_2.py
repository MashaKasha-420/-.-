def send_email (message, recipient, sender = university.help@gmail.com ):
    if recipient in "@" or ".com" or ".ru" or ".net":
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif:
        recipient == sender
        print("Нельзя отправить письмо самому себе!")
    elif:
        sender ==  university.help@gmail.com
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email("Домашнее задание проверено" , "sobolev_sp@.mail.ru")


send_email("Это сообщение для проверки связи", recipient = university.help@gmail.com)


send_email("Добрый день! Мы давно не получали от вас домашних  заданий", "mashakasha.0999@gmail.com",  sender = urban.teacher@mail.ru)