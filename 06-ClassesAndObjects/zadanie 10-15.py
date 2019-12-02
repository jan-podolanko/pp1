class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        self.channels = channels_list
    def volume_up(self):
        if self.volume == 10:
            self.volume = 10
        else:
            self.volume += 1
    def volume_down(self):
        if self.volume == 0:
            self.volume = 0
        else:
            self.volume -= 1
    def show_status(self):
        if self.is_on and self.channel_no <= len(self.channels):
            print(f'TV is on and is on channel {self.channel_no} ({self.channels[self.channel_no-1]}). Głośność jest na poziomie {self.volume}')
        elif self.is_on and self.channel_no > len(self.channels):
            print(f'TV is on and is on channel {self.channel_no}. Głośność jest na poziomie {self.volume}')   
        else:
            print('TV is off')
        """
        if self.is_on == True:
            print('TV is on')
        elif self.is_on == False:
            print('TV is off')
        """  
    def show_channels(self):
        if len(self.channels) >= 1:
            print('Lista kanałów:')
            j = 1
            for i in self.channels:
                print(f'{j}. {i}')
                j += 1
        else:
            print('Brak zainstalowanych kanałów')
zmienna = TV()
zmienna.show_status()
zmienna.on()
zmienna.show_status()
zmienna.off()
zmienna.show_status()
zmienna.set_channel(5)
zmienna.on()
zmienna.show_status()
zmienna.off()
zmienna.show_status()
zmienna.show_channels()
zmienna.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
zmienna.show_channels()
zmienna.on()
zmienna.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'TVN24', 'TVP Info', 'HBO'])
zmienna.set_channel(3)
zmienna.show_status()
zmienna.set_channel(1)
zmienna.show_status()
zmienna.set_channel(6)
zmienna.show_status()
zmienna.volume_up()
zmienna.show_status()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.volume_up()
zmienna.show_status()
zmienna.volume_down()
zmienna.show_status()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.show_status()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.volume_down()
zmienna.show_status()