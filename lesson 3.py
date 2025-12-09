





































#абстракция
from abc import ABC, abstractmethod

#абстркатный класс Animal
class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def voce(self):
        pass

class Dog(Animal):

    def move(self):
        return "Ходит"

    def voce(self):
        return "Гав Гав"


my_dog = Dog()
print(my_dog.move())
print(my_dog.voce())

class User:
    def __init__(self, name, country):
        self.name = name
        self.country = country

ardager2 = User("ardager", 'KG')

class ABCSendOTP(ABC):
    @abstractmethod
    def send_otp(self):
        pass

class KGSendOTP(ABC):

    def send_otp(self):
        sms = '<Text>1234</Text><PhoneNumber>+996507101207</PhoneNumber>'

        class RUSendOTP(ABCSendOTP):
            def send_otp(self):
                sms = {
                    'text': "1234",
                    'phone number': "+996507101207"
                }


class Register:
    def __init__(self, country1, country2):
        self.countryKG = country1
        self.countryRU = country2

    def register(self, user):
        if user.country1 == "KG":
            self.countryKG.send_otp()
        elif user.country2 == "RU":
            self.countryRU.send_otp()

register1 = Register(KGSendOTP(), KGSendOTP())
print(register1.register(ardager2))















































