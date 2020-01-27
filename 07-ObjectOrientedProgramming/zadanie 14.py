class Phone():
    n = '\n'
    def __init__(self,brand,model,color,dim1,dim2,dim3):
        self.brand = brand
        self.model = model
        self.color = color
        self.dimension1 = dim1
        self.dimension2 = dim2
        self.dimension3 = dim3
        self.on = False
    def display_specification(self):
        print(f'Phone model: {self.brand} {self.model}{Phone.n}Color: {self.color}{Phone.n}Dimensions(mm): {self.dimension1}x{self.dimension2}x{self.dimension3}')
    def call(self,p_number):
        if self.on:
            print(f'Calling {p_number}...')
        else:
            print(f'Unable to call {p_number}. Please turn the phone on.')
    def turn_on(self):
        if self.on:
            print('Phone already on!')
        else:    
            self.on = True
            print('Phone succesfully turned on')
    def turn_off(self):
        if self.on:
            self.on = False
            print('Phone succesfully turned off')
        else:    
            print('Phone already off!')


x = Phone('Huawei','Mate30 Pro','pink',158.1,73.1,8.8)
y = Phone('Ford','Model T','Turqoise',5000,2000,3000)

x.display_specification()
y.display_specification()
x.call(123456789)
x.turn_on()
x.turn_on()
x.call(123456789)
x.turn_off()
x.turn_off()
