from person import Person

class Employee(Person):
    def __init__(self, first_name, last_name, email_address, id_number, salary, job_role, employee_rating):
        super().__init__(first_name, last_name, email_address)

        self.id_number = id_number
        self._salary = salary
        self.job_role = job_role
        self.employee_rating = employee_rating

    # super() is used allows you to build classes that easily extend the functionality of previously
    # built classes without implementing their functionality again.

    def employee_account(self):
        print(f'{self.first_name} {self.last_name} employee id is {self.id_number}')

    # Getter method to get the pay of the employee. It gets the value of property.

    def get_pay(self):
        return self._salary

    # setter method - ensures data encapsulation and  sets the value of the property. Helps access private attributes.
    # def set_pay(self, p):
    #     if p > 500:
    #     self._salary = p

    def job_position(self):
        # self.job_role = job_role
           print(f'{self.first_name} {self.last_name} job role is {self.job_role}')



    def employee_score(self):
        self.employee_rating = range[0:10]

        if self.employee_rating > 7:
            print(f"{self.first_name} {self.last_name} ,finds working at Mcdonalds above average.")
        elif self._employee_rating < 7:
            print(f"{self.first_name} {self.last_name} finds working at Mcdonalds average.")
        elif self._employee_rating <5:
            print(f"{self.first_name} {self.last_name} finds working at Mcdonalds below.")











