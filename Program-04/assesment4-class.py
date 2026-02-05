class Employee:   #parent class
    def __init__(self,emp_id,name,place,address,phone):
        self.emp_id = emp_id
        self.name = name
        self.place = place
        self.address = address
        self.phone = phone
    def display_Employee(self):
        print("Employee Id :",self.emp_id)
        print("Name :",self.name)
        print("Place :",self.place)
        print("Address :",self.address)
        print("Phone : ",self.phone)
    
class PermanentEmployee(Employee):  #child class
    def __init__(self, emp_id, name, place, address, phone,joining_date, designation, salary):
        # Call parent class constructor
        super().__init__(emp_id, name, place, address, phone)

        self.joining_date = joining_date
        self.designation = designation
        self.salary = salary

    def display_Permanent(self): 
        self.display_Employee()
        print("Joining Date : ",self.joining_date)
        print("Designation : ",self.designation)
        print("Salary :",self.salary)

    
class ContractEmployee(Employee): #child class
    def __init__(self, emp_id, name, place, address, phone,start_date,contract_end_date, hourly_rate):
        super().__init__(emp_id, name, place, address, phone)
        self.start_date = start_date
        self.contract_end_date=contract_end_date
        self.hourly_rate = hourly_rate

    def display_Contract(self):
        self.display_Employee()
        print("Start Date : ",self.start_date)
        print("Contract End Date : ",self.contract_end_date)
        print("Hourly Rate :",self.hourly_rate)

permanent_emp = PermanentEmployee(
    101,
    "Anu",
    "Kochi",
    "MG Road",
    "9876543210",
    "2022-06-01",
    "Software Engineer",
    60000
)
contract_emp = ContractEmployee(
    201,
    "Rahul",
    "Trivandrum",
    "Technopark",
    "9123456780",
    "2024-01-01",
    "2024-12-31",
    500
)

permanent_emp.display_Permanent()
print("-"*30)
contract_emp.display_Contract()

