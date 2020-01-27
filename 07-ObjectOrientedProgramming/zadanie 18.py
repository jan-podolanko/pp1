class Car():
    def __init__(self,brand,model,license_plate):
        self.brand=brand
        self.model=model
        self.license_plate=license_plate
        self.mileage=0
        self.rent_status=False
    def __str__(self):
        return 'Brand: '+self.brand+'\n'+'Model: '+self.model+'\n'+'License plate: '+self.license_plate+'\n'+'Mileage: '+str(self.mileage)+'\n'+'Rented:'+str(self.rent_status)
    def change_mileage(self,mileage):
        self.mileage=mileage
    def change_rent_status(self):
        if self.rent_status:
            self.rent_status=False
        else:
            self.rent_status=True

class Rental():
    def __init__(self,name):
        


x=Car('Ford','Focus','123dfff')
print(x)
