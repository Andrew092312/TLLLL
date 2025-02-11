import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import string

senders = {
    'your@mail.ru': 'o-auth password',
    'your1@mail.ru': 'o-auth password',
    'your2@mail.ru': 'o-auth password',
    'your3@mail.ru': 'o-auth password',
    'your4@mail.ru': 'o-auth password',
    'your5@mail.ru': 'o-auth password',
    'your6@mail.ru': 'o-auth password',
    'your7@mail.ru': 'o-auth password',
    'your8@mail.ru': 'o-auth password',
    'your9@mail.ru': 'o-auth password',
    'your10@mail.ru': 'o-auth password',
    'your11@mail.ru': 'o-auth password',
    'your12@mail.ru': 'o-auth password',
    'your13@mail.ru': 'o-auth password',
    'your14@mail.ru': 'o-auth password',
    'your15@mail.ru': 'o-auth password',
    'your16@mail.ru': 'o-auth password',
    'your17@mail.ru': 'o-auth password',
    'your18@mail.ru': 'o-auth password',
    'your19@mail.ru': 'o-auth password',
    'your20@mail.com': 'o-auth password',
    'your21@mail.com': 'o-auth password',
    'your22@mail.ru': 'o-auth password',
    'your23@mail.ru': 'o-auth password',
    'your24@mail.ru': 'o-auth password',
    'your25@mail.ru': 'o-auth password',
    'your26@mail.ru': 'o-auth password'
}

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    print("  _______  _        _       _       _ ")
    print(" |__   __|| |      | |     | |     | |")
    print("    | |   | |      | |     | |     | |")
    print("    | |   | |      | |     | |     | |")
    print("    | |   | |____  | |____ | |____ | |____ ")
    print("    |_|   |______| |______||______||______|")
    print("      by @andrey200923   ")

def menu():
    print("\033[92mМеню:\033[0m")
    print("1. Аккаунт")
    print("2. Канал")
    print("3. Боты.")
    choice = input("Выбирай:  ")
    return choice

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()

    if choice == '1':
        print("1.Spam")
        print("2.Личная информация.")
        print("3.Буллинг")
        print("4.Сессия")
        print("5.Премиум аккаунт")
        print("6.Аккаунт зарегистрированный через виртуальный номер")
        comp_choice = input("Выбирай: ")

        if comp_choice in ["1", "2", "3"]:
            print("Следуй тому что тут написано и вставляй.")
            username = input("юзер: ")
            id = input("айди: ")
            chat_link = input("ссылку на чат/канал: ")
            violation_link = input("ссылку на нарушение: ")
            print("Погоди чу-чуть. by @andrey200923")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    else:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}!")
                    time.sleep(5)

        elif comp_choice == "4":
            print("Укажи всё что нужно ниже.")
            username = input("юзернейм: ")
            id = input("айди: ")
            print("Погоди чу-чуть. by @andrey200923")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    if send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    else:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}!")
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуй указаниям и вводи что просят.")
            username = input("юзернейм: ")
            id = input("айди: ")
            print("Погоди чу-чуть. by @andrey200923")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    else:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}!")
                    time.sleep(5)

    elif choice == "2":
        print("1.Личные данные")
        print("2.Жив0деры")
        print("3. каналы")
        print("4.Прайс каналы.")
        ch_choice = input("выбор: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("Погоди чу-чуть. by @andrey200923")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip())
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    else:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}!")
                    time.sleep(5)

    elif choice == "3":
        print("1.Порно боты")
        print("2.Посхалко.")
        bot_ch = input("Выбирай что то из этого: ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("Погоди чу-чуть by @andrey200923")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который выдает /дп/18+. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    if send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body):
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    else:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}!")
                    time.sleep(5)
        elif bot_ch == "2":
            print("1488")

if __name__ == "__main__":
    main()
