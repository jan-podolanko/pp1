class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        message.capitalize()
        message + 'BYE'
        self.message = message