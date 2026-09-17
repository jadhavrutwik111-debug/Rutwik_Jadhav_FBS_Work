from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def calToll(self):
        pass

class Two_wheeler(Vehicle):
    basic = 20
    def __init__(self,num_persons):
        super().__init__()
        self.num_persons = num_persons

    def calToll(self):
        if self.num_persons > 2:
            return self.basic + (self.num_persons - 2) * 10
        else:
            return self.basic

class Three_wheeler(Vehicle):
    basic = 30
    def __init__(self,num_persons):
        super().__init__()
        self.num_persons = num_persons

    def calToll(self):
        if self.num_persons > 3:
            return self.basic + (self.num_persons - 3) * 20
        else:
            return self.basic

class Four_wheeler(Vehicle):
    basic = 40
    def __init__(self,num_persons):
        super().__init__()
        self.num_persons = num_persons

    def calToll(self):
        if self.num_persons > 4:
            return self.basic + (self.num_persons - 4) * 40
        else:
            return self.basic

class Heavy(Vehicle):
    basic = 60
    def __init__(self,num_persons):
        super().__init__()
        self.num_persons = num_persons

    def calToll(self):
        if self.num_persons > 6:
            return self.basic + (self.num_persons - 6) * 100
        else:
            return self.basic

def main():  
    while(True):
        print('''Select your choice:
            1. Two wheeler
            2. Three Wheeler
            3. Four Wheeler
            4.Heavy vehicle
            5. Exit''')
        
        ch = int(input('Enter your choice'))

        if ch == 5:
            print('Thank you!')
            break
        num = int(input('Enter the no. of persons: '))
        if ch == 1:
            t = Two_wheeler(num)
        elif ch == 2:   
            t = Three_wheeler(num)
        elif ch == 3:             
            t = Four_wheeler(num)
        elif ch == 4:   
            t = Heavy(num)
        else:
            print('Invalid Choice!')
            continue

        toll = t.calToll()
        print("Total toll:",toll)
        

if __name__ == "__main__":
    main()