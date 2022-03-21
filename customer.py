from person import Person


class Customer(Person):
    def __init__(self, first_name, last_name, email_address, loyalty_card, favourite_item):
        super().__init__(first_name, last_name, email_address)
        self.loyalty_card = loyalty_card
        self.favourite_item = favourite_item

    def card(self):
        print(f'{self.first_name} {self.last_name} balance on their loyalty card is {self.loyalty_card}')

    def favourite_food(self):
        print(f'My favourite food is {self.favourite_item} ')
