# class Device: 
#     def __init__(self, name, autor, isWork: bool):
#         self._name = name
#         self._autor = autor
#         self._isWork = isWork

#     def __str__(self):
#         return f'Name: {self._name}\nAutor: {self._autor}\nStatus: {self._isWork}'



# class CoffeeMachine(Device): 
#     def __init__(self, name, autor, isWork, volume, typeCoffe):
#         super().__init__(name, autor, isWork)
#         self._volume = volume
#         self._typeCoffe = typeCoffe

#     def DoCoffe(self):
#         nameCoffe = input('What coffe you want: ')
#         print(f'You {nameCoffe}')

#     def __str__(self):
#         coffeM = super().__str__()
#         return f'{coffeM}\nVolume: {self._volume}\nType coffe: {self._typeCoffe}'


    
# class Blender(Device):
#     def __init__(self, name, autor, isWork, countSpid):
#         super().__init__(name, autor, isWork)
#         self._countSpid = countSpid

#     def __str__(self):
#         blander =  super().__str__()
#         return f'{blander}\nCount spid: {self._countSpid}'
    


# class MeatGrinder(Device):
#     def __init__(self, name, autor, isWork, countNozzle):
#         super().__init__(name, autor, isWork)
#         self._countNozzle = countNozzle

#     def __str__(self):
#         grinder = super().__str__()
#         return f'{grinder}\nCount nozzle: {self._countNozzle}'


# coffee_machine = CoffeeMachine(name="DeLonghi Magnifica", autor="DeLonghi Group", isWork=True, volume=1.8, typeCoffe="Beans")

# blender = Blender(name="Philips ProBlend", autor="Philips", isWork=True, countSpid=5)

# meat_grinder = MeatGrinder(name="Bosch ProPower", autor="Bosch", isWork=False, countNozzle=3)

# print(coffee_machine)
# print(blender)
# print(meat_grinder)






# class Ship: 
#     def __init__(self, name, speed):
#         self._name = name
#         self._speed = speed

#     def __str__(self):
#         return f'Name: {self._name}\nSpeed: {self._speed}'

# class Frigate(Ship):
#     def __init__(self, name, speed, sonarRange):
#         super().__init__(name, speed)
#         self._sonarRange = sonarRange

#     def __str__(self):
#         ship = super().__str__()
#         return f'{ship}\nSonar range: {self._sonarRange}'

#     def Scan(self):
#         return f'{self._name} scan plases'

# class Destroyer(Ship):
#     def __init__(self, name, speed, countMissile):
#         super().__init__(name, speed)
#         self._countMissile = countMissile

#     def __str__(self):
#         ship = super().__str__()
#         return f'{ship}\nCount missile: {self._countMissile}'


# class Cruiser(Ship):
#     def __init__(self, name, speed, mainCalibre):
#         super().__init__(name, speed)
#         self._mainCalibre = mainCalibre

#     def __str__(self):
#         ship = super().__str__()
#         return f'{ship}\nMain calibre: {self._mainCalibre}'

#     def fullVolley(self):
#         return f'{self._name} do fires a salvo from guns of {self._mainCalibre} caliber'




class Money:
    def __str__(self, units, cents, name):
        self._units = units
        self._cents = cents
        self._name = name

    def countMoney(cents, units):
        if cents > 100:
            units += 1

    def __str__(self):
        return f'Name: {self._name}\nCount: {self.countMoney(self._units, self._cents)}'

class Product: 
    def __init__(self, name, money:Money):
        self._name = name
        self._money = money

    def __str__(self):
        return f'Name: {self._name}\nPrice: {self._money}'