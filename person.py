class Person:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def introduce(self):
        print(f'Hi, my name is {self.first_name}')

    def email(self):
        print(f'{self.first_name} {self.last_name}. @Mcdonalds.com')
