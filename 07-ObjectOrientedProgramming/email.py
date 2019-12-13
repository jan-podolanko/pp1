from message import Message
class Email(Message):
    nl = '\n'
    def __init__(self):
        self.od = 'email@email.com'
        self.do = 'email2@email.com'
        self.temat = 'temat'
    def send(self):
        print(f'Od: {self.od}{Email.nl}Do: {self.do}{Email.nl}Temat: {self.temat}{Email.nl}Tresc: {self.message}')

x = Email()
x.set_message('witam panstwa, witam')
x.send()
