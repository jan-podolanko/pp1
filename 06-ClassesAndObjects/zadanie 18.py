import random
class dice():
    def throw_die(self, no):
        self.no_of_throws = no
        self.sum = 0
        for i in range(1,self.no_of_throws+1):
            self.throw = random.randrange(1,6)
            print(f'Throw #{i}: {self.throw}')
            self.sum += self.throw
        print(f'Sum of thrown die values: {self.sum}')

x = dice()
x.throw_die(5)
