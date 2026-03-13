class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, payment):
        cls.hourly_payment = payment

    def salary(self):
        return self.hours * self.hourly_payment
    
#пример для проверки, так как в задаче его нет
employee = EmployeeSalary.get_hours("Alex", None, 2, "alex@email.com")
print(employee.hours)

employee2 = EmployeeSalary.get_email("Alex", 40, 2, None)
print(employee2.email)
