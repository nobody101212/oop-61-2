class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.__discount = 0

    def set_discount(self, percent):
        if 0 <= percent <= 50:
            self.__discount = percent
        else:
            print("Ошибка: скидка не может быть больше 50%")

    def get_price(self):
        return self._price * (1 - self.__discount / 100)

    def apply_extra_discount(self, secret_code):
        if secret_code == "VIP123":
            self._price *= 0.95
        else:
            print("Неверный код")


p = Product("Iphone", 1000)

p.set_discount(20)
print("Цена со скидкой:", p.get_price())

p.apply_extra_discount("VIP123")
print("Цена после VIP:", p.get_price())

p.apply_extra_discount("wrong")
print("Цена итоговая:", p.get_price())


from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print({
            "type": "crypto",
            "amount": amount,
            "currency": "USDT"
        })

    def refund(self, amount):
        print(f"Возврат криптой: {amount} USDT")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.pay(amount)


processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)






