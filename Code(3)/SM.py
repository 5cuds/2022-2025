class Emps:

    number_of_emps = 0

    def __init__(self, name, age, pay, role) -> None:
        self.name = name
        self.age = age
        self.pay = pay
        self.role = role
        number_of_emps += 1

    def get_info(self):

        return f"{self.name} = Pay: {self.pay} Role = {self.role}"
    
    @staticmethod
    def roles(role):
        roles = ["Cashier", "Cooker", "Worker"]
        return role in roles
        
print(Emps.roles("Cooker"))

        
