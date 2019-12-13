from message import Message
class Sms(Message):
    nl = '\n'
    def __init__(self):
        self.nr_od = 505050505
        self.nr_do = 707070707
        self.temat = 'temat'
    def send(self):
        print(f'Od: {self.nr_od}{Sms.nl}Do: {self.nr_do}{Sms.nl}Temat: {self.temat}{Sms.nl}Tresc: {self.message}')

x = Sms()
x.set_message('witam panstwa, witam')
x.send()
