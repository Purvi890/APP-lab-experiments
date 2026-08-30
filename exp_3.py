from abc import ABC, abstractmethod


# Strategy
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit card strategy
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


# PayPal strategy
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid", amount, "using PayPal")


# Bitcoin strategy
class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")


# Context
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    # Change strategy
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Process payment
    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main function
def main():

    processor = PaymentProcessor(CreditCardPayment())

    processor.process_payment(1000)

    processor.set_strategy(PayPalPayment())
    processor.process_payment(2000)

    processor.set_strategy(BitcoinPayment())
    processor.process_payment(3000)


if __name__ == "__main__":
    main()