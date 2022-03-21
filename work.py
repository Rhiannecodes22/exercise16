from employee import Employee
from customer import Customer
# first_name, last_name, email_address, id_number, salary, job_role, employee_rating)
employee1 = Employee("Andrew", "Smith", "", 145674, 300, "Store manager", 9)
employee2 = Employee("Amy", "Ali", "", 456345, 350, "Senior manager", 2)
employee3 = Employee("Ade", "Adegoke", "", 567345, 189 , "Assistant", 9)

# self, first_name, last_name, email_address, loyalty_card, favourite_item):
customer1 = Customer("Kiera", "Unice", "", 12, "the Big Mac")
customer2 = Customer("Benjamin", "Brown", "", 34, "the Mcflurry")
customer3 = Customer("Farhia", "Craya", "", 56, "the Apple pie")

customer1.introduce()
customer1.last_name
customer1.favourite_food()
customer1.email()
customer1.loyalty_card

customer2.introduce()
customer3.introduce()


employee1.introduce()
employee1.employee_account()
employee1.email()
employee1.job_position()
# employee1.employee_score()
# EMPLOYEE SCORE and SETTER NOT WORKING? something wrong with code in employee class.

# Getter
print(employee1.get_pay)

# # Setter
# employee1.set_pay('304')
# print(

