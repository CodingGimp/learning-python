class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

employee_1 = Employee('Corey', 'Schafer', 50000)
employee_2 = Employee('Omair', 'Majid', 60000)

# print(Employee.raise_amount)
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)

print(Employee.num_of_employees)