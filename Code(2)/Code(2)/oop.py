class Emp:
    nums_of_emps = 0
    raisePay = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.gmail = first + "." + last + "@gmail.com"
        self.pay = pay

        Emp.nums_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raisePay)


emp_1 = Emp("James", "Cooper", 50000)
emp_2 = Emp("Mary", "Johnson", 20000)

print(emp_1.fullname())