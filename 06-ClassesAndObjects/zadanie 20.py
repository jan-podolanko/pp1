class flight():
    def __init__(self):
        self.airline = 'Ryanair'
        self.flight_no = 'FR6876/RYR48UM'
        self.aircraft_type = 'Boeing 737-8AS'
        self.ffrom = 'BGY'
        self.fto = 'KRK'
        self.altitude_m = 0
    def start(self, s_altitude):
        if s_altitude >= 1000 and s_altitude <= 2000:
            self.altitude_m = s_altitude
        elif s_altitude > 2000:
            print('Altitude input too high for a takeoff')
        else:
            print('Altitude input too low for a takeoff')
    def change_altitude(self, alt):
        if alt >= 300 and alt <= 11000:
            self.altitude_m = alt
        elif alt < 300:
            print('Altitude too low')
        elif alt > 11000:
            print('Altitude too high')
    def land(self):
        if self.altitude_m < 500:
            self.altitude_m = 0
            print('Plane succesfully landed')
        else:
            print('Altitude too high to execute a landing')
    def show_status(self):
        print(f"Our flight number is {self.flight_no}, we're flying from {self.ffrom} to {self.fto}. Our current altitude is {self.altitude_m} meters")

x = flight()
x.start(500)
x.show_status()
x.change_altitude(8900)
x.show_status()
x.change_altitude(200)
x.show_status()
x.change_altitude(350)
x.show_status()
x.land()
x.show_status