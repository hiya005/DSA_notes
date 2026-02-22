from abc import ABC, abstractmethod

# -------------------------------
# Abstract Base Class
# -------------------------------
class Employee(ABC):
    def __init__(self, emp_id, emp_name, basic_salary):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._basic_salary = basic_salary

    # Getter methods (Encapsulation)
    def get_emp_id(self):
        return self._emp_id

    def get_emp_name(self):
        return self._emp_name

    def get_basic_salary(self):
        return self._basic_salary

    # Setter method
    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    # Abstract method
    @abstractmethod
    def calculate_salary(self):
        pass


# -------------------------------
# Derived Class: PermanentEmployee
# -------------------------------
class PermanentEmployee(Employee):
    def __init__(self, emp_id, emp_name, basic_salary, allowances):
        super().__init__(emp_id, emp_name, basic_salary)
        self._allowances = allowances

    def calculate_salary(self):
        return self._basic_salary + self._allowances


# -------------------------------
# Derived Class: ContractEmployee
# -------------------------------
class ContractEmployee(Employee):
    def __init__(self, emp_id, emp_name, hours_worked, hourly_rate):
        super().__init__(emp_id, emp_name, 0)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate


# -------------------------------
# Payroll System Class
# -------------------------------
class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        for emp in self.employees:
            print("Employee ID   :", emp.get_emp_id())
            print("Employee Name :", emp.get_emp_name())
            print("Salary        :", emp.calculate_salary())
            print("-------------------------------")


# -------------------------------
# Main Program
# -------------------------------
def main():
    payroll = PayrollSystem()

    # Runtime Polymorphism
    emp1 = PermanentEmployee(101, "Alice", 25000, 5000)
    emp2 = ContractEmployee(102, "Bob", 100, 300)

    payroll.add_employee(emp1)
    payroll.add_employee(emp2)

    payroll.display_all_employees()


if __name__ == "__main__":
    main()
